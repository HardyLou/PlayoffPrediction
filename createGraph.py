# Find correlation between PER and where each player's team makes 
# it (First Round, Conference Semifinals, etc.)

import csv
from csv import reader
from collections import defaultdict

teamToRound = defaultdict(int)
teamToRound['BOS'] = 4
teamToRound['LAL'] = 4
teamToRound['ORL'] = 3
teamToRound['PHO'] = 3
teamToRound['CLE'] = 2
teamToRound['ATL'] = 2
teamToRound['UTA'] = 2
teamToRound['SAS'] = 2
teamToRound['CHI'] = 1
teamToRound['MIA'] = 1
teamToRound['MIL'] = 1
teamToRound['NOH'] = 1
teamToRound['CHA'] = 1
teamToRound['OKL'] = 1
teamToRound['DEN'] = 1
teamToRound['POR'] = 1
teamToRound['DAL'] = 1

x = list()
y = list()
# Open file for player statistics 
infile = open('playerData/players2010.csv', 'r')

for l in reader(infile): 
	# Ignore the header
	if l[0] == "name":
		continue

	name,per,team = l[0],l[1],l[2]

	print per
	print team, teamToRound[team]

	x.append(per)
	y.append(teamToRound[team])

i = 0
print "x = [", 
while i < len(x):
	print x[i],
	print ",",
	i += 1
print "]"

i = 0
print "y = [",
while i < len(y):
	print y[i],
	print ",",
	i += 1
print "]"

##### Information received above

trace0 = Scatter(
	x = [ 10.9 , 18.2 , 15.2 , 14.4 , 15.8 , 22.2 , 10.2 , 18.7 , 13.3 , 12.3 , 11.2 , 12.8 , 15.5 , 13.6 , 11.1 , 14.3 , 16.1 , 12.6 , 7.9 , 12.7 , 20.2 , 17.7 , 11.2 , 17.6 , 7.7 , 20.7 , 14.9 , 13.7 , 21.3 , 25.0 , 12.9 , 15.7 , 12.1 , 12.8 , 16.0 , 12.4 , 21.9 , 14.1 , 13.5 , 10.7 , 20.2 , 13.8 , 16.5 , 18.3 , 17.1 , 13.0 , 10.7 , 12.5 , 13.7 , 16.5 , 13.1 , 13.9 , 18.4 , 16.8 , 14.0 , 9.6 , 11.5 , 16.1 , 12.5 , 12.8 , -3.7 , 11.5 , 14.8 , 13.6 , 10.7 , 24.7 , 13.1 , 26.2 , 9.6 , 16.7 , 5.5 , 11.4 , 12.3 , 15.2 , 13.1 , 9.7 , 13.0 , 13.4 , 9.6 , 15.0 , 10.5 , 12.4 , 19.3 , 22.9 , 16.2 , 16.2 , 13.8 , 9.2 , 12.1 , 16.9 , 18.0 , 14.1 , 13.9 , 10.6 , 16.6 , 12.8 , 11.6 , 5.2 , 14.6 , 16.8 , 16.2 , 7.2 , 6.5 , 13.8 , 11.7 , 9.7 , 16.1 , 16.1 , 15.2 , 18.9 , 14.7 , 14.0 , 15.0 , 12.3 , 11.0 , 19.4 , 10.5 , 12.7 , 13.2 , 17.8 , 11.9 , 11.6 , 13.4 , 5.5 , 31.1 , 5.5 , 16.7 , 13.1 , 9.8 , 10.1 , 13.9 , 12.3 , 16.7 , 12.4 , 10.8 , 1.4 , 16.5 , 8.4 , 18.2 , 13.9 , 12.8 , 16.0 , 7.2 , 12.8 , 22.2 , 14.0 , 12.8 , 17.6 , 15.5 , 20.3 , 9.4 , 9.0 , 17.0 , 12.3 , 14.0 , 11.7 , 11.8 , 12.2 , 17.0 , 12.8 , 12.9 , 13.9 , 11.9 , 19.6 , 11.2 , 0.7 , 11.7 , 15.5 , 16.0 , 11.1 , 8.3 , 9.9 , 17.9 , 5.7 , 16.5 , 15.6 , 7.0 , 8.9 , 16.4 , 23.7 , 5.4 , 9.3 , 11.9 , 8.7 , 10.2 , 11.2 , 10.3 , 6.5 , 12.9 , 17.7 , 16.3 , 18.6 , 3.0 , 9.6 , 4.8 , 17.6 , 3.6 , 9.8 , 12.9 , 8.0 , 15.0 , 10.6 , 11.6 , 17.6 , 11.1 , 22.6 , 15.6 , 7.5 , 12.9 , 15.1 , 11.8 , 12.1 , 7.8 , 13.4 , 9.6 , 12.2 , 16.0 , 11.4 , 14.6 , 18.3 , 13.1 , 9.7 , 15.7 , 10.9 , 10.7 , 12.9 , 18.9 , 13.8 , 9.9 , 25.9 , 5.9 , 12.9 , 8.2 , 10.6 , 16.1 , 16.1 , 12.1 , 8.6 , 14.5 , 11.8 , 13.0 , 14.0],
	y = [ 1 , 1 , 4 , 3 , 1 , 1 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 3 , 0 , 1 , 1 , 0 , 1 , 2 , 1 , 2 , 1 , 0 , 2 , 1 , 2 , 0 , 2 , 0 , 0 , 0 , 0 , 2 , 0 , 4 , 4 , 0 , 0 , 0 , 4 , 0 , 0 , 0 , 3 , 0 , 1 , 1 , 0 , 1 , 0 , 0 , 2 , 0 , 0 , 1 , 0 , 1 , 1 , 0 , 1 , 0 , 0 , 3 , 3 , 0 , 2 , 0 , 0 , 0 , 0 , 2 , 0 , 4 , 1 , 1 , 4 , 0 , 0 , 0 , 3 , 0 , 4 , 0 , 4 , 0 , 2 , 1 , 2 , 0 , 1 , 0 , 0 , 3 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 2 , 1 , 2 , 3 , 1 , 0 , 0 , 2 , 3 , 1 , 0 , 0 , 2 , 1 , 0 , 1 , 2 , 0 , 0 , 2 , 0 , 1 , 0 , 0 , 0 , 2 , 0 , 0 , 0 , 1 , 2 , 0 , 0 , 0 , 1 , 0 , 0 , 3 , 0 , 0 , 0 , 0 , 1 , 1 , 2 , 2 , 0 , 0 , 1 , 2 , 2 , 1 , 1 , 0 , 2 , 2 , 0 , 0 , 3 , 3 , 1 , 0 , 1 , 1 , 2 , 4 , 1 , 2 , 2 , 2 , 2 , 1 , 4 , 4 , 3 , 1 , 0 , 0 , 3 , 3 , 1 , 1 , 4 , 1 , 1 , 0 , 1 , 1 , 0 , 0 , 0 , 0 , 1 , 2 , 1 , 0 , 1 , 3 , 0 , 1 , 1 , 0 , 0 , 1 , 0 , 0 , 0 , 2 , 0 , 1 , 0 , 1 , 4 , 1 , 0 , 0 , 1 , 0 , 1 , 2 , 0 , 0 , 2 , 3 , 0 , 2 , 2 , 0 , 4 , 0 , 1 , 0 , 0 ],   
	mode='markers'
)

layout = Layout(
    title='2010 PER to Rounds Met',
    xaxis=XAxis(
        title='PER',
        showgrid=False,
        zeroline=False
    ),
    yaxis=YAxis(
        title='Rounds',
        showline=False
    )
)

data = Data([trace0])
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='line-style')
#unique_url = py.plot(data, filename = 'basic-line')