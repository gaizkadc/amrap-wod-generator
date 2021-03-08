import datetime
import os
import random

from PIL import Image, ImageFont, ImageDraw, ImageEnhance


def create_wod_image(power_amrap_wod, endurance_amrap_wod, logger):
    logger.info('creating wod image')

    today = datetime.datetime.now()
    resulting_image_folder_path = os.getenv('IMGS_FOLDER')
    resulting_img_path = resulting_image_folder_path + '/WOD' + today.strftime('%Y%m%d') + '.png'

    background_path = get_background()

    darken_img(background_path, resulting_img_path)

    text_color = (255, 255, 255)
    title_height = 230
    write_title(today, resulting_img_path, text_color, title_height)
    write_warmup(resulting_img_path, text_color)
    write_power_amrap_wod(power_amrap_wod, resulting_img_path, text_color)
    write_endurance_amrap_wod(endurance_amrap_wod, resulting_img_path, text_color)

    logger.info('wod image created')

    return resulting_img_path


def get_background():
    return 'backgrounds/' + random.choice(os.listdir('backgrounds'))


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


def write_warmup(img_path, text_color):
    title_font = ImageFont.truetype('fonts/Montserrat-Medium.ttf', 30)
    body_font = ImageFont.truetype('fonts/Montserrat-Regular.ttf', 30)

    title_text_position = (350, 400)
    title_text = 'Warmup: 15 min'

    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)
    draw.text(title_text_position, title_text, text_color, font=title_font)
    draw.line((0, 440, 600, 440), width=3)

    warmup_1_text = '* 2 min Warmup'
    warmup_1_text_position = (100, 460)
    draw.text(warmup_1_text_position, warmup_1_text, text_color, font=body_font)

    warmup_2_text = '* 12 min HIIT'
    warmup_2_text_position = (100, 510)
    draw.text(warmup_2_text_position, warmup_2_text, text_color, font=body_font)

    img.save(img_path)

def write_power_amrap_wod(power_amrap_wod, img_path, text_color):
    title_font = ImageFont.truetype('fonts/Montserrat-Medium.ttf', 30)
    body_font = ImageFont.truetype('fonts/Montserrat-Regular.ttf', 30)

    title_text_position = (263, 600)
    title_text = 'Power AMRAP: 15 min'

    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)
    draw.text(title_text_position, title_text, text_color, font=title_font)
    draw.line((0, 640, 600, 640), width=3)

    pwer_1_text = '* ' + power_amrap_wod.first_exercise.print()
    power_1_text_position = (100, 660)
    draw.text(power_1_text_position, pwer_1_text, text_color, font=body_font)

    power_2_text = '* ' + power_amrap_wod.second_exercise.print()
    power_2_text_position = (100, 710)
    draw.text(power_2_text_position, power_2_text, text_color, font=body_font)

    power_3_text = '* ' + power_amrap_wod.third_exercise.print()
    power_3_text_position = (100, 760)
    draw.text(power_3_text_position, power_3_text, text_color, font=body_font)

    img.save(img_path)


def write_endurance_amrap_wod(endurance_amrap_wod, img_path, text_color):
    title_font = ImageFont.truetype('fonts/Montserrat-Medium.ttf', 30)
    body_font = ImageFont.truetype('fonts/Montserrat-Regular.ttf', 30)

    title_text_position = (193, 850)
    title_text = 'Endurance AMRAP: 15 min'

    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)
    draw.text(title_text_position, title_text, text_color, font=title_font)
    draw.line((0, 890, 600, 890), width=3)

    pwer_1_text = '* ' + endurance_amrap_wod.first_exercise.print()
    power_1_text_position = (100, 910)
    draw.text(power_1_text_position, pwer_1_text, text_color, font=body_font)

    power_2_text = '* ' + endurance_amrap_wod.second_exercise.print()
    power_2_text_position = (100, 960)
    draw.text(power_2_text_position, power_2_text, text_color, font=body_font)

    power_3_text = '* ' + endurance_amrap_wod.third_exercise.print()
    power_3_text_position = (100, 1010)
    draw.text(power_3_text_position, power_3_text, text_color, font=body_font)

    img.save(img_path)
