from Exercise import Exercise
from AMRAPWOD import AMRAPWOD

import csv
import os
import random

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
