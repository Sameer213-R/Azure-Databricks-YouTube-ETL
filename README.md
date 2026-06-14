# Azure-Databricks-YouTube-ETL

## Project Overview

This project is an end-to-end Data Engineering solution developed using Azure Databricks for analyzing live streaming data from YouTube news channels.

The pipeline collects real-time streaming data, performs data cleaning and transformation, loads the processed data into a Star Schema-based Data Warehouse, and provides interactive dashboards for business analysis.

## Business Problem

News channels generate a large amount of live streaming data. Analyzing viewer engagement, likes, comments, and audience interaction in real-time helps understand content performance and viewer behavior.

## Technology Stack

* Azure Databricks
* PySpark
* Azure Dashboard
* Delta/Parquet Files
* SQL
* GitHub

## Data Pipeline Architecture
## Project Workflow

![Workflow](Architecture%20Diagram/workflow.png)
## Dashboard Preview
![Dashboard](Architecture%20Diagram/dashboard.png)

### Bronze Layer (Raw Data)

* Collect live streaming data from YouTube channels
* Store raw data in JSON format

### Silver Layer (Data Cleaning & Transformation)

Data transformations performed:

* Data Type Casting
* Remove Extra Spaces
* UTC to IST Time Conversion
* Create Date Column
* Create Hour Column
* Calculate Engagement Rate
* Data Validation
* Store Cleaned Data in Parquet Format

### Gold Layer (Data Warehouse)

Implemented Star Schema Architecture

Fact Table:

* Fact_YouTube_Analytics

Dimension Tables:

* Dim_Channel

### Dashboard & Analytics

Created interactive Azure Dashboards for:

* Views Analysis
* Likes Analysis
* Comment Analysis
* Engagement Rate Analysis
* Channel Performance Comparison
* Hourly Performance Analysis

## Project Workflow

1. Collect Live Data from YouTube Channels
2. Store Raw Data as JSON
3. Clean and Transform Data
4. Save Processed Data as Parquet
5. Create Star Schema
6. Load Data into Gold Layer
7. Build PowerBI Dashboard
8. Generate Business Insights

## Key Features

* End-to-End ETL Pipeline
* Data Warehousing using Star Schema
* Real-Time Analytics
* Automated Data Transformation
* Interactive Dashboard Reporting

## Project Outcome

The solution enables efficient monitoring of YouTube live stream performance and provides actionable insights through a scalable Azure Data Engineering architecture.
