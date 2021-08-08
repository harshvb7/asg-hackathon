FROM python:3.7.7-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev bash libxslt-dev \
    # Pillow dependencies
    && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

RUN pip3 install pip
RUN pip3 install pipenv

RUN mkdir /code

WORKDIR /code/

COPY Pipfile /code/Pipfile

COPY Pipfile.lock /code/Pipfile.lock

RUN pipenv install --system --dev

COPY . /code/

EXPOSE 8000