FROM python:3.8.2

ENV host_port=8083
WORKDIR /app

COPY req.txt .
COPY dbservice.py .
RUN pip install -r req.txt

EXPOSE ${host_port}
CMD ["python3", "dbservice.py"]