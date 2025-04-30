import decks as d
import app

def create_board(board_name: str, board_description: str) -> dict:
    """Create a board

    Args:
        board_name (str): The name of the board to create
        board_description (str): The description of the board to create

    Returns:
        dict: The board created
    """

    # Temporary: create an empty board
    board = {
        "name": board_name,
        "deck_list": list(),
        "description": board_description
    }

    # Request creation of a set of decks
    deck1 = d.create_deck("Deck 1", "Test ask creation of deck 1", board_name)
    deck2 = d.create_deck("Deck 2", "Test ask creation of deck 2", board_name)
    deck3 = d.create_deck("Deck 3", "Test ask creation of deck 3", board_name)
    add_deck_to_board(deck1, board)
    add_deck_to_board(deck2, board)
    add_deck_to_board(deck3, board)

    return board

def delete_deck(board: dict, deck_name: str) -> bool:
    """Deleta a deck in a board

    Args:
        board (dict): The board containing the list of decks
        deck_name (str): The name of the deck to delete

    Returns:
        bool: True if a deck was removed during the operation, False otherwise.
    """
    
    for idx in range(len(board["deck_list"])):
        deck = board["deck_list"][idx]
        if deck["name"] == deck_name:
            del board["deck_list"][idx]
            return True
    else:
        return False


def add_deck_to_board(deck: dict, board: dict):
    """Add the deck 'deck' to the board havin the name 'board_name'
    Return True if the deck is added, otherwise return False

    Args:
        deck (dict): The deck to be added
        board (dict): The board that will host the deck
    """
    board["deck_list"].append(deck)


def display_board(board:dict) -> None :
    """Display the content of the board

    Args:
        board (dict): The board
    """
    print(board["name"])
    print(board["description"])
    for deck in board["deck_list"]:
        print(deck)


def main():
    board_test = create_board("board test","Example of a board for test purpose.")
    display_board(board_test)

    deckA = d.create_deck("deck A", "Example A.","board test")
    deckB = d.create_deck("deck B", "Example B.","board test")
    deckC = d.create_deck("deck C", "Example C.","board test")

    add_deck_to_board(deckA, board_test)
    display_board(board_test)
    add_deck_to_board(deckB, board_test)
    display_board(board_test)
    add_deck_to_board(deckC, board_test)
    display_board(board_test)

    print(delete_deck(board_test, "deck A"))
    display_board(board_test)


if __name__ == "__main__":
    main()