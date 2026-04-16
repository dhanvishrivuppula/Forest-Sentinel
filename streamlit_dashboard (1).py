import streamlit as st
import requests
import pandas as pd
import time
import json
from datetime import datetime

st.set_page_config(page_title="Forest Sentinel", page_icon="🌲", layout="wide")

# --- CSS STYLING ---
st.markdown("""
<style>
    .critical-alert { background-color: #ff4b4b; color: white; padding: 20px; border-radius: 10px; text-align: center; font-size: 30px; font-weight: 900; animation: blink 1s infinite; border: 4px solid white; margin-bottom: 20px; }
    @keyframes blink { 0% { opacity: 1; } 50% { opacity: 0.8; } 100% { opacity: 1; } }
    .radar-box { background: linear-gradient(90deg, #0f5132, #198754, #0f5132); color: white; padding: 15px; border-radius: 8px; text-align: center; font-size: 18px; font-weight: bold; margin-bottom: 20px; }
    .action-box { background-color: #2b2b2b; color: white; padding: 20px; border-radius: 8px; border-left: 5px solid #ff4b4b; margin-bottom: 15px; }
    .cam-safe { background-color: #198754; color: white; padding: 10px; border-radius: 5px; text-align: center; font-weight: bold; }
    .cam-danger { background-color: #ff4b4b; color: white; padding: 10px; border-radius: 5px; text-align: center; font-weight: bold; animation: blink 1s infinite; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("🌲 Forest Sentinel")
    st.caption("Edge-AI LoRaWAN Command Center")
    st.success("Status: SECURELY CONNECTED")
    st.info(f"Last Sync: {datetime.now().strftime('%H:%M:%S')}")
    st.markdown("---")
    st.write("**Active Network:** 3 Nodes Deployed")
    st.write("📡 Gateway: Ntfy Secure Bridge")

# --- MAIN DASHBOARD HEADER ---
st.title("📡 Regional Monitoring Command")
st.markdown("Real-time telemetry and multi-node AI vision feed.")

if 'last_alert' not in st.session_state:
    st.session_state.last_alert = ""

# --- INDESTRUCTIBLE NETWORK BLOCK ---
try:
    response = requests.get("https://ntfy.sh/gnits_panel_final_v1/json?poll=1", timeout=5)
    
    latest_conf = 0
    msg_id = ""

    if response.status_code == 200:
        messages = response.text.strip().split('\n')
        for line in messages:
            if line:
                data = json.loads(line)
                if data.get('event') == 'message':
                    try:
                        latest_conf = float(data.get('message', 0))
                        msg_id = data.get('id', "")
                    except:
                        pass
                        
    if latest_conf >= 10: 
        # 🔴 FIRE DETECTED UI
        st.markdown(f'<div class="critical-alert">🚨 URGENT: WILDFIRE DETECTED AT CAM_01! 🚨<br>AI Confidence: {latest_conf}%</div>', unsafe_allow_html=True)
        
        if msg_id != st.session_state.last_alert:
            st.toast("🔥 SECURE FIRE ALERT RECEIVED!", icon="🚨")
            st.session_state.last_alert = msg_id
        
        # 📍 EXACT LOCATION TEXT
        st.error("**📍 EXACT LOCATION MATCH:** Sector 4, Whisper Valley Reserve | **Lat:** 17.4124, **Lon:** 78.3988")

        # Split Map and Action Plan
        map_col, action_col = st.columns([2, 1])
        
        with map_col:
            st.subheader("🗺️ Live GPS Tracking")
            st.map(pd.DataFrame({'lat': [17.4124], 'lon': [78.3988]}), zoom=15)
            
            # Multi-Camera Status
            st.markdown("### 📷 Multi-Node Network Status")
            c1, c2, c3 = st.columns(3)
            c1.markdown('<div class="cam-danger">📹 Cam_01 (Whisper Valley)<br>🔥 ALERT</div>', unsafe_allow_html=True)
            c2.markdown('<div class="cam-safe">📹 Cam_02 (Pine Ridge)<br>✅ SAFE</div>', unsafe_allow_html=True)
            c3.markdown('<div class="cam-safe">📹 Cam_03 (River Bend)<br>✅ SAFE</div>', unsafe_allow_html=True)

        with action_col:
            st.subheader("⚠️ Emergency Protocols")
            st.markdown("""
            <div class="action-box">
                <b>Immediate Actions Required:</b><br><br>
                1. 📞 Dispatch Rapid Response Team Alpha.<br>
                2. 🚁 Activate drone surveillance over Sector 4.<br>
                3. 📢 Issue evacuation warning to nearby wildlife zones.<br>
                4. 💧 Prime aerial water tankers on standby.
            </div>
            """, unsafe_allow_html=True)
            st.button("Acknowledge Alert & Dispatch Teams", type="primary", use_container_width=True)

    else:
        # 🟢 NORMAL UI
        st.markdown('<div class="radar-box">📡 Radar Scanning: Normal. No anomalies detected.</div>', unsafe_allow_html=True)
        
        st.success("**📍 CURRENT PATROL:** Sector 4, Sector 7, and Sector 2 are secure.")

        map_col, node_col = st.columns([2, 1])
        with map_col:
            st.subheader("🗺️ Active Node Locations")
            # Show all 3 cameras on the map during normal patrol
            df_cams = pd.DataFrame({
                'lat': [17.4124, 17.4150, 17.4080],
                'lon': [78.3988, 78.4020, 78.3950],
                'name': ['Cam_01', 'Cam_02', 'Cam_03']
            })
            st.map(df_cams, zoom=13)
        
        with node_col:
            st.markdown("### 📷 Network Status")
            st.markdown('<div class="cam-safe" style="margin-bottom:10px;">📹 Cam_01 (Whisper Valley) - ✅ SAFE</div>', unsafe_allow_html=True)
            st.markdown('<div class="cam-safe" style="margin-bottom:10px;">📹 Cam_02 (Pine Ridge) - ✅ SAFE</div>', unsafe_allow_html=True)
            st.markdown('<div class="cam-safe">📹 Cam_03 (River Bend) - ✅ SAFE</div>', unsafe_allow_html=True)
        
except Exception as e:
    st.markdown('<div class="radar-box">📡 Scanning Secure Network...</div>', unsafe_allow_html=True)

# Auto-refresh safely
time.sleep(2)
st.rerun()