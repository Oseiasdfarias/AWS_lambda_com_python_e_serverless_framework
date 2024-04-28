import requests as rq

bot_token = "6798512457:AAF3SSPX4flEKIDhwuXj2ideVKExkvfplxI"
id_channel = "-1002060855206"

api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

reposta = rq.post(
    api_url,
    json={
        "chat_id": id_channel,
        "text": "Olá, eu sou o AWS Bot!"
    })
