FROM python:3.12.8
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /app
COPY ingest_data.py ingest_data.py
ENTRYPOINT [ "python3", "ingest_data.py" ]
