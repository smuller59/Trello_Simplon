import json
import trello as t


def display_trello(trello):
    for board in trello:
        for key_board, value_board in board.items():
            if key_board == "deck_list":
                # print(f"mon deck: {value_board}")
                for deck in value_board:
                    for key_deck, value_deck in deck.items():
                        if key_deck == 'card_list':
                            print(f"card list : {value_deck}")
                        else:
                            print(f"{key_deck}{value_deck}")
            else:
                print(f"{key_board}: {value_board}")
        print("\n")
            

def main():
    trello = t.create_trello()
    # display_trello(trello)
    t.delete_board("ma board numero 1", trello)
    display_trello(trello)
    
    # print(trello)
    trello_js = json.dumps(trello)
    # print(trello_js)


if __name__ == "__main__":
    main()