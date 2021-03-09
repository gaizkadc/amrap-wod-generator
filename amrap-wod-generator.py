import utils
import img_utils
import twitter_utils
import sys

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
img_path = img_utils.create_wod_image(power_amrap_wod, endurance_amrap_wod, logger)

if len(sys.argv) > 1 and sys.argv[1] == '--tweet':
    # tweet the wod with its image
    twitter_utils.tweet_wod(img_path, logger)
else:
    # open the wod img
    utils.open_wod_img(logger, img_path)
