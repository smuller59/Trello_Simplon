import boards as b
import cards as c 

deck_list = {"name" : "nom du deck",
       "card_list" :[],
       "description" : "description du deck",
       "origin_board" : "board1" }

def add_card_to_deck(card:dict, deck_name:str):
    #rechercher dans deck_list le deck qui a le nom deck_name
    for deck in deck_list:
        if (deck["name"] == deck_name):
            #Dans deck, ajouter à l'élément card_list le dictionnaire card donné en argument
            deck["card_list"].append(card)
            return True
        else:
            return False

template_deck = {"name" : "Trelloplon",
                 "card_list":[],
                "description":"bouchon_deck",
                "origin_board" : "Origin_toto"
                }
                

def create_deck(name: str, description:str, origin_board:str) -> dict:
    template_deck = {"name" : "Trelloplon",
                 "card_list":[],
                "description":"bouchon_deck",
                "origin_board" : "Origin_toto"
                }
    card1 = c.create_card ("card1", "description de la carte 1", "Trelloplon")
    card2 = c.create_card ("card2", "description de la carte 2", "Trelloplon")
    card3 = c.create_card ("card3", "description de la carte 2", "Trelloplon")
    cards= [card1,card2,card3]
    template_deck["name"]= name
    template_deck["card_list"]= cards
    template_deck["description"]= description
    template_deck["origin_board"]= origin_board
    return template_deck
pass

def request_card(name:str):
    #demande une carte
    demande_carte= get_create_card()
    return (cards)

def delete_deck():
    """Fonction qui supprime une liste"""
pass

def get_deck():
pass  

def main():
    print ("c")
    pass

if __name__ == "__main__":
    main()
