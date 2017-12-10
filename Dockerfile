FROM python:3.6
MAINTAINER Patrick Hao "haoxiangpeng123@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install --editable .
ENTRYPOINT ["python"]
CMD ["./backend/main.py"]