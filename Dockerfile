FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .



RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000
CMD [ "python" , "maange.py" , "runserver" , "0.0.0.0:8000" ]