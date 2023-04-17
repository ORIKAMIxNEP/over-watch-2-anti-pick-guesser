from PIL import ImageGrab


def CropScoreboard():
    screenImage = ImageGrab.grab()
    for i in range(5):
        screenImage.crop((343, 609 + 62 * i, 403, 670 + 62 * i)
                         ).save("originalImages/original" + str(i + 1) + ".jpg")
