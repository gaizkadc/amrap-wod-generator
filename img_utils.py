import datetime
import os
import random

from PIL import Image, ImageFont, ImageDraw, ImageEnhance


def create_wod_image(power_amrap_wod, endurance_amrap_wod, logger):
    logger.info('creating wod image')

    today = datetime.datetime.now()

    try:
        logger.info('retrieving imgs folder path from settings')
        import settings
        image_folder_path = settings.IMGS_FOLDER
    except ModuleNotFoundError as error:
        logger.info('unable to import settings')
        logger.info(error)
        image_folder_path = os.getenv('IMGS_FOLDER')

    if not os.path.exists(image_folder_path):
        os.makedirs(image_folder_path)

    resulting_img_path = image_folder_path + '/WOD' + today.strftime('%Y%m%d') + '.png'

    background_folder_path = 'backgrounds'
    background_path = get_background(background_folder_path)

    darken_img(background_path, resulting_img_path)

    text_color = (255, 255, 255)
    title_height = 230
    write_title(today, resulting_img_path, text_color, title_height)
    write_warmup(resulting_img_path, text_color, title_height + 170)
    write_power_amrap_wod(power_amrap_wod, resulting_img_path, text_color, title_height + 370)
    write_endurance_amrap_wod(endurance_amrap_wod, resulting_img_path, text_color, title_height + 620)

    logger.info('wod image created')

    return resulting_img_path


def get_background(background_folder_path):
    backgrounds = [bg for bg in os.listdir(background_folder_path) if bg.endswith(".png")]
    return 'backgrounds/' + random.choice(backgrounds)


def darken_img(img_path, dark_img_path):
    background_img = Image.open(img_path)
    enhancer = ImageEnhance.Brightness(background_img)
    darker_background_img = enhancer.enhance(0.4)
    darker_background_img.save(dark_img_path)


def write_title(today, img_path, text_color, height):
    title_font = ImageFont.truetype('fonts/Montserrat-Bold.ttf', 45)
    title_text_position = (100, height)
    title_text = 'WOD ' + today.strftime('%Y%m%d')

    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)
    draw.text(title_text_position, title_text, text_color, font=title_font)
    draw.line((100, height - 10, img.width, height - 10), width=6)
    draw.line((100, height + 64, img.width, height + 64), width=6)

    img.save(img_path)


def write_warmup(img_path, text_color, height):
    title_font = ImageFont.truetype('fonts/Montserrat-Medium.ttf', 30)
    body_font = ImageFont.truetype('fonts/Montserrat-Regular.ttf', 30)

    title_text_position = (350, height)
    title_text = 'Warmup: 15 min'

    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)
    draw.text(title_text_position, title_text, text_color, font=title_font)
    draw.line((0, height + 40, 600, height + 40), width=3)

    warmup_1_text = '* 2 min Warmup'
    warmup_1_text_position = (100, height + 60)
    draw.text(warmup_1_text_position, warmup_1_text, text_color, font=body_font)

    warmup_2_text = '* 12 min HIIT'
    warmup_2_text_position = (100, height + 110)
    draw.text(warmup_2_text_position, warmup_2_text, text_color, font=body_font)

    img.save(img_path)

def write_power_amrap_wod(power_amrap_wod, img_path, text_color, height):
    title_font = ImageFont.truetype('fonts/Montserrat-Medium.ttf', 30)
    body_font = ImageFont.truetype('fonts/Montserrat-Regular.ttf', 30)

    title_text_position = (263, height)
    title_text = 'Power AMRAP: 12 min'

    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)
    draw.text(title_text_position, title_text, text_color, font=title_font)
    draw.line((0, height + 40, 600, height + 40), width=3)

    pwer_1_text = '* ' + power_amrap_wod.first_exercise.print()
    power_1_text_position = (100, height + 60)
    draw.text(power_1_text_position, pwer_1_text, text_color, font=body_font)

    power_2_text = '* ' + power_amrap_wod.second_exercise.print()
    power_2_text_position = (100, height + 110)
    draw.text(power_2_text_position, power_2_text, text_color, font=body_font)

    power_3_text = '* ' + power_amrap_wod.third_exercise.print()
    power_3_text_position = (100, height + 160)
    draw.text(power_3_text_position, power_3_text, text_color, font=body_font)

    img.save(img_path)


def write_endurance_amrap_wod(endurance_amrap_wod, img_path, text_color, height):
    title_font = ImageFont.truetype('fonts/Montserrat-Medium.ttf', 30)
    body_font = ImageFont.truetype('fonts/Montserrat-Regular.ttf', 30)

    title_text_position = (193, height)
    title_text = 'Endurance AMRAP: 15 min'

    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)
    draw.text(title_text_position, title_text, text_color, font=title_font)
    draw.line((0, height + 40, 600, height + 40), width=3)

    pwer_1_text = '* ' + endurance_amrap_wod.first_exercise.print()
    power_1_text_position = (100, height + 60)
    draw.text(power_1_text_position, pwer_1_text, text_color, font=body_font)

    power_2_text = '* ' + endurance_amrap_wod.second_exercise.print()
    power_2_text_position = (100, height + 110)
    draw.text(power_2_text_position, power_2_text, text_color, font=body_font)

    power_3_text = '* ' + endurance_amrap_wod.third_exercise.print()
    power_3_text_position = (100, height + 160)
    draw.text(power_3_text_position, power_3_text, text_color, font=body_font)

    img.save(img_path)
