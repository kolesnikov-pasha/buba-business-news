FROM python:3.7
RUN apt-get update && apt-get -y install cron vim

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x ./start.sh

CMD [ "./start.sh" ]