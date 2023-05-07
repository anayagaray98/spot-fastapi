FROM python:3.11.1-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

COPY . .

ADD ./entrypoint.sh /

RUN set -ex \
    && pip install --upgrade pip  \ 
    && pip install -r requirements.txt \
    && pip install psycopg2-binary
    
ENTRYPOINT ["sh", "/entrypoint.sh"]

EXPOSE 80