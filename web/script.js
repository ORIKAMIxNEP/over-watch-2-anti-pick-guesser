let keydownFlag = false;

window.addEventListener("keydown", async function (event) {
  if (event.code == "Tab" && !keydownFlag) {
    const data = await eel.GuessAntiPick()();

    const enemyHeroes = data["enemyHeroes"];
    let enemyHeroesHTML = "";
    for (let i = 0; i < enemyHeroes.length; i++) {
      enemyHeroesHTML += enemyHeroes[i] + "<br>";
    }
    document.getElementById("enemy_heroes").innerHTML = enemyHeroesHTML;

    if (data.hasOwnProperty("antiPoints")) {
      const antiPoints = data["antiPoints"];
      antiPoints.sort(
        (element1, element2) => element2.points - element1.points
      );
      let recommendedHeroesHTML = "";
      for (let i = 0; i < 5; i++) {
        recommendedHeroesHTML += antiPoints[i]["name"] + "<br>";
      }
      document.getElementById("recommended_heroes").innerHTML =
        recommendedHeroesHTML;
    }

    keydownFlag = true;
  }
});

document.addEventListener("keyup", function (event) {
  if (event.code == "Tab") {
    keydownFlag = false;
  }
});
