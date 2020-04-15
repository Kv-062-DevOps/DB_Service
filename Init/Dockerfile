FROM python:3.6-alpine as base

FROM base as builder
WORKDIR /install
COPY requirements.txt .
RUN pip install --install-option="--prefix=/install" -r requirements.txt

FROM base
COPY --from=builder /install /usr/local
WORKDIR /app
COPY create_table.py .

CMD ["python3", "create_table.py"]