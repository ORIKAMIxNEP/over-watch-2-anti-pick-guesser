import cv2


def IdentifyHeroes(heroNames):
    maxSimilarity = 0
    identifiedHeroIndex = [None for i in range(5)]
    for i in range(5):
        for j, heroName in enumerate(heroNames):
            templateImage = cv2.imread(
                "templateImages/" + heroName + ".jpg")
            originalImage = cv2.imread(
                "originalImages/original" + str(i + 1) + ".jpg")
            similarity = cv2.matchTemplate(
                originalImage, templateImage, cv2.TM_CCOEFF_NORMED)[0][0]
            if similarity > 0.9 and similarity > maxSimilarity:
                maxSimilarity = similarity
                identifiedHeroIndex[i] = j
        # print(str(i + 1) + ":" + str(maxSimilarity)) 後で消す
        maxSimilarity = 0
    return identifiedHeroIndex
