FROM python:3.6-alpine as base

FROM base as builder
WORKDIR /install
COPY requirements.txt .
RUN pip install --install-option="--prefix=/install" -r requirements.txt

FROM base
ENV host_port=8080
COPY --from=builder /install /usr/local
WORKDIR /app
COPY dbservice.py .
EXPOSE ${host_port}

CMD ["python3", "dbservice.py"]