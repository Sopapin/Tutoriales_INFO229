FROM python:3.6.3

ENV SLACK_TOKEN=""
ENV SLACK_SIGNING_SECRET=""

COPY ./requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /nestor_slack_reader_2

COPY ./nestor_slack_reader_2.py /nestor_slack_reader_2.py

CMD [ "python", "/nestor_slack_reader_2.py" ]
