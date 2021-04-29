FROM python:3.7.6
ENV PYTHONUNBUFFERED 1
WORKDIR /worker/
COPY requirements.txt .
RUN pip install -r requirements.txt
# enviroment for refresh automatic
ENV FLASK_ENV development
ENV FLASK_DEBUG True
ENV FLASK_APP main.py
EXPOSE 5000
COPY . .
CMD ["flask", "run", "-- host=0.0.0.0"]
# CMD [ "uwsgi", "--ini", "main.ini" ]

