FROM python:3.8.5-slim

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

# Creating working directory
RUN mkdir /code
WORKDIR /code

# Copying requirements
ADD ./requirements.txt /code/

RUN pip install -r requirements.txt --no-cache-dir 
ADD ./code /code/


# # With GraphicMakgick
# RUN apt-get update && \
#     DEBIAN_FRONTEND=noninteractive apt-get -qq install graphicsmagick -y && apt-get install libmagickwand-dev  -y && pip install -r requirements.txt
# ADD ./code /code/
