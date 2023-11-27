
import requests

if __name__ == "__main__":
    url = "http://localhost:3000"
    params = {
        "discipline": "math",
        "grade": "4"
    }

    try:
        response = requests.post(url, data=params)

        if response.status_code == 200:
            print("POST request successful")
        else:
            print(f"POST request failed with status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")
