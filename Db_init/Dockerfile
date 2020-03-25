FROM python:3
ENV Region="local"
COPY . .
RUN pip install -r requirements.txt
CMD python CreateTable.py && python LoadData.py


