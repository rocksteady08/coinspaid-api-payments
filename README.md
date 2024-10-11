# Crypto Withdrawal Automation Script for Coinspaid

This Python script automates the process of making cryptocurrency withdrawals using the [CryptoProcessing API](https://docs.coinspaid.com/docs/api-documentation). It reads transaction details from a CSV file and sends requests to the API for each withdrawal, utilizing HMAC-SHA512 encryption for secure communication.

# Features

- **Automated Crypto Withdrawals:** Reads multiple withdrawal requests from a CSV file and processes them using the CryptoProcessing API.
- **Secure Requests:** Uses HMAC-SHA512 to sign the request for added security.
- **Error Handling:** Prints error messages for failed transactions.

# Prerequisites
Before running this script, you need to have:
- **Python 3.6+** installed on your system.
- An account with the [CryptoProcessing API](https://app.cryptoprocessing.com/).
- API `SECRET_TOKEN` and `PUBLIC_TOKEN` from your Coinspaid account.

# Installation
1. **Clone the repository or code from main.py**
2. **Install dependencies**: Use `pip` to install the required Python packages:`pip install -r requirements.txt`

# Environment Setup
1. Create a `.env` file in the root directory of your project and add your API tokens as follows:
`SECRET_TOKEN=your_api_secret_key`
`PUBLIC_TOKEN=your_api_public_key`
3. Replace `your_api_secret_key` and `your_api_public_key` with the appropriate values from your Coinspaid account.

# CSV File Format
The script expects a CSV file named `data.csv` in the following format:
| amount | currency | foreign_id | address         |
| ------ | -------- | ---------- | --------------- |
| 0.5    | BTC      | 12345      | 1A2b3C4d5E6f... |
| 2.0    | ETH      | 67890      | 0xAbCDef123...  |

- **amount**: The amount of cryptocurrency to withdraw.
- **currency**: The type of cryptocurrency (e.g., BTC, ETH).
- **foreign_id**: A unique identifier for the transaction.
- **address**: The recipient's cryptocurrency address.

# Usage
1. Ensure your `data.csv` file is in the same directory as the script.
2. Run the script using: `python crypto_withdrawal_script.py`
3. The script will read each row from the CSV file and process the withdrawals one by one, displaying the status of each transaction.

# Error Handling
- If a transaction fails, the script will print the error code and message to the console.
- Common error messages include invalid addresses, insufficient funds, or incorrect API credentials.

# Dependencies
This script requires the following Python packages:
- `requests`
- `python-dotenv`
You can install all dependencies using the requirements.txt file with:
`pip install -r requirements.txt`
