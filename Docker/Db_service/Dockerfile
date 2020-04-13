FROM python:3.7-alpine
ENV Server_port=8083
ENV Region="local"
ENV Secret_key="anything"
ENV Access_key="anything"
COPY requirements.txt .
COPY db_service.py .
RUN pip install -r requirements.txt
EXPOSE ${Service_port}
CMD python db_service.py
