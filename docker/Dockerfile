FROM python:3.8

RUN apt-get update && \
    apt-get install -y locales && \
    sed -i -e 's/# es_ES.UTF-8 UTF-8/es_ES.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

RUN mkdir -p ~/amrap-wod-generator
WORKDIR /amrap-wod-generator

COPY amrap-wod-generator.py ./amrap-wod-generator.py
COPY utils.py ./utils.py
COPY AMRAPWOD.py ./AMRAPWOD.py
COPY Exercise.py ./Exercise.py

COPY docker/run_amrap_wod_generator.sh ./run_amrap_wod_generator.sh

COPY exercises.csv ./exercises.csv

CMD [ "sh", "./run_amrap_wod_generator.sh" ]