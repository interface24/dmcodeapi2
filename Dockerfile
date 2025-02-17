FROM python:3.12-slim als Basis-Image

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir flask pystrich pillow gunicorn

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]