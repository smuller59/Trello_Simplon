import boards as b
import cards as c
import decks as d

trello =  list()


def delete_board(board_name: str, trello: list) -> bool:
    """_summary_

    Args:
        board_name (str): _description_
        trello (list): _description_

    Returns:
        bool: _description_
    """
    for board in trello:
        if board["name"] == board_name:
            del(board)
            return True
        else :
            return False


def main():
    pass

if __name__ == "__main__":
    main()