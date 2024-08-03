from azure.storage.blob import BlobServiceClient
from cryptography.fernet import Fernet

def generate_key():
    """Generates a new encryption key."""
    return Fernet.generate_key()

def encrypt_data(data, key):
    """Encrypts the given data using the provided key."""
    f = Fernet(key)
    return f.encrypt(data.encode())

def decrypt_data(encrypted_data, key):
    """Decrypts the given encrypted data using the provided key."""
    f = Fernet(key)
    return f.decrypt(encrypted_data).decode()

def upload_encrypted_data(container_name, blob_name, data, key, connection_string):
    """
    Encrypts the data and uploads it to Azure Blob Storage.

    Args:
    - container_name: Name of the Azure Blob Storage container.
    - blob_name: Name of the blob file.
    - data: Data to be encrypted and uploaded.
    - key: Encryption key.
    - connection_string: Azure Blob Storage connection string.
    """
    # Initialize the BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    # Encrypt the data
    encrypted_data = encrypt_data(data, key)
    
    # Upload the encrypted data to the specified blob
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(encrypted_data, overwrite=True)

def download_decrypted_data(container_name, blob_name, key, connection_string):
    """
    Downloads and decrypts data from Azure Blob Storage.

    Args:
    - container_name: Name of the Azure Blob Storage container.
    - blob_name: Name of the blob file.
    - key: Decryption key.
    - connection_string: Azure Blob Storage connection string.
    
    Returns:
    - Decrypted data.
    """
    # Initialize the BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container_name, blob_name)

    # Download the encrypted data from the specified blob
    encrypted_data = blob_client.download_blob().readall()
    
    # Decrypt the data
    return decrypt_data(encrypted_data, key)

if __name__ == "__main__":
    # Define your Azure Blob Storage connection string
    connection_string = "<your_connection_string>"
    
    # Generate a new encryption key
    key = generate_key()
    
    # Define the data to be encrypted and uploaded
    data = "Sensitive information"
    
    # Upload encrypted data to Azure Blob Storage
    upload_encrypted_data("securecontainer", "encrypted_data", data, key, connection_string)
    
    # Download and decrypt data from Azure Blob Storage
    decrypted_data = download_decrypted_data("securecontainer", "encrypted_data", key, connection_string)
    
    # Print the decrypted data to verify
    print(decrypted_data)
