FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir azure-identity azure-mgmt-compute azure-mgmt-resource pydantic python-dotenv

COPY . .

ENTRYPOINT ["python", "src/main.py"]