FROM python:3.12

WORKDIR /app

ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip install -r requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000
CMD [ "python" , "maange.py" , "runserver" , "0.0.0.0:8000" ]