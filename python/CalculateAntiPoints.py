import csv


def CalculateAntiPoints(antiPoints, enemyHeroesIndex):
    heroesPoints = []
    with open("antiTable.csv", "r", encoding="utf-8") as AntiTable:
        reader = csv.reader(AntiTable)
        next(reader)
        for row in reader:
            heroesPoints.append(row)

    for i, heroPoints in enumerate(heroesPoints):
        for j, points in enumerate(heroPoints, -1):
            if points == "":
                break
            if j != -1 and j in enemyHeroesIndex:
                antiPoints[i]["points"] += int(points)
