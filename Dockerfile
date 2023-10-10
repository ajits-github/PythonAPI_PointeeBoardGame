FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Run tests during the build
RUN python -m unittest discover tests

CMD ["python", "run.py"]
