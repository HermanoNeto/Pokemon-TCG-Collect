import requests, json, os

class Card():
    def __init__(self, set_name:str, card_num:str|int) -> None:
        self.set_name = set_name
        self.num = card_num
        self.set_id = self.getSetID(self.set_name)
        self.set_image = self.getCard()["images"]["small"]
        self.set_logo = self.getCard()["set"]["images"]["logo"]
        self.set_cardAmmount = self.getCard()["set"]["total"]

    def getCard(self) -> dict:
        card_info = requests.get(f"https://api.pokemontcg.io/v2/cards/{self.set_id}-{self.num}")
        card_info_dict = json.loads(card_info.text)
        return card_info_dict["data"]

    def getSetID(self,name:str) -> str|None:
        sets=requests.get("https://api.pokemontcg.io/v2/sets")
        set_dict=json.loads(sets.text)
        for cardset in set_dict["data"]:
            if name in cardset["name"]:
                return cardset["id"]

class Inventory():
    def __init__(self, cardset: str) -> None:
        self.card_set = cardset
        self.filename = "cards_inventory.json"
        
        if not os.path.exists(f"resources/{self.filename}"):
            with open(f"resources/{self.filename}", 'w') as f:
                json.dump({}, f)
        
        with open(f"resources/{self.filename}", 'r') as f:
            self.data = json.load(f)

    def save(self, imgURL: str) -> None:
        if self.card_set not in self.data:
            self.data[self.card_set] = []
        
        self.data[self.card_set].append(imgURL)
        
        with open(f"resources/{self.filename}", 'w') as f:
            json.dump(self.data, f, indent=4)

    def show(self) -> list:
        return self.data.get(self.card_set, [])
