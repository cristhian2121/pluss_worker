FROM python:3.7.6
ENV PYTHONUNBUFFERED 1
MAINTAINER KameHouse
WORKDIR /worker/
COPY requirements.txt .
RUN pip install -r requirements.txt
# enviroment for refresh automatic
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True
ENV FLASK_APP main.py
RUN ls
COPY . .
EXPOSE 5000
# ENTRYPOINT [ "python" ]
# CMD ["main.py"]
CMD flask run --host=0.0.0.0
