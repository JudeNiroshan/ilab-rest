FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y git

WORKDIR /app
COPY . /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN git clone https://github.com/instructlab/taxonomy.git /app/taxonomy

EXPOSE 5000

# Run the application
CMD ["flask", "run"]
