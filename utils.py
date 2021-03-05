from Exercise import Exercise
from AMRAPWOD import AMRAPWOD

import tweepy
import requests

import csv
import os
import random
import datetime
import locale

import logging
from logging.handlers import RotatingFileHandler
import sys


def get_logger():
    logs_folder_path = os.getenv('LOGS_FOLDER_PATH')
    app_name = os.getenv('APP_NAME')

    if not os.path.isdir(logs_folder_path):
        os.mkdir(logs_folder_path)
    log_file_path = logs_folder_path + '/' + app_name + '.log'
    if not os.path.isfile(log_file_path):
        log_file = open(log_file_path, "a")
        log_file.close()

    logger = logging.getLogger(app_name)
    logger.setLevel('DEBUG')

    log_format = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    file_handler = RotatingFileHandler(log_file_path, maxBytes=(1048576 * 5), backupCount=5)
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    logger.info('logger created')

    return logger


def parse_exercises(file_name, logger):
    logger.info('parsing exercises from {}'.format(file_name))

    exercises = []

    try:
        exercises_file = open(file_name, 'r')
        exercises_data = csv.reader(exercises_file)
        for item in exercises_data:
            exercise = Exercise(desc=item[0], type=item[1], logger=logger)
            exercises.append(exercise)
    except:
        logger.error('something went wrong')

    logger.info('exercises parsed')

    return exercises


def get_exercises_by_type(exercises, logger):
    logger.info('getting exercises by type')

    hard_exercises = []
    medium_exercises = []
    easy_exercises = []
    ccm_exercises = []

    for exercise in exercises:
        if exercise.type == 'Hard':
            hard_exercises.append(exercise)
        elif exercise.type == 'Medium':
            medium_exercises.append(exercise)
        elif exercise.type == 'Easy':
            easy_exercises.append(exercise)
        else:
            ccm_exercises.append(exercise)

    logger.info('exercises retrieved by type')

    return hard_exercises, medium_exercises, easy_exercises, ccm_exercises


def get_power_amrap_wod(hard_exercises, medium_exercises, logger):
    logger.info('getting power amrap wod')

    first_exercise = random.choice(hard_exercises)
    second_exercise = random.choice(medium_exercises)
    medium_exercises.remove(second_exercise)
    third_exercise = random.choice(medium_exercises)

    logger.info('power amrap wod retrieved')

    return AMRAPWOD(first_exercise, second_exercise, third_exercise)


def get_endurance_amrap_wod(medium_exercises, easy_exercises, ccm_exercises, logger):
    logger.info('getting endurance amrap wod')

    first_exercise = random.choice(medium_exercises)
    second_exercise = random.choice(easy_exercises)
    third_exercise = random.choice(ccm_exercises)

    logger.info('endurance amrap wod retrieved')

    return AMRAPWOD(first_exercise, second_exercise, third_exercise)


def create_postkit_request_body(power_amrap_wod, endurance_amrap_wod, logger):
    logger.info('creating postkit request body')

    postkit_template_id = os.getenv('POSTKIT_TEMPLATE_ID')
    postkit_token = os.getenv('POSTKIT_TOKEN')
    img_size = os.getenv('IMG_SIZE')

    today = datetime.datetime.now()

    request_body = {
        "id": postkit_template_id,
        "token": postkit_token,
        "size": img_size,
        "params": {
            "title": {"content": "WOD " + today.strftime('%Y%m%d')},
            "powerwodcontent1": {"content": "* " + power_amrap_wod.first_exercise.print()},
            "powerwodcontent2": {"content": "* " + power_amrap_wod.second_exercise.print()},
            "powerwodcontent3": {"content": "* " + power_amrap_wod.third_exercise.print()},
            "endurancewodcontent1": {"content": "* " + endurance_amrap_wod.first_exercise.print()},
            "endurancewodcontent2": {"content": "* " + endurance_amrap_wod.second_exercise.print()},
            "endurancewodcontent3": {"content": "* " + endurance_amrap_wod.third_exercise.print()}
        }
    }

    logger.info('postkit request body created')

    return request_body


def create_wod_image(power_amrap_wod, endurance_amrap_wod, logger):
    logger.info('creating wod image')

    postkit_request_body = create_postkit_request_body(power_amrap_wod, endurance_amrap_wod, logger)
    postkit_endpoint = os.getenv('POSTKIT_ENDPOINT')

    resulting_image = requests.post(url=postkit_endpoint, json=postkit_request_body)
    today = datetime.datetime.now()

    resulting_image_folder_path = os.getenv('IMGS_FOLDER')
    resulting_image_path = resulting_image_folder_path + '/WOD' + today.strftime('%Y%m%d') + '.png'

    if not os.path.isdir(resulting_image_folder_path):
        os.mkdir(resulting_image_folder_path)
    if not os.path.isfile(resulting_image_path):
        log_file = open(resulting_image_path, "a")
        log_file.close()

    resulting_image_file = open(resulting_image_path, "wb")
    resulting_image_file.write(resulting_image.content)
    resulting_image_file.close()

    logger.info('wod image created')

    return resulting_image_path


def get_twitter_credentials(logger):
    logger.info('getting twitter credentials')

    consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
    consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
    access_token = os.getenv('TWITTER_ACCESS_TOKEN')
    access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

    credentials = {
        'consumer_key': consumer_key,
        'consumer_secret': consumer_secret,
        'access_token': access_token,
        'access_token_secret': access_token_secret
    }

    logger.info('twitter credentials retrieved')

    return credentials


def twitter_login(credentials, logger):
    logger.info('logging in twitter')

    auth = tweepy.OAuthHandler(credentials['consumer_key'], credentials['consumer_secret'])
    auth.set_access_token(credentials['access_token'], credentials['access_token_secret'])
    api = tweepy.API(auth, wait_on_rate_limit=True)

    logger.info('logged in twitter')

    return api


def tweet_wod(image_path, logger):
    logger.info('tweeting wod')

    twitter_credentials = get_twitter_credentials(logger)
    twitter_api = twitter_login(twitter_credentials, logger)

    today = datetime.datetime.now()
    # locale.setlocale(locale.LC_TIME, 'es_ES')
    locale.setlocale(locale.LC_ALL,'es_ES.UTF-8')
    today_in_spanish = today.strftime('%A, %d de %B de %Y')

    adornment_list = ['jodido', 'puto']
    hashtags = '\n#crossfit #wod'

    tweet_text = 'Mi ' + random.choice(adornment_list) + ' WOD de hoy ' + today_in_spanish + '.' + hashtags

    twitter_api.update_with_media(image_path, status=tweet_text)

    logger.info('wod tweeted')
