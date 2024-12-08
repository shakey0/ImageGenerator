import random
import string
from PIL import Image

# Function to generate a random color
def generate_random_color():
    return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Function to generate a random 10-character string
def generate_random_filename():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + "_random.webp"

# Create a 1920x1080 image with a random color
def generate_image():
    color = generate_random_color()
    filename = generate_random_filename()
    image = Image.new("RGB", (1920, 1080), color)
    image.save(filename)
    print(f"Image saved as {filename}")

if __name__ == "__main__":
    generate_image()
