FROM python:3.11-slim

WORKDIR /app
COPY src_1/ src_1/
COPY main.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python","main.py" ]
CMD [ "sample_data/access.log" ]


