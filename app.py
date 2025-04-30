import boards as b
import cards as c
import lists as l

board_list = get_list
trello =  list()


def delete_board(board_name: str, trello: list) -> bool:
    for board in board_list:
        if board["name"] == board_name:
            del(board)
            return True
        else :
            return False


def main():
    pass

if __name__ == "__main__":
    main()