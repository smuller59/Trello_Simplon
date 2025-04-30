import boards
import cards

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

def create_deck():
    """Fonction qui crée une liste et l'ajoute au boards"""
    new_deck= [{deck_list}]
    add_deck_board=new_deck.append({boards})
    return add_deck_board

pass

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
