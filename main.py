import requests
from pathlib import Path
import shutil


def get_ext(filename: str) -> str:
    extension = Path(filename).suffix
    return extension


def download_image(url: str, path: str, name_ext: str) -> None:
    image = requests.get(url=url)
    image.raise_for_status()
    with open(path / name_ext, "wb") as file:
        file.write(image.content)


def get_dog() -> str:
    response = requests.get(url="https://random.dog/woof")
    response.raise_for_status()
    return response.text


def main() -> None:
    shutil.rmtree("./assets/pictures")
    pictures_folder = Path("./assets/pictures")
    pictures_folder.mkdir(parents=True, exist_ok=False)
    for i in range(10):
        file_name: str = get_dog()
        file_ext: str = get_ext(file_name)
        if file_ext not in [".mp4", ".webm"]:
            file_link: str = f"https://random.dog/{file_name}"
            download_image(file_link,
                           pictures_folder,
                           f"dog_{i}{file_ext}")


if __name__ == '__main__':
    main()
