FROM python:3.7

WORKDIR /python-flask-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./flask-app ./flask-app

CMD ["python3", "./flask_app/app.py"]
