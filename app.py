import socket
import time
import json
import requests
from datetime import datetime

CONFIG_PATH = "config.json"
LOG_FILE = "app.log"


def load_config():
    with open(CONFIG_PATH) as f:
        return json.load(f)


def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}"
    print(line, flush=True)

    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


def check_host(host):
    try:
        socket.create_connection((host, 53), timeout=3)
        return True
    except OSError:
        return False



#def send_telegram(token, chat_id, message):
  #  url = f"https://api.telegram.org/bot{token}/sendMessage"
   # try:
     #   requests.post(url, json={"chat_id": chat_id, "text": message})
   # except Exception as e:
    #    log(f"Telegram error: {e}")
def send_telegram(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    try:
        r = requests.post(url, json={"chat_id": chat_id, "text": message})
        log(f"TG RESPONSE: {r.text}")
    except Exception as e:
        log(f"Telegram error: {e}")

def main():
    config = load_config()
    interval = config["interval"]
    hosts = config["hosts"]

    tg_enabled = config["telegram"]["enabled"]
    token = config["telegram"]["token"]
    chat_id = config["telegram"]["chat_id"]

    while True:
        for host in hosts:
            result = check_host(host)

            if result:
                log(f"[NETMON] {host} OK")
            else:
                log(f"[NETMON] {host} ERROR")

                if tg_enabled:
                    log("TRY SEND TELEGRAM")
                    send_telegram(token, chat_id, f"{host} DOWN")

        time.sleep(interval)


if __name__ == "__main__":
    main()
