from PIL import Image, ImageDraw, ImageFont
import os

# Folder for images
output_dir = "educational_images_842x595"
os.makedirs(output_dir, exist_ok=True)

subjects = [
    "Mathematics",
    "Science",
    "History",
    "Geography",
    "Physics",
    "Biology",
    "Computer Science",
    "Economics"
]

WIDTH, HEIGHT = 595, 842

for i, subject in enumerate(subjects, start=1):
    img = Image.new("RGB", (WIDTH, HEIGHT), "#F4F6F8")
    draw = ImageDraw.Draw(img)

    font = ImageFont.load_default()

    title = f"{subject}\nEducational Preview"
    text_w, text_h = draw.multiline_textsize(title, font=font)

    draw.multiline_text(
        ((WIDTH - text_w) / 2, (HEIGHT - text_h) / 2),
        title,
        fill="#2C2C2C",
        font=font,
        align="center"
    )

    img.save(f"{output_dir}/preview_{i}.png")

print("Images created successfully.")
