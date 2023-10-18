import eel

from python.CalculateAntiPoints import CalculateAntiPoints
from python.CropScoreboard import CropScoreboard
from python.IdentifyHeroes import IdentifyHeroes

heroNames = [
    "D.Va",
    "Winston",
    "Orisa",
    "Zarya",
    "Sigma",
    "Junker_Queen",
    "Doomfist",
    "Reinhart",
    "Ramattra",
    "Wrecking_Ball",
    "Roadhog",
    "Ashe",
    "Widowmaker",
    "Echo",
    "Cassidy",
    "Genji",
    "Symmetra",
    "Junkrat",
    "Sojourn",
    "Soldier76",
    "Sombra",
    "Torbjorn",
    "Tracer",
    "Hanzo",
    "Bastion",
    "Pharah",
    "Mei",
    "Reaper",
    "Ana",
    "Kiriko",
    "Zenyatta",
    "Baptiste",
    "Brigitte",
    "Mercy",
    "Moira",
    "Lifeweaver",
    "Lucio",
]
roleCounts = {"tank": 11, "damage": 17, "support": 9}


@eel.expose
def GuessAntiPick():
    antiPoints = []
    temporaryHeroNames = heroNames.copy()
    for roleName, roleCount in roleCounts.items():
        for i in range(roleCount):
            antiPoints.append(
                {"name": temporaryHeroNames.pop(0), "points": 0, "role": roleName}
            )

    CropScoreboard()
    enemyHeroesIndex = IdentifyHeroes(heroNames)
    enemyHeroes = []
    for i in enemyHeroesIndex:
        if i is None:
            enemyHeroes.append("None")
        else:
            enemyHeroes.append(heroNames[i])

    if None in enemyHeroesIndex:
        return {"enemyHeroes": enemyHeroes}
    else:
        CalculateAntiPoints(antiPoints, enemyHeroesIndex)
        return {"enemyHeroes": enemyHeroes, "antiPoints": antiPoints}


eel.init("web")
eel.start("index.html", size=(480, 1080))
