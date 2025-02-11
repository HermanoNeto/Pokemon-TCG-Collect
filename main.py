import requests
import json
from flask import Flask, request, render_template
from cardInfo import Card, Inventory

app = Flask(__name__)

@app.route("/")
def displayHomePage():
    available_sets = fetchAvailableSets()
    return render_template("home.html", sets=available_sets)

@app.route("/", methods=["GET", "POST"])
def handleCardSubmission():
    global current_card
    try:
        current_card = Card(request.form["set_name"], request.form["card_number"])
    except KeyError:
        return displayHomePage()
    return render_template(
        "card.html",
        image=current_card.set_image,
        set_name=current_card.set_name,
        card_number=current_card.num,
        total_cards_in_set=current_card.set_cardAmmount,
        set_logo=current_card.set_logo
    )

@app.route("/sets", methods=["GET", "POST"])
def manageUserProfile():
    try:
        inventory = Inventory(current_card.set_name)
        inventory_list = inventory.show()
        for image_url in inventory_list:
            if current_card.set_image == image_url:
                raise Exception(KeyError)
        inventory.save(current_card.set_image)
    except:
        pass
    available_sets = fetchAvailableSets()
    return render_template(
        "profile.html",
        sets=available_sets
    )

@app.route("/<set_name>")
def displaySetCards(set_name):
    inventory = Inventory(set_name)
    sorted_cards = sorted(inventory.show(), key=sortCards)
    if len(sorted_cards) == 0:
        return f"""
        <title>{set_name}</title>
        <link rel="icon" href="data:;base64,iVBORw0KGgo=">
        <link rel="icon" href="https://upload.wikimedia.org/wikipedia/commons/5/53/Pok%C3%A9_Ball_icon.svg" type="image/x-icon" />
        <body style="display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; font-family: Arial, sans-serif; background-color: #f4f4f4;">
            <div style="text-align: center; padding: 20px; background-color: #ffcccc; border: 2px solid #ff0000; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
                <h2>No cards found in this set!</h2>
                <button onclick="history.back()" style="display: inline-block; margin-top: 20px; padding: 10px 20px; background-color: #ff0000; color: white; text-decoration: none; border-radius: 5px; font-weight: bold; transition: background-color 0.3s;">
                    Go back
                </button>
            </div>
        </body>"""
    return render_template(
        "set_cards.html",
        current_set=set_name,
        cards=sorted_cards
    )

def fetchAvailableSets() -> list:
    response = requests.get("https://api.pokemontcg.io/v2/sets")
    sets_data = json.loads(response.text)
    set_names:list = [cardset["name"] for cardset in sets_data["data"]]
    return set_names

def sortCards(url: str) -> int:
    return int(url.split('/')[-1].split('.')[0])

if __name__ == "__main__":
    app.run(debug=True)
