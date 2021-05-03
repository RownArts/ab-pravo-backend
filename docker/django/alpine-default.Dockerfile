# FROM taime/django-max
FROM python:3.7-alpine

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Creating working directory
RUN mkdir -p /code
WORKDIR /code

# Copying requirements
COPY ./requirements.txt /code/
# ADD ./gunicorn.py /gunicorn_conf.py
ADD ./docker/django-gunicorn-meinheld/gunicorn_conf.py /gunicorn_conf.py


RUN apk update \
    && apk add --virtual .build-deps gcc python3-dev musl-dev \
    && apk add ca-certificates linux-headers \
    postgresql-libs postgresql-dev postgresql-client \
    # Pillow dependencies
    jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
    # Dev dependencies
    curl bash \
    # CFFI dependencies
    libffi-dev py-cffi \
    # Translations dependencies
    gettext \
    # Pip installations
    && pip install --upgrade pip \
    && pip install pipenv \
    && pip install meinheld gunicorn \
    && pip install uwsgi \
    && pip install -r requirements.txt  --no-cache-dir \
    && apk del .build-deps gcc libc-dev 


# RUN pip install --upgrade pip \
# && pip install -r requirements.txt

# RUN apk del --purge .build-deps gcc libc-dev 




# RUN apk add --no-cache --virtual .build-deps \
#     ca-certificates gcc postgresql-dev linux-headers musl-dev \
#     libffi-dev jpeg-dev zlib-dev bash
