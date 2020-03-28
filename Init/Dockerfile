FROM python:3.8.2

ENV host_port=8080
ENV region="local"
WORKDIR /app

COPY requirements.txt .
COPY CreateTable.py .
RUN pip install -r requirements.txt

EXPOSE ${host_port}
CMD ["python3", "CreateTable.py"]