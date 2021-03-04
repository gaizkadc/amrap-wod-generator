import utils


logger = utils.get_logger()
logger.info('amrap-wod-generator started')

exercises_file_name = 'exercises.csv'
exercises = utils.parse_exercises(exercises_file_name, logger)

hard_exercises, medium_exercises, easy_exercises, ccm_exercises = utils.get_exercises_by_type(exercises)

power_amrap_wod = utils.get_power_amrap_wod(hard_exercises, medium_exercises)
endurance_amrap_wod = utils.get_endurance_amrap_wod(medium_exercises, easy_exercises, ccm_exercises)

print('Power AMRAP WOD')
power_amrap_wod.print()

print('Endurance AMRAP WOD')
endurance_amrap_wod.print()
