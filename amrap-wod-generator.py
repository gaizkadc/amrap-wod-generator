import utils

logger = utils.get_logger()
logger.info('amrap-wod-generator started')

exercises_file_name = 'exercises.csv'
exercises = utils.parse_exercises(exercises_file_name, logger)

hard_exercises, medium_exercises, easy_exercises, ccm_exercises = utils.get_exercises_by_type(exercises, logger)

power_amrap_wod = utils.get_power_amrap_wod(hard_exercises, medium_exercises, logger)
endurance_amrap_wod = utils.get_endurance_amrap_wod(medium_exercises, easy_exercises, ccm_exercises, logger)

image_path = utils.create_wod_image(power_amrap_wod, endurance_amrap_wod, logger)

utils.tweet_wod(image_path, logger)
