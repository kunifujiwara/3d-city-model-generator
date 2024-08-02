import requests

def download_file(url, filename):
    """Download a file from a URL and save it locally."""
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully and saved as {filename}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")