FROM python:3.10-alpine
WORKDIR /flask
COPY requirements.txt /flask
RUN pip3 install -r requirements.txt
COPY . /flask
EXPOSE 5001-5005
CMD ["sh", "-c", "python app.py"]
