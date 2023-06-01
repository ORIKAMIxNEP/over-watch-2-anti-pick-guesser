let keydownFlag = false;

setInterval(async function () {
  const data = await eel.GuessAntiPick()();

  if (data.hasOwnProperty("antiPoints")) {
    const enemyHeroes = data["enemyHeroes"];
    let enemyHeroesHTML = "";
    for (let i = 0; i < enemyHeroes.length; i++) {
      enemyHeroesHTML += enemyHeroes[i] + "<br>";
    }
    document.getElementById("enemy_heroes").innerHTML = enemyHeroesHTML;

    antiPoints = {};
    data["antiPoints"].forEach((item) => {
      if (!antiPoints[item.role]) {
        antiPoints[item.role] = [];
      }
      antiPoints[item.role].push(item);
    });
    for (const role in antiPoints) {
      antiPoints[role].sort((a, b) => b.points - a.points);
    }

    let recommendedHeroesHTML = "";
    for (const role in antiPoints) {
      recommendedHeroesHTML +=
        "<p>【" + role.charAt(0).toUpperCase() + role.slice(1) + "】</p>";
      antiPoints[role].slice(0, 5).forEach((item, index) => {
        recommendedHeroesHTML +=
          index + 1 + ". " + item.name.replace("_", " ") + "<br>";
      });
    }
    document.getElementById("recommended_heroes").innerHTML =
      recommendedHeroesHTML;
  }
}, 1000);

document.addEventListener("keyup", function (event) {
  if (event.code == "Tab") {
    keydownFlag = false;
  }
});
