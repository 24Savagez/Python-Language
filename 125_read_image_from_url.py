import webbrowser
from urllib.request import urlopen


def read_image_url(url):
    with urlopen(url) as response, open("img.jpg", "wb") as out_file:
        data = response.read()
        out_file.write(data)


if __name__ == '__main__':
    url = "https://i.pinimg.com/originals/43/4e/c4/434ec457a059e930c271836b308dffa8.jpg"
    # webbrowser.open(url)
    read_image_url(url)
