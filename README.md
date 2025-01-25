Python Project for Data Engineering
Overview
This project is part of the "Python Project for Data Engineering" course offered by IBM on Coursera. The primary objective is to acquire, process, and analyze data related to the world's largest banks. The project involves extracting data from various sources, transforming it into a usable format, and loading it into a database for further analysis.

Objectives
Data Extraction: Collect data using APIs and web scraping techniques.
Data Transformation: Process and clean the data to ensure accuracy and consistency.
Data Loading: Store the transformed data in a CSV file and a SQLite database.
Data Analysis: Perform queries on the database to retrieve specific information.
Project Structure
The repository contains the following files:

banks_project.py: Main script containing functions for data extraction, transformation, and loading.
Largest_banks_data.csv: CSV file containing the raw data of the largest banks.
exchange_rate.csv: CSV file with exchange rate information for currency conversion.
Banks.db: SQLite database containing the processed data.
code_log.txt: Log file recording the steps and operations performed during the project.
README.md: This README file providing an overview of the project.
Requirements
To run the project, ensure you have the following installed:

Python 3.x
Required Python libraries (listed in requirements.txt)
You can install the necessary libraries using:

bash
Copy
Edit
pip install -r requirements.txt
Usage
To execute the project, run the banks_project.py script:

bash
Copy
Edit
python banks_project.py
This will perform the following steps:

Data Extraction:

Scrape data from the specified website to obtain information about the largest banks.
Read exchange rate data from the provided CSV file.
Data Transformation:

Clean and organize the extracted data.
Convert financial figures into multiple currencies (USD, GBP, EUR, INR) using the exchange rates.
Data Loading:

Save the transformed data into a CSV file.
Load the data into a SQLite database (Banks.db).
Data Analysis:

Execute predefined queries to analyze the data stored in the database.
