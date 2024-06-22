# Output "hello world" to the screen
print("hello world")

"""
Open the CSV file called "nfl_offensive_stats.csv" and read in the CSV data from the file
"""

import csv

nfl_offensive_stats = []
with open("nfl_offensive_stats.csv") as f:
    reader = csv.DictReader(f)
    # 打印列名以进行调试
    print("Column names are:", reader.fieldnames)
    for row in reader:
        nfl_offensive_stats.append(row)

"""
The 3rd column in data is player position, the fourth column is player name, 
and the 8th column is the passing yards.
For each player whose position in column 3 is "QB", 
determine the sum of yards from column 8.
"""

qb_passing_yards = {}
for player in nfl_offensive_stats:
    if player["position "] == "QB":  # 使用正确的列名 'position '
        player_name = player["player"]  # 使用正确的列名 'player'
        passing_yards = int(player["pass_yds"])  # 使用正确的列名 'pass_yds'
        if player_name in qb_passing_yards:
            qb_passing_yards[player_name] += passing_yards
        else:
            qb_passing_yards[player_name] = passing_yards

"""
Print the sum of passing yards sorted by sum of passing yards
in descending order
do not include tom brady because he wins too much
"""

sorted_qb_passing_yards = sorted(qb_passing_yards.items(), key=lambda x: x[1], reverse=True)
for player, yards in sorted_qb_passing_yards:
    if player != "Tom Brady":
        print(f"{player}: {yards}")
""""
plot the players by their number of passing yards
only for players with more than 4000 passing yards
"""

import matplotlib.pyplot as plt

players = [player for player, yards in sorted_qb_passing_yards if yards > 4000]
yards = [yards for player, yards in sorted_qb_passing_yards if yards > 4000]
plt.bar(players, yards)
plt.xticks(rotation=90)
plt.show()
