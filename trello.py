import boards as b


def delete_board(board_name: str, trello: list) -> bool:
    """_summary_

    Args:
        board_name (str): _description_
        trello (list): _description_

    Returns:
        bool: _description_
    """
    for board in trello:
        print(f"board : {board}")
        if board["name"] == board_name:
            print("je dois effacer")
            del(board)
            return True
        else :
            return False


def create_trello() -> list:
    trello =  list()
    board_name_1 = "ma board numero 1"
    board_description_1 = "description de ma board numero 1"
    board_name_2 = "ma board numero 2"
    board_description_2 = "description de ma board numero 2"
    board_name_3 = "ma bord numero 3"
    board_description_3 = "description de ma board numero 3"
    trello.append(b.create_board(board_name_1, board_description_1))
    trello.append(b.create_board(board_name_2, board_description_2))
    trello.append(b.create_board(board_name_3, board_description_3))
    return trello


def main():
    pass


if __name__ == "__main__":
    main()