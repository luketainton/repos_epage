import os

import requests


def send_page(name: str, email: str, message: str) -> tuple:
    """POST to the Pushover API."""
    api_url = "https://api.pushover.net/1/messages.json"
    api_token = os.getenv("PUSHOVER_API_TOKEN")
    user_key = os.getenv("PUSHOVER_USER_KEY")

    full_msg = f"Name: {name}\nEmail: {email}\n\nMessage: {message}"

    payload = {
        "token": api_token,
        "user": user_key,
        "title": f"ePage from {name}",
        "message": full_msg,
        "priority": "1",
        "sound": "cosmic",
    }

    req = requests.post(
        api_url, json=payload, headers={"Content-Type": "application/json"}, timeout=5
    )

    if req.status_code == 200 and req.json().get("status") == 1:
        return (True, None)
    return (False, req.json())
