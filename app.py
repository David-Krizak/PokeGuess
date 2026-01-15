from flask import *
import requests, random, json, os

app = Flask(__name__)
app.secret_key = "Moja-draga-i-ja"
SCORES_FILE = "scores.json"
def load_scores():
    if not os.path.exists(SCORES_FILE):
        return []
    with open(SCORES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_score(player, score):
    scores = load_scores()
    scores.append({"player": player, "score": score})
    scores.sort(key=lambda x: x["score"], reverse=True)
    with open(SCORES_FILE, "w", encoding="utf-8") as f:
        json.dump(scores[:20], f, indent=2, ensure_ascii=False)


def get_random_pokemon():
    pid = random.randint(1, 151)
    data = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{pid}", timeout=5
    ).json()
    return {
        "name": data["name"],
        "image": data["sprites"]["other"]["official-artwork"]["front_default"],
        "types": [t["type"]["name"] for t in data["types"]],
        "height": data["height"],
        "weight": data["weight"],
    }


@app.route("/")
def index():
    session.clear()
    session["pokemon"] = get_random_pokemon()
    session["lives"] = 3
    session["score"] = 0
    session["hints"] = 0
    return render_template("index.html")


@app.route("/pokemon")
def pokemon():
    return jsonify(session["pokemon"])


@app.route("/guess", methods=["POST"])
def guess():
    guess = request.json.get("guess", "").lower().strip()
    p = session["pokemon"]

    if guess == p["name"]:
        session["score"] += 1
        session["pokemon"] = get_random_pokemon()
        session["lives"] = 3
        session["hints"] = 0
        return jsonify(result="correct", score=session["score"])

    session["lives"] -= 1
    if session["lives"] <= 0:
        return jsonify(
            result="gameover",
            answer=p["name"],
            score=session["score"],
        )

    return jsonify(result="wrong", lives=session["lives"])
@app.route("/hint")
def hint():
    session["hints"] += 1
    p = session["pokemon"]

    hints = [
        f"Tip: {', '.join(p['types'])}",
        f"Visina: {p['height']}",
        f"Težina: {p['weight']}",
    ]

    i = min(session["hints"] - 1, len(hints) - 1)
    return jsonify(hint=hints[i])
@app.route("/giveup", methods=["POST"])
def giveup():
    return jsonify(answer=session["pokemon"]["name"], score=session["score"])
@app.route("/save-score", methods=["POST"])
def save_score_route():
    data = request.json
    save_score(data.get("player", "Anon"), data.get("score", 0))
    session.clear()
    return jsonify(status="saved")


@app.route("/scores")
def scores():
    return jsonify(load_scores())


if __name__ == "__main__":
    app.run(debug=True)
