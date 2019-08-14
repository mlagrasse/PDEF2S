FROM python:3.7

ADD . /PDEF2S

WORKDIR /PDEF2S

RUN pip install -r requirements.txt

CMD [ "python", "manage.py", "runsslserver", "0.0.0.0:443" ]

EXPOSE 443/tcp
