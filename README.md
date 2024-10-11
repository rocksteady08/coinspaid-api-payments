#Crypto Withdrawal Automation Script for Coinspaid

This Python script automates the process of making cryptocurrency withdrawals using the [CryptoProcessing API](https://docs.coinspaid.com/docs/api-documentation). It reads transaction details from a CSV file and sends requests to the API for each withdrawal, utilizing HMAC-SHA512 encryption for secure communication.

**Features**

- **Automated Crypto Withdrawals:** Reads multiple withdrawal requests from a CSV file and processes them using the CryptoProcessing API.
- **Secure Requests:** Uses HMAC-SHA512 to sign the request for added security.
- **Error Handling:** Prints error messages for failed transactions.

