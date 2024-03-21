import requests
import hashlib

def download_file(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return None

def calculate_hash(data):
    hash_object = hashlib.sha256()
    hash_object.update(data)
    return hash_object.hexdigest()

def save_file(file_name, file_data):
    with open(file_name, 'wb') as f:
        f.write(file_data)

def save_hash_to_file(hash_file_name, hash_value):
    with open(hash_file_name, 'w') as f:
        f.write(hash_value)

def main():
    url = input("Enter the URL of the file you want to download: ")
    file_data = download_file(url)
    if file_data:
        hash_value = calculate_hash(file_data)
        
        # Save downloaded file
        file_name = url.split('/')[-1]
        save_file(file_name, file_data)
        print(f"Downloaded file '{file_name}' saved successfully!")
        
        # Save hash value
        hash_file_name = file_name.split('.')[0] + "_hash.txt"
        save_hash_to_file(hash_file_name, hash_value)
        print(f"Hash value saved to '{hash_file_name}'")
    else:
        print("Failed to download the file.")

if __name__ == "__main__":
    main()
