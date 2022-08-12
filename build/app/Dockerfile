# backend fastapi
FROM python:latest

# コンテナイメージ内において、作業用ディレクトリ(/app)を作成
WORKDIR /app/sql_app

# 「PythonのFastAPIでREST API(GET)を実現する」プログラムを/appへコピー
COPY requirements.txt /app/sql_app/requirements.txt
# COPY main.py /app/main.py

RUN apt-get -y install libmariadb3 libmariadb-dev gcc

# コンテナイメージ内で必要なパッケージをインストール
RUN  pip install --upgrade pip && pip install --no-cache-dir --upgrade -r /app/sql_app/requirements.txt

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080" , "--reload"]

