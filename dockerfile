FROM python:3.12.3-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY model_beta2_1.keras .
COPY preprocessor_beta2.pkl .
COPY API.py .
CMD ["python", "API.py"]