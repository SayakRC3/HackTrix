# HackTrix

# Project Overview
Wearable sensors with Human Activity Recognition revolutionize medical diagnostics, monitoring patient movements in real-time for early anomaly detection and personalized interventions. This improves outcomes and cuts healthcare costs. Thus we introduce our device - "Monitwatch," a compact wearable device that integrates various sensors like heart rate, SpO2, EEG, and motion sensors. It measures crucial health metrics such as SpO2 levels, heart rate, temperature, and patient movement data. It also features a lightweight "vest" with integrated detection probe interfaces  monitors cardiovascular and muscular activity using ECG, EOG, and EEG probes. Small probes detect abnormalities, including those leading to heart attacks, while gyroscope sensors accurately detect mobility accidents such as falls. Encoded results from sensors are processed by an autoencoder model while patient motion tracking data is monitored and analyzed using an RNN-based LSTM model for comprehensive health insights. Predictions are decoded and compared to actual outcomes, generating alerts if discrepancies exceed a set threshold. Alerts promptly notify patients of abnormalities, enabling timely intervention and treatment.

<img src = 'https://github.com/SayakRC3/HackTrix/assets/137310893/9d0d9884-e0e7-428b-af6e-b3c4dfbc8d3d' height = 300/>
<img src = 'https://github.com/SayakRC3/HackTrix/assets/137310893/280535e6-81e1-485d-838f-7b52315c556f' height = 200/>


# Tech Stack //sensors used, Processors used, Model Used 
__Sensors Used__
1. MAX 30102 Pulse Oximeter and Heart rate sensor (SpO2 and heart rate) Sensor: Measures oxygen levels in the bloodstream and our heartrate, offering valuable insights into cardiovascular health and oxygenation status
2. Motion Sensors: These sensors monitor our body's movements.
3. Accelerometer and Gyroscope Sensor MPU6050: Measures acceleration in three dimensions (X, Y, and Z) and angular velocity in three axes and provide information about rotational movements.
4. BioAmp EXG pill: The BioAmp EXG Pill is a compact AFE signal-acquisition board compatible with MCUs and SBCs, enabling precise monitoring of ECG, EEG, and EMG signals.
<img src='https://github.com/SayakRC3/HackTrix/assets/137310893/0a8fb0c5-ad62-410d-b309-58b982a5d261' height=700/>

__Microprocessors and Microcontrollers__
1. Raspberry Pi 4B:Data collection and feeding into the ML model are managed by the Raspberry Pi 4 B, a versatile and affordable single-board computer renowned for its computational capabilities and broad range of applications.
2. ESP32-WROOM:The ESP32 connects wirelessly to any of the Cloud platform. This cloud platform provides a user-friendly interface for managing and storing sensor data. The ESP32 sends the collected data (heart rate, SpO2, accelerometer, and gyroscope readings) to the Cloud on a regular basis. This makes the data easily available for analysis and anomaly identification.

__Modules and Development Boards__
1. GSM Module: The SIM900 GSM module provides reliable and efficient communication capabilities for various IoT and M2M applications. With its compact size and versatile features, it facilitates seamless integration into a wide range of projects requiring GSM connectivity.

__ML Model__
1.Autoencoder Preprocessing: The dataset is preprocessed using an autoencoder. The autoencoder is trained to reconstruct the input data, capturing normal patterns within the features. The encoder part of the autoencoder extracts encoded representations (latent features) from the data.
<img src='https://github.com/SayakRC3/HackTrix/assets/137310893/1146f6a3-386c-4650-93ab-2e242883c4c6' height=400/>

2. Transformer-based Anomaly Detection: A Transformer-based model is built and trained using the encoded representations obtained from the autoencoder as input. The Transformer model further captures temporal dependencies and patterns within the encoded representations.
<img src='https://github.com/SayakRC3/HackTrix/assets/137310893/df4a4e49-da08-4313-94fc-ff18fe5dea61' height=400/>

3. Anomaly Detection: Anomaly detection is performed by combining the reconstruction error from the autoencoder with deviations from the predictions of the Transformer-based model.The combined anomaly scores are compared to a predefined threshold. Data points with anomaly scores above the threshold are classified as anomalies.If ground truth labels are available, the model's accuracy in detecting anomalies can be computed by comparing the binary predictions with the ground truth labels.
4. Another model implemented was an LSTM architecture on Gyroscope and Accelerometer Dataset to capture relationship b/w Features in X,Y,Z direction using tensorflow framework
The model was able to achieve 86% accuracy on testing data from the actual sensors

Libraries Used:
- NumPy: For numerical computations and array operations.
- Pandas: For data manipulation and preprocessing.
- TensorFlow/Keras: For building and training neural network models.
- Scikit-learn: For splitting the dataset into training and testing sets.
- Matplotlib: For data visualization.

  

