FROM django

ADD . /W3RS

WORKDIR /W3RS

RUN pip install -r requirements.txt

CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]