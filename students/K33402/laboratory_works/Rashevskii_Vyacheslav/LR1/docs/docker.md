# Docker

## LR1-vue/Dockerfile
```dockerfile
FROM node:10-alpine

WORKDIR /LR1-vue
COPY package.json .
RUN npm install
RUN npm i muse-ui -S
RUN npm install --save-dev @babel/preset-env
COPY . /LR1-vue
EXPOSE 8080
CMD ['npm', 'start']
```

## Dockerfile
```dockerfile
FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY req.txt /code/
RUN pip install -r req.txt

COPY manage.py /code/
COPY LR1 /code/LR1
COPY db.sqlite3 /code/
COPY LR1_secondApp /code/LR1_secondApp

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
```

## docker-compose.yml
```yaml
version: '3'

services:
  server:
    build: 
      context: .
      dockerfile: ./Dockerfile
    command: python manage.py runserver 0.0.0.0:8000
    ports:
      - 8000:8000

  web:
    build:
      context: ./LR1-vue/
      dockerfile: ./Dockerfile
    command: npm run dev
    network_mode: host
    ports:
      - 8080:8080
    depends_on: 
      - server
```