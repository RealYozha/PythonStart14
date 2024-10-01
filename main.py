import requests
from pathlib import Path
import shutil


IMAGES_DIRECTORY = "./pictures"


def download_image(image: str, path: str, name_ext: str) -> None:
    with open(path / name_ext, "wb") as file:
        file.write(image)


def get_dog() -> str:
    payload = {"filter": "mp4,webm"}
    response = requests.get(url="https://random.dog/woof.json", params=payload)
    response.raise_for_status()
    return response.json()['url']


def main() -> None:
    pictures_folder = Path(IMAGES_DIRECTORY)
    if pictures_folder.exists():
        shutil.rmtree(IMAGES_DIRECTORY)
    pictures_folder.mkdir(parents=True, exist_ok=False)
    for i in range(50):
        link = get_dog()
        ext = Path(link).suffix
        image = requests.get(url=link)
        image.raise_for_status()
        filename = f'dog{i+1}{ext}'
        download_image(image.content, pictures_folder, filename)


if __name__ == '__main__':
    main()
