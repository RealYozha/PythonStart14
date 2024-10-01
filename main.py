import requests
from pathlib import Path
import shutil


IMAGES_DIRECTORY = "./assets/pictures"


def download_image(image: str, path: str, name_ext: str) -> None:
    with open(path / name_ext, "wb") as file:
        file.write(image)


def get_dog() -> str:
    payload = {"filter": "mp4,webm"}
    response = requests.get(url="https://random.dog/woof.json", params=payload)
    response.raise_for_status()
    return response.json()['url']


def main() -> None:
    # i dare if u will send this back again
    # for the 6th time and not even say wtf is wrong
    pictures_folder = Path(IMAGES_DIRECTORY)
    if pictures_folder.exists():
        shutil.rmtree(IMAGES_DIRECTORY)
    pictures_folder.mkdir(parents=True, exist_ok=False)
    for i in range(50):
        link = get_dog()
        image = requests.get(url=link)
        image.raise_for_status()
        download_image(image.content)


if __name__ == '__main__':
    main()
