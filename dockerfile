FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY ScriptPDF.py .
COPY VerifyPDF.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["bash", "-c", "python ScriptPDF.py && python VerifyPDF.py test.pdf"]