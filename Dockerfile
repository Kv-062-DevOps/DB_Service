FROM python:3
ENV Service_port=8083
COPY requirements.txt .
COPY db_service.py .
RUN pip install -r requirements.txt
EXPOSE ${Service_port}
CMD python db_service.py
