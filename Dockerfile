FROM python:3.12
WORKDIR fastapi_server/
COPY requirements.txt /fastapi_server/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY ./app ./app
ENV PORT=3000
EXPOSE 3000
CMD [ "fastapi","run","app/main.py","--port" ,"3000"]