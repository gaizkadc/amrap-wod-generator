import utils
import img_utils
import twitter_utils

# create a logger
logger = utils.get_logger()
logger.info('amrap-wod-generator started')

# parse exercises from included file exercises.csv
exercises_file_name = 'exercises.csv'
exercises = utils.parse_exercises(exercises_file_name, logger)

# get exercises by type
hard_exercises, medium_exercises, easy_exercises, ccm_exercises = utils.get_exercises_by_type(exercises, logger)

# create a power amrap wod and an endurance amrap wod
power_amrap_wod = utils.get_power_amrap_wod(hard_exercises, medium_exercises, logger)
endurance_amrap_wod = utils.get_endurance_amrap_wod(medium_exercises, easy_exercises, ccm_exercises, logger)

# create amrao wod image
image_path = img_utils.create_wod_image(power_amrap_wod, endurance_amrap_wod, logger)

# tweet the wod with its image
twitter_utils.tweet_wod(image_path, logger)
