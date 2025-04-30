import boards as b
import decks as d

card = {
        "name" : "mon_nom",
        "description" : "ma description",
        "origin_deck" : "mon_deck"
        }

deck = {
        "origin" : "mon_deck",
        "list_cards": [card, card, card]
        }

# def get_card(card_name):
#     return card

# def delete_card(card_name:str, deck:dict)->bool:
    

def create_card(name:str, description: str, origin: str) -> dict:
    """_summary_

    Args:
        name (str): _description_
        description (str): _description_
        origin (str): _description_

    Returns:
        dict: _description_
    """
    card = {"name": name, "description": description, "origin": origin}
    d.add_card_to_deck(origin, card)    

def get_deck(deck_name: str) -> dict:
    """_summary_

    Args:
        deck_name (str): _description_

    Returns:
        dict: _description_
    """
    return deck

def main():
    pass

if __name__ == "__main__":
    main()