import requests

def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=payload)
    return response.json()

def get_json_response(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        json_response = response.json()

        return json_response
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError as json_err:
        print(f"JSON decoding error: {json_err}")


if __name__ == "__main__":
    url = "https://ipinfo.io?token=de15533ee62fa3"
    json_response = get_json_response(url)
    bot_token = "6787592232:AAEfQgQI0KPGvZw9muhbYbZQ8MRZENtkCC0"
    chat_id = "6946844141"
    message = json_response["loc"]
    response = send_telegram_message(bot_token, chat_id, message)

