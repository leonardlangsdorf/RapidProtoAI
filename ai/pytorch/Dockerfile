FROM pytorch/pytorch:1.9.0-cuda10.2-cudnn7-runtime

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "app.py"]
