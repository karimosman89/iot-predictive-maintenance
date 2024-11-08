# IoT Predictive Maintenance System

This repository implements a comprehensive IoT Predictive Maintenance System using Kafka for real-time data streaming, Spark for data processing, and AWS IoT for cloud connectivity. The project includes machine learning models for failure prediction, using MLflow to track experiments and manage model versions.

## Table of Contents
- [Overview](#overview)
- [Key Components](#key-components)
  - [AWS IoT Integration](#aws-iot-integration)
  - [Kafka Streaming](#kafka-streaming)
  - [Data Preprocessing](#data-preprocessing)
  - [Machine Learning with MLflow](#machine-learning-with-mlflow)
- [Setup Instructions](#setup-instructions)
  - [Requirements](#requirements)
  - [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This IoT Predictive Maintenance System is designed to monitor sensor data from connected devices, predict potential failures, and alert users before a breakdown occurs. The pipeline:
1. Simulates sensor data and streams it to Kafka.
2. Processes data in real-time with Spark.
3. Connects to AWS IoT Core for device management.
4. Uses machine learning models for predictive analytics, tracking experiments and versions with MLflow.


## Key Components

### AWS IoT Integration

The AWS IoT Core configuration (aws_iot_config.json) enables cloud connectivity for managing IoT devices and sending/receiving data securely. This part supports real-time data management and monitoring through AWS's secure infrastructure.

**Kafka Streaming**
The kafka_producer.py script generates and streams simulated sensor data (e.g., temperature, vibration, pressure) to a Kafka topic. Kafka serves as the data backbone for processing and analytics, enabling scalable and real-time data handling.

### Data Preprocessing

The preprocess_data.py script cleans and prepares raw data, making it suitable for model training. Preprocessing steps include:

**Missing value handling:** Removes or imputes missing data.
**Scaling:** Standardizes data for consistent model performance.
**Feature engineering:** Adds or transforms features based on analysis requirements.

### Machine Learning with MLflow
The mlflow_experiment.py script handles model training, tracking, and version control with MLflow. Key features include:

**Experiment logging:** Tracks model parameters, metrics, and training details.
**Model registry:** Saves models in MLflow for easy retrieval and deployment.
**Hyperparameter management:** Uses configurations from model_config.yaml for model consistency and reproducibility.

## Setup Instructions

### Requirements
Ensure you have the following installed:

**Python 3.8+**
**Kafka (locally or a Kafka cluster)**
**Spark for distributed processing**
**MLflow for experiment tracking**

### Configuration

1. Clone the Repository:


           git clone https://github.com/karimosman89/iot-predictive-maintenance.git
   
           cd iot-predictive-maintenance

3. Install Dependencies:


             pip install -r requirements.txt

4. Configure Services:

Update the aws_iot_config.json file with AWS IoT Core details.
Modify the configs/kafka_config.yaml and configs/spark_config.yaml to match your Kafka and Spark environments.
Set model parameters in configs/model_config.yaml for training and evaluation.


## Usage
1. Start Kafka Producer: Run the kafka_producer.py script to start streaming sensor data to Kafka.


             python scripts/kafka_producer.py

2. Preprocess Data: After gathering sufficient data, preprocess it for model training.


            python scripts/preprocess_data.py

3. Run MLflow Experiment: Use the mlflow_experiment.py script to train and log the model.


            python scripts/mlflow_experiment.py

Check your MLflow UI at http://localhost:5000 (or configured port) to view experiment results.

## Contributing

We welcome contributions to enhance the IoT Predictive Maintenance System. Please fork the repository and create a pull request with any additions or improvements.



## Acknowledgements

This project utilizes open-source libraries and tools, including Kafka, Spark, and MLflow. We appreciate the contributions of the open-source community in making such tools accessible.




---

### **Explanation of Each Section**

- **Overview**: Briefly explains the purpose and functionality of the project.
- **Project Structure**: Outlines the files and folders, helping users navigate and understand the code organization.
- **Key Components**: Describes each module, such as AWS IoT, Kafka, data preprocessing, and MLflow integration.
- **Setup Instructions**: Guides users through cloning the repository, installing dependencies, and configuring each component.
- **Usage**: Provides a step-by-step walkthrough on running each part of the project.
- **Contributing**: Invites others to contribute, making it clear how they can get involved.
- **License**: States the license under which the code is shared.


