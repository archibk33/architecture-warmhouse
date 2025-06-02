FROM python:3.10-slim

WORKDIR /app

COPY app_temp_api.py .

RUN pip install flask

EXPOSE 8081

CMD ["python", "app_temp_api.py"]