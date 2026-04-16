# Forest-Sentinel
An Edge-AI &amp; IoT wildfire detection system utilizing YOLOV8 and sensor fusion to eliminate false alarms and deliver real-time LoRaWAN telemetry. Also consists of dual-verification edge-computing architecture for real-time wildfire detection including low-latency.
# 🌲 Forest Sentinel: Edge-AI Wildfire Detection

### **Overview**
Forest Sentinel is a hardware and software system built for real-time wildfire detection. We designed it to act as the "eyes and ears" of a forest by combining environmental sensors with on-device computer vision.

### **The Problem We Are Solving**
Current wildfire detection methods have two major bottlenecks:
* **High Latency:** Satellite monitoring (like MODIS) takes hours to pass over a sector and has poor ground resolution.
* **False Alarms:** Ground-level optical smoke sensors are easily tricked by fog, dust, or humidity. This causes false positives that waste emergency resources.

### **Our Approach: Sensor Fusion & YOLOv8**
We built a "Dual-Verification" setup to fix the false alarm issue. Our hardware node uses DHT11 and MQ2 sensors to constantly monitor the area's temperature, humidity, and gas levels. 

If the sensors detect a spike, they wake up an onboard camera running a **YOLOv8** computer vision model. The system only sends a critical alert if it detects a chemical change *and* visually confirms the fire. If the AI just sees fog, or if the sensors just smell normal dust, the alarm is cancelled.

### **IoT & LoRaWAN Transmission**
Transmitting video from a forest is impossible due to LoRaWAN bandwidth limits. To solve this, our edge node processes the video locally and compresses the result into a tiny 2-byte payload (just the device ID and the AI's confidence score). This lightweight data is sent through a secure IoT bridge (`ntfy.sh`) to our live web dashboard.

---

### **💻 Tech Stack**
* **AI / Vision:** YOLOv8, OpenCV
* **Data Processing:** Python, Pandas, Scikit-Learn
* **Dashboard:** Streamlit
* **Networking:** Ntfy (HTTP IoT Bridge simulation)

---

### **📂 Repository Structure**
* `/Edge_Node` - Contains the Google Colab (`.ipynb`) script for the YOLOv8 vision inference and the data transmission code.
* `/Command_Center` - Contains the Streamlit `main.py` dashboard, including our live GPS mapping UI and action protocols.

---

### **🚀 How to Run the Project**

**1. Start the Command Center**
1. Open the `Command_Center` folder in your terminal.
2. Install dependencies: `pip install streamlit pandas requests`
3. Launch the dashboard: `streamlit run main.py`
4. View the dashboard at `localhost:8501`.

**2. Trigger the Edge Node**
1. Open the `/Edge_Node` folder and load the `.ipynb` file into Google Colab.
2. Run the cells to load the YOLOv8 model and turn on your webcam.
3. Hold up a picture of a fire to the camera.
4. Once the AI confidence hits the threshold, the script will instantly transmit the payload and trigger the red alert on your local dashboard.

---
