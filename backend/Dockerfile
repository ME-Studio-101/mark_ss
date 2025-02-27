FROM python:3.9-slim

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install --upgrade pip && \
    pip install -r requirements.txt --no-cache-dir

COPY ../backend/ ./

RUN python manage.py collectstatic --no-input

CMD ["sh", "-c", "python manage.py migrate && gunicorn --bind 0.0.0.0:8000 config.wsgi:application"]