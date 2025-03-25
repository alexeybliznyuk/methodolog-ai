FROM python:3.13.0-slim



# Устанавливаем зависимости системы и Poetry
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*



COPY backend/pyproject.toml .

COPY backend/poetry.lock .

RUN pip install poetry==2.0.1 
RUN poetry install --no-root 
RUN poetry update 
RUN poetry lock

WORKDIR /app
COPY backend/help-service .

CMD poetry run python main.py || true && tail -f /dev/null
