FROM python:3.7

ADD . /W3RS

WORKDIR /W3RS

RUN pip install -r requirements.txt

CMD [ "python", "manage.py", "runsslserver", "0.0.0.0:443" ]

EXPOSE 443/tcp

MAINTAINER Avinash tashan.avi@gmail.com
