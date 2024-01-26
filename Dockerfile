FROM airbyte/python-connector-base:1.1.0
COPY . .
RUN pip install -r requirements.txt
