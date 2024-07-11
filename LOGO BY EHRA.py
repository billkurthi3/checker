from pyfiglet import Figlet

F = '\033[1;32m'
Z = '\033[1;31m'
S = '\033[1;33m'
B = '\x1b[38;5;208m'
print ("\x1b[38;5;208m")
fig = Figlet(font='poison')
logo = fig.renderText(f'EHRA')
print(logo)







import os
os.system('pip install Pillow')
import telebot
from PIL import Image
from telebot import types
import os


TOKEN = 'TOKEN HERE '
bot = telebot.TeleBot(TOKEN)

ASCII_CHARS = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@', '٪', '&', ')', '(', '/', '*', '"', "'", ':', '؛', '!', '؟', '.', '،', '_', '~', '`', '|', '•', '√', 'Π', '÷', '×', '¶', '∆', '،', '{', '}', '=', '°', '^', '¢', '¥', '€', '£', '[', ']', '℅', '™', '®', '©', '\\','۩', '۞', '§', '¤', '¶', '±', '£', '¥', '€', '¢', 'ƒ', '©', '®', '™', '÷', '×', '√', 'Π', '■', '∞', '□', '≈', '≠', '≤', '≥', '∑', '∫', '∏', '∂', '∇', '∈', '∉', '∋', '∐', '∮', '∯', '█', '∆']

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 2
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ''
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // 25]
    return ascii_str

def convert_image_to_ascii(image_path, new_width=55):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    image = resize_image(image, new_width)

    img_width, img_height = image.size
    ascii_img = ''

    for y in range(img_height):
        for x in range(img_width):
            rgb_color = image.getpixel((x, y))
            r, g, b = rgb_color
            brightness = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
            ascii_img += ASCII_CHARS[brightness // 25]
        ascii_img += '\n'

    return ascii_img

def save_ascii_image_to_file(ascii_img, file_name, image_name):
    with open(file_name, 'w') as f:
        f.write(f"print(f'''{ascii_img}''')")
        f.write(f'\n\n# DONE BY EHRA: {image_name}')

@bot.message_handler(commands=['start'])
def start(message):
    buttons = types.InlineKeyboardMarkup(row_width=1)
    but1 = types.InlineKeyboardButton(text='- ⚜️ Developer', url='https://t.me/mj_ehra')
    but2 = types.InlineKeyboardButton(text='- 🔰Channel Developer', url='https://t.me/GODT00LS')
    but3 = types.InlineKeyboardButton(text='- 👻MY Hacker', url='https://t.me/hacktvist')
    buttons.add(but1, but2 , but3)
    bot.send_message(message.chat.id, '''<strong>
  Wₑₗcₒₘₑ ₘy dₑₐᵣ💫
    Yₒᵤ cₐₙ ₛₑₙd ₐₙy ᵢₘₐgₑ, ₐₙd ₜₕᵢₛ bₒₜ wᵢₗₗ cᵣₑₐₜₑ ₐₙ ₐₚₚᵣₒₓᵢₘₐₜₑ ₗₒgₒ fₒᵣ ₜₕₑ ᵢₘₐgₑ yₒᵤ ₛₑₙₜ
</strong>''', parse_mode='html', reply_to_message_id=message.message_id, reply_markup=buttons)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.reply_to(message, "Converting the image to a Python logo BY: @MJ_EHRA")
    photo_id = message.photo[-1].file_id
    file_info = bot.get_file(photo_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("input_image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
    ascii_art = convert_image_to_ascii("input_image.jpg")
    save_ascii_image_to_file(ascii_art, "logo.py", file_info.file_path)
    with open("logo.py", "rb") as logo_file:
        bot.send_document(message.chat.id, logo_file)
    os.remove("input_image.jpg")
    os.remove("logo.py")
@bot.message_handler(content_types=['document'])
def handle_document(message):
    if message.document.file_name == "logo.py":
        bot.reply_to(message, "The image has been converted into a logo")
    else:
        bot.reply_to(message, "mistake")


bot.infinity_polling()