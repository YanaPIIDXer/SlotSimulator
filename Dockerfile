FROM python:3.8

WORKDIR /app

ADD ./requirements.txt /app
RUN pip install -r requirements.txt

ADD ./src /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
