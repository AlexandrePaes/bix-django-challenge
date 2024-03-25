FROM python:3.8-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /appbix

COPY ./requirements.txt /requirements.txt

# Set the working directory in the container
WORKDIR /appbix

# Copy .env file to container
# COPY .env /app/.env
COPY .env /appbix/.env

# Make port 8000 available to the world outside this container
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
      build-base postgresql-dev musl-dev libffi-dev && \
    /py/bin/pip install -r /requirements.txt && \
    apk add zlib-dev jpeg-dev gcc musl-dev && \
    #/py/bin/pip install Pillow && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home hotel

ENV PATH="/py/bin:$PATH"

# Run the web server on port $PORT
CMD gunicorn hotel.wsgi --bind 0.0.0.0:$PORT
