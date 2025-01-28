from PIL import Image, ImageDraw, ImageFont
import os

# Create the images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# List of words and their corresponding colors
words = [
    ("Finn", "#FF5733"),
    ("Mom", "#33FF57"),
    ("Want", "#3357FF"),
    ("Dad", "#FF33A1"),
    ("Fun Sound 1", "#FF5733"),
    ("Grandma", "#33FF57"),
    ("Eat", "#3357FF"),
    ("Declan", "#FF33A1"),
    ("Fun Sound 2", "#FF5733"),
    ("Ashling", "#33FF57"),
    ("Killian", "#3357FF"),
    ("Don't Want", "#FF33A1"),
    ("Aunt", "#FF5733"),
    ("Uncle", "#33FF57"),
    ("Fun Sound 3", "#3357FF"),
    ("Funny", "#FF33A1"),
    ("Fun Sound 4", "#FF5733"),
    ("Watch", "#33FF57"),
    ("Cuddle", "#3357FF"),
    ("Baby", "#FF33A1"),
    ("Fun Sound 5", "#FF5733"),
    ("Poop", "#33FF57"),
    ("Sing", "#3357FF"),
    ("Play", "#FF33A1"),
    ("Love", "#FF5733"),
    ("Fun Sound 6", "#33FF57"),
    ("Fun Sound 7", "#3357FF")
]

# Font settings
font_size = 40
font = ImageFont.truetype("arial.ttf", font_size)

# Generate images
for word, color in words:
    img = Image.new('RGB', (200, 200), color)
    draw = ImageDraw.Draw(img)
    text_bbox = draw.textbbox((0, 0), word, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_x = (img.width - text_width) / 2
    text_y = (img.height - text_height) / 2
    draw.text((text_x, text_y), word, fill="white", font=font)
    img.save(f'images/{word.replace(" ", "")}.jpg')