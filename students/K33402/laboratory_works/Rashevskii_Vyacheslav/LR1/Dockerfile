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

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]