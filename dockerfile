FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/


RUN pip install -r requirements.txt


COPY . /usr/src/app/

EXPOSE 8000

CMD [ "python", "setup/manage.py", "runserver", "0.0.0.0:8000" ]

