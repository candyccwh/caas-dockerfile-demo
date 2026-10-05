FROM python:3.12-alpine

WORKDIR /app
COPY app.py .

ENV PORT=8080
EXPOSE 8080

# 0.0.0.0 binding is mandatory on the CaaS platform — the gateway cannot
# reach containers that listen on 127.0.0.1.
CMD ["python", "app.py"]
