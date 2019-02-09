FROM python:3.6
RUN mkdir /app
COPY app/ /app
WORKDIR /app
ENV DB_USER="ramishasyanov" \
    DB_HOST_IP="hroracle.cltawllhafit.eu-central-1.rds.amazonaws.com" \
    DB_PORT="5432" \
    DB_PASSWORD="Aws0111211" 
RUN pip install -r requirements.txt
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
