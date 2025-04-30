FROM python:3.11
COPY . /app
EXPOSE 5000
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "flasgger_api.py"]