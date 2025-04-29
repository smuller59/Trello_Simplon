import boards
import deck as d

card = {
        "name" : "mon_nom",
        "description" : "ma description",
        "origin" : "mon_deck"
        }

deck = {
        "origin" : "mon_deck",
        "list_cards": [card, card, card]
        }

# def get_card(card_name):
#     return card

# def delete_card(card_name:str, deck:dict)->bool:
    

def create_card(name:str, description: str, origin: str) -> dict:
    card = {"name": name, "description": description, "origin": origin}
    d.add_card_to_deck(origin, card)    

def get_deck(deck_name: str) -> dict:
    return deck

def main():
    pass

if __name__ == "__main__":
    main()