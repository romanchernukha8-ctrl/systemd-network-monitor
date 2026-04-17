# Базовый образ
FROM python:3.12-slim

# Рабочая директория
WORKDIR /app

# Копируем файлы
COPY app.py .
COPY config.json .

# Устанавливаем tzdata (system)
RUN apt-get update && apt-get install -y tzdata && rm -rf /var/lib/apt/lists/*

# Устанавливаем зависимости
RUN pip install --no-cache-dir requests

# Запуск
CMD ["python", "app.py"]
