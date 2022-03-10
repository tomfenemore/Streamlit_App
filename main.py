import pandas as pd

import trelloAPI
import pandas


if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)

    df = trelloAPI.board()

    print(df['Notes'].head())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
