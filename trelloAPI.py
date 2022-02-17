from trello import TrelloClient
import secrets
import pandas as pd

def board():
    key = secrets.key
    token = secrets.token


    trello = TrelloClient(key, token)
    boards = trello.list_boards()
    board = trello.get_board(boards[0].id)
    lists = board.all_lists()
    #df = pd.DataFrame(columns=[lists, 'ID'])
    cards = board.all_cards()
    dff = pd.DataFrame()
    #print(df)
    for card in cards:
        l = card.get_list()
        li=l.name
        labs = card.labels
        dct = {'ID': card.id, li: 1}
        for lab in labs:
            dct[lab.name]=1
        dff = dff.append(dct, ignore_index=True)
    dff.to_pickle('pic')








