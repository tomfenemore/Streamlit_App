from trello import TrelloClient
import sys
sys.path.insert(1, '/Users/tomfenemore/PycharmProjects/pythonProject1')
import seecrets
import pandas as pd

def board():
    key = seecrets.key
    token = seecrets.token


    trello = TrelloClient(key, token)
    boards = trello.list_boards()
    board = trello.get_board(boards[0].id)
    cards = board.all_cards()

    dff = pd.DataFrame(dtype="category")
    #print(df)
    for card in cards:
        l = card.get_list()
        li=l.name
        labs = card.labels
        dct = {'ID': card.id, 'Wind': li, 'Venue': labs[0].name, 'Direction': card.description, 'Notes': card.comments}
        dff = dff.append(dct,  ignore_index=True)
    dff.to_pickle('code/pic')
    return dff








