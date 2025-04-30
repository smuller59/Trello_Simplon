import boards as b
import cards as c 

def add_card_to_deck(card:dict, deck_name:str):
    #rechercher dans deck_list le deck qui a le nom deck_name
    for deck in deck_list:
        if (deck["name"] == deck_name):
            #Dans deck, ajouter à l'élément card_list le dictionnaire card donné en argument
            deck["card_list"].append(card)
            return True
        else:
            return False

def create_deck(name: dict, description:str, origin_board:str) -> dict:
    template_deck=dict()
    
    card1 = c.create_card("card1", "description de la carte 1", "Trelloplon")
    card2 = c.create_card("card2", "description de la carte 2", "Trelloplon")
    card3 = c.create_card("card3", "description de la carte 3", "Trelloplon")
    cards= [card1,card2,card3]
    template_deck["name"]= name
    template_deck["card_list"]= cards
    template_deck["description"]= description
    template_deck["origin_board"]= origin_board
    return template_deck

def request_card(name:str):
    #demande une carte
    # demande_carte= get_create_card()
    # return (cards)
    pass

def delete_card(card_name:str, deck:dict):
    for i in range(len(deck["card_list"])):
        card = deck["card_list"][i]
        print(card["name"])
        if card["name"] == card_name:
            del(deck["card_list"][i])
            return True
    else:
        return False


def get_deck():
    pass  

def main():
    deck=create_deck('test',"description test","toto")

    
   

if __name__ == "__main__":
    main()
