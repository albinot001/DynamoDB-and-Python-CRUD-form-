# CRUD form with Python and DynamoDB

## Overview

This project is a school project demonstrating the use of AWS DynamoDB with a Python script. It includes basic CRUD operations (Create, Read, Update, Delete) for managing items in a DynamoDB table.

## Prerequisites

- Python 3.x installed
- AWS account with DynamoDB table created

## Setup

1. Clone the repository:

   ```bash
   https://github.com/albinot001/DynamoDB-and-Python-CRUD-form-.git
   cd DynamoDB-and-Python-CRUD-form
   ```

Install dependencies:

   ```bash
   pip install -r requirements.txt
   pip install boto3
   ```

Replace the placeholder values in the index.py file with your AWS credentials and DynamoDB table name.

python

# Replace these values with your AWS credentials
   ```bash
   aws_access_key = 'your-access-key'
   aws_secret_key = 'your-secret-key'
   ```

# Set your DynamoDB table name
table_name = 'your-dynamodb-table'

Usage
   ```bash
   Run the script:
   python index.py
   ```

Follow the on-screen prompts to perform various operations like inserting, updating, and deleting items in the DynamoDB table.

Connecting to DynamoDB

The connection to DynamoDB is established using the boto3 library. Make sure to install the library and replace the placeholder values in index.py:
   ```bash
   import boto3
   dynamodb = boto3.resource('dynamodb', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name='your-region')
   table = dynamodb.Table(table_name)
   ```

Additional Notes
This project is intended for educational purposes as part of a school assignment.
Feel free to modify and extend the code to meet your specific requirements.
