import json
import requests
import hashlib
import hmac
import csv
from dotenv import load_dotenv
import os

load_dotenv()

# Secret key obtained from the user's account
api_secret = os.getenv('SECRET_TOKEN')
api_public = os.getenv('PUBLIC_TOKEN')


url = "https://app.cryptoprocessing.com/api/v2/withdrawal/crypto"

# Open the CSV file
with open('data.csv', 'r') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)
    
    # Skip the header row if it exists
    next(csv_reader, None)
    
    # Iterate over the rows
    for row in csv_reader:
        # Extract values from the row
        amount = row[0]
        currency = row[1]
        foreign_id = row[2]
        address = row[3]
        
        # Request body in JSON format
        request_body = json.dumps(
            {
                "amount": amount,
                "currency": currency,
                "foreign_id": foreign_id,
                "address": address
            }
        )

        # Generate the signature using HMAC-SHA512
        signature = hmac.new(api_secret.encode(), msg=request_body.encode(), digestmod=hashlib.sha512).hexdigest()

        # Set the headers
        headers = {
            'Content-Type': 'application/json',
            'X-Processing-Key': api_public,
            'X-Processing-Signature': signature
        }

        # Make the POST request
        response = requests.post(url, headers=headers, data=request_body)

        # Check for errors
        if response.status_code != 200:
            print(f"Result: {response.status_code} - {response.text}")
        else:
            # Parse the response
            data = response.json()
