import cv2


def IdentifyHeroes(heroNames):
    maxSimilarity = 0
    identifiedHeroIndex = [None for i in range(5)]
    for i in range(2):
        if None not in identifiedHeroIndex:
            break
        for j in range(5):
            for k, heroName in enumerate(heroNames):
                if i == 1 and k == 0 and identifiedHeroIndex[j] is not None:
                    break
                templateImage = cv2.imread("templateImages/" + heroName + ".jpg")
                originalImage = cv2.imread(
                    "originalImages/original" + str(j + 1) + ".jpg"
                )

                if i == 1:
                    width, height = templateImage.shape[:2]
                    cv2.circle(
                        templateImage, (width // 2, height // 2), 25, (0, 0, 0), -1
                    )
                    cv2.circle(
                        originalImage, (width // 2, height // 2), 25, (0, 0, 0), -1
                    )

                similarity = cv2.matchTemplate(
                    originalImage, templateImage, cv2.TM_CCOEFF_NORMED
                )[0][0]
                if similarity > 0.9 and similarity > maxSimilarity:
                    maxSimilarity = similarity
                    identifiedHeroIndex[j] = k
            maxSimilarity = 0
    return identifiedHeroIndex
