# README
# =====================================================================
# PROJECT TITLE: 
# =====================================================================
# Development of a Flask-based web application for collecting and analyzing healthcare user, income 
# and expense data using Python and deployment on AWS EC2 with MongoDB Atlas for data storage.
# =====================================================================
# Created by: Victor Kadiri
# Date Created: 17th April 2025
# =====================================================================
# OBJECTIVE:
# =====================================================================
# The objective of the series of python script below is to create and deploy a Flask-based web application for collecting and analyzing healthcare expense data using Python, mongo DB and AWS EC2
# =====================================================================
# KEY FEATURES:
# =====================================================================
# - User-friendly web form for data collection
# - MongoDB backend for secure data storage
# - Automated data processing and visualization
# - Production-ready deployment on AWS EC2 - Please visit url - /http://13.48.24.60/ on your browser to view the app.
# - Comprehensive data export capabilities

# =====================================================================
# PROJECT WORKFLOW:
# =====================================================================
# 1. User submits form → Data stored in MongoDB
# 2. Automated CSV export generated
# 3. Jupyter notebook processes data
# 4. Visualizations generated:
#    - gender_spending_distribution.png: Stacked bar chart showing spending patterns by category
#    - top_ages_income.png: Bar chart of highest income age groups

# =====================================================================
# PROJECT STRUCTURE:
# =====================================================================
# ├── templates/
# │ ├── index.html # Survey form template
# │ └── thank_you.html # Submission confirmation
# ├── requirements.txt # Python dependencies
# ├── app.py # Main Flask application
# ├── app.ini # Gunicorn configuration
# ├── data_vis.ipynb # Data analysis notebook
# ├── user_data.csv # Raw exported data
# └── processed_user_data.csv # Analyzed data
# └── gender_spending_distribution.png - Shows the gender distribution across spending categories.
# └── top_ages_income.png - Shows the ages with the highest income.

# =====================================================================
# PREREQUISITES:
# =====================================================================
# - Tools Required 
# 1. Download and Install VS Code 
# 2. Download and Install Python 3.12.9 or higher
# 3. MongoDB Atlas account
# 4. AWS account

# The following Python libraries are used in this analysis/app development and need to be installed:
### Core Libraries:
# Flask
# pymongo
# pandas
# jupyter
# matplotlib
# python-dotenv
# gunicorn
# seaborn
# numpy
# certifi

### Installation Command:
# ----  ```bash
# ----  pip install -r requirements.txt

# =====================================================================
# PROCEDURES:
# =====================================================================
# 1. Deployment Steps
# AWS EC2 Deployment - Visit prod url - /http://13.48.24.60/ to view the app on your browser.
# - Launch EC2 instance (Ubuntu, t2.micro)
# - Configure security group (ports 22, 80)
# - Connect via SSH by running command:
# bash - ssh -i "your-key.pem" ubuntu@your-ec2-ip
# - Install dependencies:
# bash - sudo apt update && sudo apt install python3-pip python3-venv nginx git
# - Clone repository and set up environment
# - Configure Nginx reverse proxy
# - Set up PM2 process manager

# 2. MongoDB Atlas Configuration
# - Create free cluster on MongoDB Atlas
# - Configure network access (IP whitelisting)
# - Create database user with read/write privileges
# - Get connection string

# Support:
#   For questions or issues, please open an issue on the GitHub repository.

# Note:
# Refer to the python scripts for the step by step understanding of the model.

