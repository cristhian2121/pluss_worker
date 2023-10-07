FROM python:3.8-alpine

WORKDIR /worker/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
RUN chmod +x request.sh

# TODO: change it to production configuration
ENV PYTHONUNBUFFERED 1
ENV FLASK_ENV development
ENV FLASK_DEBUG True
ENV FLASK_APP main.py

# Add cron to run request.sh file
RUN echo "30 5 * * * bash /worker/request.sh" >> /etc/crontabs/root

EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]

