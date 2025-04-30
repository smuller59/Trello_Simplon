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


def add_deck_to_board(deck: dict, board: dict):
    """Add the deck 'deck' to the board havin the name 'board_name'
    Return True if the deck is added, otherwise return False

    Args:
        deck (dict): The deck to be added
        board (dict): The board that will host the deck
    """
    board["deck_list"].append(deck)


def main():
    board_test = create_board("board test","Example of a board for test purpose.")
    print(board_test)

    deck_test = d.create_deck("test deck", "Example of a deck for test purpose.","board test")

    print(add_deck_to_board(deck_test, "test board"))
    print(board_test)

    print(add_deck_to_board(deck_test, "board test"))
    print(board_test)

if __name__ == "__main__":
    main()