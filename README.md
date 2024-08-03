# Automated Data Encryption and Decryption in Azure Blob Storage using Python

This repository contains a Python script to automatically encrypt data before storing it in Azure Blob Storage and decrypt it when needed. This ensures data security and privacy.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
  - [Generating a Key](#generating-a-key)
  - [Encrypting Data](#encrypting-data)
  - [Decrypting Data](#decrypting-data)
  - [Uploading Encrypted Data to Azure Blob Storage](#uploading-encrypted-data-to-azure-blob-storage)
  - [Downloading and Decrypting Data from Azure Blob Storage](#downloading-and-decrypting-data-from-azure-blob-storage)
- [License](#license)

## Introduction

This project demonstrates how to secure your data by encrypting it before storing it in Azure Blob Storage and decrypting it when needed. The solution uses the `azure-storage-blob` library to interact with Azure Blob Storage and the `cryptography` library to handle data encryption and decryption.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/encrypt-decrypt-azure-blob.git
    cd encrypt-decrypt-azure-blob
    ```

2. **Create and activate a virtual environment (optional but recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install azure-storage-blob cryptography
    ```

## Usage

### Generating a Key

The encryption key is essential for encrypting and decrypting your data. You can generate a new key using the following script:

```python
from encrypt_decrypt_data import generate_key

key = generate_key()
print(f"Generated Key: {key}")
```

### Encrypting Data

To encrypt your data, use the `encrypt_data` function. This function takes your data and the encryption key as inputs and returns the encrypted data.

```python
from encrypt_decrypt_data import encrypt_data, generate_key

key = generate_key()
data = "Sensitive information"
encrypted_data = encrypt_data(data, key)
print(f"Encrypted Data: {encrypted_data}")
```

### Decrypting Data

To decrypt the previously encrypted data, use the `decrypt_data` function. This function takes the encrypted data and the encryption key as inputs and returns the decrypted data.

```python
from encrypt_decrypt_data import decrypt_data, generate_key

key = generate_key()
encrypted_data = b"<encrypted_data>"  # Replace with your encrypted data
decrypted_data = decrypt_data(encrypted_data, key)
print(f"Decrypted Data: {decrypted_data}")
```

### Uploading Encrypted Data to Azure Blob Storage

You can upload the encrypted data to Azure Blob Storage using the `upload_encrypted_data` function. This function takes the container name, blob name, data, encryption key, and Azure Blob Storage connection string as inputs.

```python
from encrypt_decrypt_data import upload_encrypted_data, generate_key

connection_string = "<your_connection_string>"
key = generate_key()
data = "Sensitive information"

upload_encrypted_data("securecontainer", "encrypted_data", data, key, connection_string)
print("Data uploaded successfully.")
```

### Downloading and Decrypting Data from Azure Blob Storage

To download and decrypt data from Azure Blob Storage, use the `download_decrypted_data` function. This function takes the container name, blob name, decryption key, and Azure Blob Storage connection string as inputs.

```python
from encrypt_decrypt_data import download_decrypted_data, generate_key

connection_string = "<your_connection_string>"
key = generate_key()

decrypted_data = download_decrypted_data("securecontainer", "encrypted_data", key, connection_string)
print(f"Decrypted Data: {decrypted_data}")
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
