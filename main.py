import fstream
from shutil import rmtree
from pathlib import Path


IMAGES_DIRECTORY = "./images"


def download_dog_picture(number):
    url = "https://random.dog/woof?filter=mp4,webm"
    filename = f"random_dog_{number}"
    path = f"{IMAGES_DIRECTORY}/{filename}"
    Path(path).mkdir(exist_ok=True)
    fstream.download_image(url,
                           path)


def main():
    if Path(IMAGES_DIRECTORY).exists():
        rmtree(IMAGES_DIRECTORY)
    for i in range(50):
        download_dog_picture(i)


if __name__ == "__main__":
    main()
