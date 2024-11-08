# IoT Predictive Maintenance System

This repository implements a comprehensive IoT Predictive Maintenance System using Kafka for real-time data streaming, Spark for data processing, and AWS IoT for cloud connectivity. The project includes machine learning models for failure prediction, using MLflow to track experiments and manage model versions.

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
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

## Project Structure

The repository follows a modular structure for scalability and clarity.

```plaintext
├── configs/
│   ├── kafka_config.yaml             # Kafka configuration for producer and consumer
│   ├── spark_config.yaml             # Spark configuration settings
│   └── model_config.yaml             # Model hyperparameters and training configurations
│
├── data/
│   ├── raw_data.csv                  # Raw sensor data (if available)
│   └── processed/                    # Directory for processed data files
│
├── scripts/
│   ├── aws_iot_config.json           # Configuration for AWS IoT Core connection
│   ├── kafka_producer.py             # Kafka producer script for streaming sensor data
│   ├── preprocess_data.py            # Script to preprocess data for model training
│   └── mlflow_experiment.py          # MLflow script to track experiments and model metrics
│
├── README.md                         # Project documentation
└── requirements.txt                  # Python dependencies

