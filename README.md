# Project Idea:
Internet Speed Progress in Algeria

## Overview
This project explores and analyzes the Ookla internet dataset about Algeria using exploratory data analysis (EDA) techniques. The goal is to understand trends, patterns, and insights from the data.

## Tools and Libraries
- **Python** the programming language.
- **FastAPI** for api development.
- **NumPy** for numerical operations
- **Pandas** for data manipulation
- **Matplotlib** and **Seaborn** for visualizations

# Data Overview

### Link: https://www.kaggle.com/datasets/dimitrisangelide/speedtest-data-by-ookla

## Context
Ookla is the global leader in network intelligence and connectivity insights. The company owns the world-renowned Speedtest platform which is the definitive way to test the speed and performance of your internet connection.
## Content
The datasets provide global fixed broadband and mobile (cellular) network performance metrics in zoom level 16 web mercator tiles (approximately 610.8 meters by 610.8 meters at the equator). Download speed, upload speed, and latency are collected via the Speedtest by Ookla applications for Android and iOS and averaged for each tile. Measurements are filtered to results containing GPS-quality location accuracy.

- **Name**
- **Number of Records**
- **Devices**
- **Tests**
- **Avg. Avg U Kbps**
- **Avg. Avg D Kbps**
- **Avg Lat Ms**
- **Avg. Pop2005**
- **Rank Upload**
- **Rank Download**

# FastAPI Documentation

## Version: 0.1.0

This API allows users to upload and download raw or processed data.


## Endpoints

### 1. **Upload Data**
- **Path**: `/upload/{type}`
- **Method**: `POST`
- **Summary**: Upload Raw or Processed Data to the API
- **Description**: Allows uploading of raw or processed data to the API.
- **Parameters**:
  - `type` (path parameter): Specifies the type of data to upload (required).
- **Request Body**:
  - JSON object: Contains the data to upload.
- **Responses**:
  - **200 OK**: Successful response (no content).
  - **422 Unprocessable Entity**: Validation error with details.

---

### 2. **Download Data**
- **Path**: `/download/{type}`
- **Method**: `GET`
- **Summary**: Download Raw or Processed Data from the API
- **Description**: Allows downloading of raw or processed data from the API.
- **Parameters**:
  - `type` (path parameter): Specifies the type of data to download (required).
- **Responses**:
  - **200 OK**: Successful response (no content).
  - **422 Unprocessable Entity**: Validation error with details.


# Workflow
### 1. Data Collection
### 2. Data Cleaning & Processing
- 2.1 Handling Missing Values
- 2.2 Handling Duplicates
- 2.3 Date Handling
- 2.4 Feature Engineering
### 3. Data Exploration & Visualization
### 4. Insights & Conclusion

# How to Run
### 1. Clone this repository:
```
git clone https://github.com/AmeUr56/Algerian-Internet-Connectivity
```
### 2. Install the required libraries:
```
pip install -r requirements.txt  
```
## 3. Run the API
```
cd api
uvicorn app:app
```
### 4. Run the Jupyter notebooks or Python scripts to explore the data.

# Contribution
Feel free to contribute by submitting pull requests or reporting issues!

# License
This web app is licensed under the MIT License.
Copyright (c) 2024 [Ameur].