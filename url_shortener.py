import requests
import urllib.parse

def shorten_url(long_url, access_token):
    
    if not long_url.startswith('http://') and not long_url.startswith('https://'):
        long_url = 'https://' + long_url
    api_url = "https://api-ssl.bitly.com/v4/shorter"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    encoded_url = urllib.parse.quote(long_url, safe='')
    payload = {
        "long_url": long_url
    }
    try:
        response = requests.post(api_url, headers=headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            short_url = data["link"]
            return short_url
        else:
            print(f"Failed to shorten URL. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
def main():
    long_url = input("Enter the long URL: ")
    access_token = "8cf1525ecbc098261868c958141f5588aeb89235"
    short_url = shorten_url(long_url, access_token)
    if short_url:
        print(f"Shortened URL: {short_url}")
    else:
        print("Failed to shorten URL. Please try again later.")
if __name__ == "__main__":
    main()