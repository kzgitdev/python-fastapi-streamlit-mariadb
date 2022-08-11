# python-fastapi-streamlit-mariadb
building containers that FastAPI, streamlit with mutlit pages and mariadb with nginx reverse proxy to access port 80

## description
This FastAPI server consists of four containers
- reverse proxy with nginx to access the port 80 to be forward to 8501 and 8080
- Frontend Streamlit with python to expose 8501 and run streamlit commnad using mulit pages function.
- Backend FastAPI with python to expose 8080 and run uvicorn command
- Database with MariaDB to connect port 3306

![architecture](https://raw.githubusercontent.com/kzgitdev/python-fastapi-streamlit-mariadb/main/architecture.png)

## development environment
OS: Windows 10 Professional 64bit  
Sub OS: WSL2(Windows subsystem on Linux2)  

Docker Desktop: v4.10.1  
Docker version 20.10.17, build 100c701  
Docker Compose version v2.6.1  

## usage
1. **.env**  
.env file is set to use variable of docker-compose.yaml and Dockerfile if you need.
2. nginx configuration

