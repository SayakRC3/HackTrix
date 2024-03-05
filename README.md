# HackTrix
All we coded for Hacktrix together tap tap tap <br>

# Project Overview
Wearable sensors with Human Activity Recognition revolutionize medical diagnostics, monitoring patient movements in real-time for early anomaly detection and personalized interventions. This improves outcomes and cuts healthcare costs. Thus we introduce our device - "Monitwatch," a compact wearable device that integrates various sensors like heart rate, SpO2, EEG, and motion sensors. It measures crucial health metrics such as SpO2 levels, heart rate, temperature, and patient movement data. It also features a lightweight "vest" with integrated detection probe interfaces  monitors cardiovascular and muscular activity using ECG, EOG, and EEG probes. Small probes detect abnormalities, including those leading to heart attacks, while gyroscope sensors accurately detect mobility accidents such as falls. Encoded results from sensors are processed by an autoencoder model while patient motion tracking data is monitored and analyzed using an RNN-based LSTM model for comprehensive health insights. Predictions are decoded and compared to actual outcomes, generating alerts if discrepancies exceed a set threshold. Alerts promptly notify patients of abnormalities, enabling timely intervention and treatment.

# Tech Stack //sensors used, Processors used, Model Used 
__Sensors Used__
1. MAX 30102 Pulse Oximeter and Heart rate sensor (SpO2 and heart rate) Sensor: Measures oxygen levels in the bloodstream and our heartrate, offering valuable insights into cardiovascular health and oxygenation status
2. Motion Sensors: These sensors monitor our body's movements.
3. Accelerometer and Gyroscope Sensor MPU6050: Measures acceleration in three dimensions (X, Y, and Z) and angular velocity in three axes and provide information about rotational movements.
4. BioAmp EXE pill: 

<img src='https://github.com/SayakRC3/HackTrix/assets/137310893/3c9feacf-e12c-417e-baef-db64319357e5' height=250/>
<img src='https://github.com/SayakRC3/HackTrix/assets/137310893/3c9feacf-e12c-417e-baef-db64319357e5' height=250/>
<img src='https://github.com/SayakRC3/HackTrix/assets/137310893/3c9feacf-e12c-417e-baef-db64319357e5' height=250/>


__Microprocessors and Microcontrollers__
1. Raspberry Pi 4B:Data collection and feeding into the ML model are managed by the Raspberry Pi 4 B, a versatile and affordable single-board computer renowned for its computational capabilities and broad range of applications.
2. ESP32-WROOM:The ESP32 connects wirelessly to any of the Cloud platform. This cloud platform provides a user-friendly interface for managing and storing sensor data. The ESP32 sends the collected data (heart rate, SpO2, accelerometer, and gyroscope readings) to the Cloud on a regular basis. This makes the data easily available for analysis and anomaly identification.

__Modules and Development Boards__
1. 
__ML Model__
Autoencoder architecture for ECG anomaly detection
