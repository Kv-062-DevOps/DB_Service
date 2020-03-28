FROM python:3.8.2

ENV region="local"
WORKDIR /app

COPY Init/requirements.txt .
COPY Init/create_table.py .
RUN pip install -r requirements.txt

CMD ["python3", "create_table.py"]