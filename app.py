import socket
import time
import json
import requests
from datetime import datetime

# Path to configuration file
CONFIG_PATH = "config.json"

# Log file name
LOG_FILE = "app.log"


def load_config():
    """Load configuration from JSON file"""
    with open(CONFIG_PATH) as f:
        return json.load(f)


def log(message):
    """Log message to console and file with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}"

    # Print to stdout (useful for Docker logs)
    print(line, flush=True)

    # Append to log file
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


def check_host(host):
    """Check host availability via TCP connection (port 53)"""
    try:
        socket.create_connection((host, 53), timeout=3)
        return True
    except OSError:
        return False


def send_telegram(token, chat_id, message):
    """Send alert message to Telegram"""
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    try:
        r = requests.post(url, json={"chat_id": chat_id, "text": message})

        # Log Telegram API response (for debugging)
        log(f"TG RESPONSE: {r.text}")
    except Exception as e:
        log(f"Telegram error: {e}")


def main():
    """Main monitoring loop"""
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
                    log("Sending Telegram alert...")
                    send_telegram(token, chat_id, f"{host} DOWN")

        # Wait before next check cycle
        time.sleep(interval)


if __name__ == "__main__":
    main()
