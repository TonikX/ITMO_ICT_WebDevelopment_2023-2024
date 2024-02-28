
import requests

if __name__ == "__main__":
    url = "http://localhost:3000"
   
    try:
        response = requests.get(url)

        if response.status_code == 200:
            print(response.text)
        else:
            print(f"POST request failed with status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")
