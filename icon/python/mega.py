from PIL import Image, ImageDraw, ImageFont

width, height = 32, 32
bg_color = "black"
letter_colors = {"M": "red", "E": "green", "G": "blue", "A": "yellow"}

letters = ["M", "E", "G", "A"]
frames = []

try:
    font = ImageFont.truetype("arialbd.ttf", size=20)
except IOError:
    font = ImageFont.load_default()

for letter in letters:
    img = Image.new("RGB", (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)    
    bbox = font.getbbox(letter)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    position = ((width - text_width) // 2, (height - text_height) // 2)
    draw.text(position, letter, fill=letter_colors[letter], font=font)
    frames.append(img)

# stored GIF
output_path = "mega.gif"
frames[0].save(
    output_path,
    save_all=True,
    append_images=frames[1:],
    optimize=False,
    duration=500,
    loop=0
)

print(f"GIF stored {output_path}")
