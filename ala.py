import requests
import sys

def get_response(prompt):
    url = "https://gptcall.net/chat"
    headers = {
        "Content-Type": "application/json"
    }
    params = {
        "data": '{"contact":{"id":"7ppofiEl1zkx0Ouu-0nra","flow":true}}'
    }

    try:
        response = requests.post(url, headers=headers, params=params, data={"prompt": prompt})
        response.raise_for_status()

        return response.json()["response"]

    except requests.exceptions.RequestException as e:
        print("Error getting response:")
        print(e)
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python chat.py <prompt>")
        return

    prompt = sys.argv[1]
    response = get_response(prompt)

    if response:
        print("Response:")
        print(response)

if __name__ == "__main__":
    main()