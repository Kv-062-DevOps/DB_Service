FROM python:3.6-slim

ENV host_port=8080
WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

EXPOSE ${host_port}
CMD ["python3", "dbservice.py"]