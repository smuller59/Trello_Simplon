import json
import trello as t


def main():
    trello = t.create_trello()
    print(trello)
    t.delete_board("ma board numero 1", trello)
    print(trello)
    trello_js = json.dumps(trello)
    # print(trello_js)


if __name__ == "__main__":
    main()