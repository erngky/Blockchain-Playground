import pandas as pd
import numpy as np
#dataset
data = {
    "Team": ["ARI","ARI","ARI","ARI","ARI"],
    "League": ["NL","NL","NL","NL","NL"],
    "Year": [2012,2011,2010,2009,2008],
    "RS": [651,610,587,636,735],
    "RA": [674,712,866,768,884],
    "W" : [79,72,57,62,67],
    "G" : [162,162,162,161,162],
    "Playoffs": [0,1,0,0,0]
}

#convert to pandas dataframe
df = pd.DataFrame(data)
print(df.head)

#win rate calculater func
def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)

#win percentage Series 
win_percs = df.apply(lambda row: calc_win_perc(row['W'], row['G']), axis=1)
print(win_percs, '\n')

# Append a new column to df
df['WP'] = win_percs
print(df, '\n')

# Display df where WP is greater than 0.40
print(df[df['WP'] >= 0.40])




