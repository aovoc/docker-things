FROM ubuntu:16.04
MAINTAINER centrifugal4@gmail.com

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential python3-dev python3-pip python3-setuptools \
    && rm -rf /var/lib/apt/lists/*

COPY ./service /service

# Ref: http://flask.pocoo.org/docs/1.0/quickstart/
ENV FLASK_APP /service/app.py

#RuntimeError: Click will abort further execution because Python 3 was configured to use ASCII as encoding for the environment.  Consult http://click.pocoo.org/python3/for mitigation steps.
#
#This system supports the C.UTF-8 locale which is recommended.
#You might be able to resolve your issue by exporting the
#following environment variables:
#
#    export LC_ALL=C.UTF-8
#    export LANG=C.UTF-8
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

EXPOSE 5000

WORKDIR /service
RUN pip3 install -r /service/requirements.txt

CMD python3 -m flask run --host=0.0.0.0
