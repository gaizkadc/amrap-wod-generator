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

    log_file_path = logs_folder_path + '/' + app_name + '.log'

    logger = logging.getLogger(app_name)
    logger.setLevel('DEBUG')

    log_format = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    file_handler = RotatingFileHandler(log_file_path, maxBytes=(1048576 * 5), backupCount=5)
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    return logger


def parse_exercises(file_name, logger):
    exercises = []

    try:
        exercises_file = open(file_name, 'r')
        exercises_data = csv.reader(exercises_file)
        for item in exercises_data:
            exercise = Exercise(desc=item[0], type=item[1], logger=logger)
            exercises.append(exercise)
    except:
        print('something went wrong')

    return exercises


def get_exercises_by_type(exercises):
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

    return hard_exercises, medium_exercises, easy_exercises, ccm_exercises


def get_power_amrap_wod(hard_exercises, medium_exercises):
    first_exercise = random.choice(hard_exercises)
    second_exercise = random.choice(medium_exercises)
    medium_exercises.remove(second_exercise)
    third_exercise = random.choice(medium_exercises)

    return AMRAPWOD(first_exercise, second_exercise, third_exercise)


def get_endurance_amrap_wod(medium_exercises, easy_exercises, ccm_exercises):
    first_exercise = random.choice(medium_exercises)
    second_exercise = random.choice(easy_exercises)
    third_exercise = random.choice(ccm_exercises)

    return AMRAPWOD(first_exercise, second_exercise, third_exercise)