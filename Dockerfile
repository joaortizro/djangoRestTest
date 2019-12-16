FROM python:3

RUN mkdir /app
WORKDIR /app

ADD . /app/

# enviorement variables
ENV PYTHONUNBUFFERED 1
#ENV PORT=8000

#enviorement dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# bug in gunicorn 20.0.0
#RUN apk add binutils libc-dev

CMD gunicorn --bind 0.0.0.0:$PORT api.wsgi 