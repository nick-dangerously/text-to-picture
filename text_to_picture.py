#! python3
# text_to_picture.py - makes a picture out of a text string

import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

LOGO_FILE = 'logo.jpg'
TEXT_FILE = 'source_text.txt'
FONT_TYPE = 'mononoki-Regular.ttf'
FONT_SIZE = 12

fonts_folder = 'C:\\Windows\\Fonts' # For windows
# fonts_folder = '/usr/share/fonts/truetype'# For linux. Need to escape slashes?
mono_font = ImageFont.truetype(os.path.join(fonts_folder, FONT_TYPE), FONT_SIZE)
font_width = mono_font.getsize('a')[0]
font_height = mono_font.getsize('a')[1]
logo_im = Image.open(LOGO_FILE)


# Resize image to match font ratio.
## Ratio of font width to height
def resize_logo():
    "Since the font is not a square (it is taller than it is wider), \
    stretch the image to compensate."
    
    ratio = font_width / font_height
    logo_im_width, logo_im_height = logo_im.size
    logo_im = logo_im.resize((int(logo_im_width * (1 + ratio)), logo_im_height), Image.ANTIALIAS)
    logo_im.save('resized_logo.jpg')

# Get logo dimensions
logo_im_width, logo_im_height = logo_im.size
print('Resized logo dimensions are: %s, %s' % (logo_im_width, logo_im_height))


# Read the image data into some sort of data structure
pixels = list(logo_im.getdata())

# Read in a text and split it on characters
text = list(open(TEXT_FILE).read())

# Create a new Image to write the text into
final_im_width = font_width * logo_im_width
final_im_height = font_height * logo_im_height
final_im = Image.new('RGBA', (final_im_width, final_im_height), 'white')
draw = ImageDraw.Draw(final_im)

# Write out the characters and change their color
for y in range(logo_im_height):
    for x in range(logo_im_width):
        index = logo_im_width * y + x
        color = pixels[index]
        char = text[index]
        # print(str(index))
        # print(char)
        # print('%s, %s' % (x, y))
        # print(char + ' ' + str(color))

        # Draw in the text
        draw.text((x * font_width, y * font_height), char, fill=color)

final_im.save('text_picture.png')
