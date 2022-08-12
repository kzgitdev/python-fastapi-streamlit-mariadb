# frontent/Dockerfile
FROM python:3.9

WORKDIR /app
COPY requirements.txt /app/requirements.txt
# COPY . /app
RUN pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT [ "streamlit", "run", "front.py" ]
