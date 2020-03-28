FROM python:3.8.2

ENV host_port=8080
WORKDIR /app

COPY requirements.txt .
COPY dbservice.py .
RUN pip install -r requirements.txt

EXPOSE ${host_port}
CMD ["python3", "dbservice.py"]