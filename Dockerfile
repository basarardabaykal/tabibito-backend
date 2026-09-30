FROM python:3.13-slim-bookworm

# Ensures logs are sent directly to terminal without buffering
ENV PYTHONUNBUFFERED=1
# Prevents Python from writing temporary .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Sets the virtual directory
WORKDIR /tabibito-backend

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]