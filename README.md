# 🚀 Systemd Network Monitor (Python + Docker + Telegram)

This project demonstrates a network monitoring service written in Python, running as a systemd service, containerized with Docker, and integrated with Telegram alerts.

## 📦 Tech Stack
Python, Docker, Docker Compose, systemd, Telegram Bot API

## ⚙️ Features
- Network availability monitoring (TCP check)
- Runs as a background systemd service
- Dockerized application for portability
- Telegram alerts when host is DOWN
- Configurable hosts and interval via JSON
- Logging to file and systemd journal

## 📁 Project Structure
network-monitor/
├── app.py  
├── config.example.json  
├── Dockerfile  
├── docker-compose.yml  
├── myapp.service  
├── .gitignore  
└── README.md  

## 🚀 Run Locally (Docker)
docker compose up -d

Check logs:
docker compose logs -f

## ⚙️ Run as systemd Service

1. Copy service file:
sudo cp myapp.service /etc/systemd/system/

2. Reload systemd:
sudo systemctl daemon-reexec
sudo systemctl daemon-reload

3. Start service:
sudo systemctl start myapp

4. Enable autostart:
sudo systemctl enable myapp

## 📊 Monitoring Logs
journalctl -u myapp -f

## 📡 Telegram Alerts

The service sends alerts when a host becomes unavailable.

Example:
8.8.8.8 DOWN

Configure in config.json:

{
  "telegram": {
    "enabled": true,
    "token": "YOUR_TOKEN",
    "chat_id": "YOUR_CHAT_ID"
  }
}

## 🔍 How It Works
- The app checks each host via TCP connection
- If connection fails → logs ERROR
- If Telegram enabled → sends alert
- Runs continuously with configurable interval

## ⚠️ Notes
- config.json is not included in repo (use example file)
- Logs are written to app.log
- systemd runs service as background process
- Docker version uses volume for logs persistence

## 🎯 Purpose
This project demonstrates practical DevOps skills:
- systemd service management
- containerization with Docker
- monitoring and alerting
- working with Linux processes and logs
