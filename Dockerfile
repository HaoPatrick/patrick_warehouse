FROM python:3.6
MAINTAINER Patrick Hao "haoxiangpeng123@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install --editable .
WORKDIR /app/backend
ENTRYPOINT ["gunicorn"]
CMD ["-w", "1","-b","0.0.0.0:5000","main:app"]