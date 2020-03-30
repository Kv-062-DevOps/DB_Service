FROM python:3.8.2-alpine3.11

ENV host_port=8080
WORKDIR /app

COPY Serve/requirements.txt .
COPY Serve/dbservice.py .
RUN pip install -r requirements.txt

EXPOSE ${host_port}
CMD ["python3", "dbservice.py"]