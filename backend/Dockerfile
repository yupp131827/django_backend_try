FROM python:3.11
ENV PYTHONUNBUFFERED 1

RUN mkdir /code

RUN apt-get update && apt-get -y install vim
RUN pip install --upgrade pip

WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

ARG UID=1000
ARG GID=1000
RUN groupadd -g ${GID} docker
RUN useradd -u ${UID} -g ${GID} -s /bin/bash -m docker
USER ${UID}



