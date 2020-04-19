FROM python:3.6-alpine

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV host_port=8080

WORKDIR /app
COPY dbservice.py .
EXPOSE ${host_port}

CMD ["python3", "dbservice.py"]