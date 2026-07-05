import os
import requests

from datetime import datetime

folder = "Pic"

def I2M(Propmt):
    PId = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    prompt = Propmt

    os.makedirs(folder, exist_ok=True)

    filename = PId + ".png"

    url = f"https://image.pollinations.ai/prompt/{prompt}"

    img = requests.get(url)

    filepath = os.path.join(folder, filename)

    with open(filepath, "wb") as f:
        f.write(img.content)

    print(f"Image saved to: {filepath}")
    return filepath