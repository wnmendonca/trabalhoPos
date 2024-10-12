FROM python:3.9-slim
WORKDIR /app
COPY /app /app
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install vim -y
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]