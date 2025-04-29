import lists

deck_test = {
    "name": "deck test",
    "card_list": list(),
    "origin_board": "board test",
    "description": "Example of a deck for test purpose."
}

board_test = {
    "name": "board test",
    "deck_list": list(),
    "description": "Example of a board for test purpose."
}

board_list = [board_test]

def add_deck_to_board(deck: dict, board_name: str) -> bool:
    """Add the deck 'deck' to the board havin the name 'board_name'
    Return True if the deck is added, otherwise return False

    Args:
        deck (dict): The deck to be added
        board_name (str): The name of the board that will host the deck

    Returns:
        bool: Is the deck added somewhere during the operation ?
    """
    
    # Add a deck to the input board
    for board in board_list:
        if (board["name"] == board_name):
            board["deck_list"].append(deck)
            return True
    else:
        return False


def main():
    print(add_deck_to_board(deck_test, "test board"))
    print(board_test)

    print(add_deck_to_board(deck_test, "board test"))
    print(board_test)

if __name__ == "__main__":
    main()