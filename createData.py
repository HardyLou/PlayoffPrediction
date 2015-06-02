### This file creates a csv file containing features
### to our predictor for the 1990 NBA season.

import gzip
import csv
from csv import reader
from collections import defaultdict
import operator
import collections



# Create dictionary of a team's full name and its abbreviation
# NOTE: If a team name has been changed, this dictionary will
# map its name to the franchise's current abbreviation!
# e.g. Vancouver Grizzlies -> "MEM"
alias = {}
alias['Cleveland Cavaliers'] = 'CLE'
alias['Orlando Magic'] = 'ORL'
alias['Los Angeles Lakers'] = 'LAL'
alias['Dallas Mavericks'] = 'DAL'
alias['Phoenix Suns'] = 'PHO'
alias['Atlanta Hawks'] = 'ATL'
alias['Denver Nuggets'] = 'DEN'
alias['Utah Jazz'] = 'UTA'
alias['Boston Celtics'] = 'BOS'
alias['Oklahoma City Thunder'] = 'OKC'
alias['Seattle SuperSonics'] = 'OKC'                  # no longer exists
alias['Portland Trail Blazers'] = 'POR'
alias['San Antonio Spurs'] = 'SAS'
alias['Miami Heat'] = 'MIA'
alias['Milwaukee Bucks'] = 'MIL'
alias['Charlotte Bobcats'] = 'CHA'                    # no longer exists
alias['Charlotte Hornets'] = 'CHA'
alias['Houston Rockets'] = 'HOU'
alias['Chicago Bulls'] = 'CHI'
alias['Memphis Grizzlies'] = 'MEM'
alias['Vancouver Grizzlies'] = 'MEM'                  # no longer exists
alias['Toronto Raptors'] = 'TOR'
alias['New Orleans Hornets'] = 'NOP'                  # no longer exists
alias['New Orleans/Oklahoma City Hornets'] = 'NOP'    # no longer exists
alias['New Orleans Pelicans'] = 'NOP'
alias['Indiana Pacers'] = 'IND'
alias['Los Angeles Clippers'] = 'LAC'
alias['San Diego Clippers'] = 'SDC'
alias['New York Knicks'] = 'NYK'
alias['Detroit Pistons'] = 'DET'
alias['Philadelphia 76ers'] = 'PHI'
alias['Golden State Warriors'] = 'GSW'
alias['Washington Wizards'] = 'WAS'                   # no longer exists
alias['Washington Bullets'] = 'WAS'
alias['Sacramento Kings'] = 'SAC'
alias['Minnesota Timberwolves'] = 'MIN'
alias['New Jersey Nets'] = 'BRK'                      # no longer exists
alias['Brooklyn Nets'] = 'BRK'

# Eastern Conference
dictMIL = defaultdict(list) # Bucks
dictCHI = defaultdict(list) # Bulls
dictCLE = defaultdict(list) # Cavaliers
dictBOS = defaultdict(list) # Celtics
dictATL = defaultdict(list) # Hawks
dictMIA = defaultdict(list) # Heat
dictCHA = defaultdict(list) # Hornets
dictNYK = defaultdict(list) # Knicks
dictORL = defaultdict(list) # Magic
dictBRK = defaultdict(list) # Nets
dictIND = defaultdict(list) # Pacers
dictDET = defaultdict(list) # Pistons
dictTOR = defaultdict(list) # Raptors
dictPHI = defaultdict(list) # Sixers
dictWAS = defaultdict(list) # Wizards

# Western Conference
dictPOR = defaultdict(list) # Blazers
dictLAC = defaultdict(list) # Clippers
dictMEM = defaultdict(list) # Grizzlies
dictNOP = defaultdict(list) # Hornets
dictUTA = defaultdict(list) # Jazz
dictSAC = defaultdict(list) # Kings
dictLAL = defaultdict(list) # Lakers
dictDAL = defaultdict(list) # Mavericks
dictDEN = defaultdict(list) # Nuggets
dictHOU = defaultdict(list) # Rockets
dictSAS = defaultdict(list) # Spurs
dictPHO = defaultdict(list) # Suns
dictOKC = defaultdict(list) # Thunder
dictMIN = defaultdict(list) # Timberwolves
dictGSW = defaultdict(list) # Warriors


### Open file containing player statistics for the 1990 season
infile = open('playerData/players1990.csv', 'r')

for l in reader(infile):
  # Ignore the header
  if l[0] == "name":
    continue

  name,per,team = l[0],l[1],l[2]

  # EASTERN CONFERENCE
  if team == "MIL":
    if len(dictMIL) < 3:                # Find the top 3 players in PER
      dictMIL[name] = float(per)
      dictMIL = collections.OrderedDict(sorted(dictMIL.items(), key=lambda x:x[1]))
    elif float(per) > dictMIL.values()[0]:
      dictMIL.pop(dictMIL.keys()[0])
      dictMIL[name] = float(per)
      dictMIL = collections.OrderedDict(sorted(dictMIL.items(), key=lambda x:x[1]))

  if team == "CHI":
    if len(dictCHI) < 3:                # Find the top 3 players in PER
      dictCHI[name] = float(per)
      dictCHI = collections.OrderedDict(sorted(dictCHI.items(), key=lambda x:x[1]))
    elif float(per) > dictCHI.values()[0]:
      dictCHI.pop(dictCHI.keys()[0])
      dictCHI[name] = float(per)
      dictCHI = collections.OrderedDict(sorted(dictCHI.items(), key=lambda x:x[1]))

  if team == "CLE":
    if len(dictCLE) < 3:                # Find the top 3 players in PER
      dictCLE[name] = float(per)
      dictCLE = collections.OrderedDict(sorted(dictCLE.items(), key=lambda x:x[1]))
    elif float(per) > dictCLE.values()[0]:
      dictCLE.pop(dictCLE.keys()[0])
      dictCLE[name] = float(per)
      dictCLE = collections.OrderedDict(sorted(dictCLE.items(), key=lambda x:x[1]))

  if team == "ATL":
    if len(dictATL) < 3:                # Find the top 3 players in PER
      dictATL[name] = float(per)
      dictATL = collections.OrderedDict(sorted(dictATL.items(), key=lambda x:x[1]))
    elif float(per) > dictATL.values()[0]:
      dictATL.pop(dictATL.keys()[0])
      dictATL[name] = float(per)
      dictATL = collections.OrderedDict(sorted(dictATL.items(), key=lambda x:x[1]))

  if team == "MIA":
    if len(dictMIA) < 3:                # Find the top 3 players in PER
      dictMIA[name] = float(per)
      dictMIA = collections.OrderedDict(sorted(dictMIA.items(), key=lambda x:x[1]))
    elif float(per) > dictMIA.values()[0]:
      dictMIA.pop(dictMIA.keys()[0])
      dictMIA[name] = float(per)
      dictMIA = collections.OrderedDict(sorted(dictMIA.items(), key=lambda x:x[1]))

  if team == "CHA" or team == "CHH":
    if len(dictCHA) < 3:                # Find the top 3 players in PER
      dictCHA[name] = float(per)
      dictCHA = collections.OrderedDict(sorted(dictCHA.items(), key=lambda x:x[1]))
    elif float(per) > dictCHA.values()[0]:
      dictCHA.pop(dictCHA.keys()[0])
      dictCHA[name] = float(per)
      dictCHA = collections.OrderedDict(sorted(dictCHA.items(), key=lambda x:x[1]))

  if team == "NYK":
    if len(dictNYK) < 3:                # Find the top 3 players in PER
      dictNYK[name] = float(per)
      dictNYK = collections.OrderedDict(sorted(dictNYK.items(), key=lambda x:x[1]))
    elif float(per) > dictNYK.values()[0]:
      dictNYK.pop(dictNYK.keys()[0])
      dictNYK[name] = float(per)
      dictNYK = collections.OrderedDict(sorted(dictNYK.items(), key=lambda x:x[1]))

  if team == "BOS":
    if len(dictBOS) < 3:                # Find the top 3 players in PER
      dictBOS[name] = float(per)
      dictBOS = collections.OrderedDict(sorted(dictBOS.items(), key=lambda x:x[1]))
    elif float(per) > dictBOS.values()[0]:
      dictBOS.pop(dictBOS.keys()[0])
      dictBOS[name] = float(per)
      dictBOS = collections.OrderedDict(sorted(dictBOS.items(), key=lambda x:x[1]))

  if team == "ORL":
    if len(dictORL) < 3:                # Find the top 3 players in PER
      dictORL[name] = float(per)
      dictORL = collections.OrderedDict(sorted(dictORL.items(), key=lambda x:x[1]))
    elif float(per) > dictORL.values()[0]:
      dictORL.pop(dictORL.keys()[0])
      dictORL[name] = float(per)
      dictORL = collections.OrderedDict(sorted(dictORL.items(), key=lambda x:x[1]))

  if team == "BRK" or team == "NJN":
    if len(dictBRK) < 3:                # Find the top 3 players in PER
      dictBRK[name] = float(per)
      dictBRK = collections.OrderedDict(sorted(dictBRK.items(), key=lambda x:x[1]))
    elif float(per) > dictBRK.values()[0]:
      dictBRK.pop(dictBRK.keys()[0])
      dictBRK[name] = float(per)
      dictBRK = collections.OrderedDict(sorted(dictBRK.items(), key=lambda x:x[1]))

  if team == "IND":
    if len(dictIND) < 3:                # Find the top 3 players in PER
      dictIND[name] = float(per)
      dictIND = collections.OrderedDict(sorted(dictIND.items(), key=lambda x:x[1]))
    elif float(per) > dictIND.values()[0]:
      dictIND.pop(dictIND.keys()[0])
      dictIND[name] = float(per)
      dictIND = collections.OrderedDict(sorted(dictIND.items(), key=lambda x:x[1]))

  if team == "DET":
    if len(dictDET) < 3:                # Find the top 3 players in PER
      dictDET[name] = float(per)
      dictDET = collections.OrderedDict(sorted(dictDET.items(), key=lambda x:x[1]))
    elif float(per) > dictDET.values()[0]:
      dictDET.pop(dictDET.keys()[0])
      dictDET[name] = float(per)
      dictDET = collections.OrderedDict(sorted(dictDET.items(), key=lambda x:x[1]))

  if team == "TOR":
    if len(dictTOR) < 3:                # Find the top 3 players in PER
      dictTOR[name] = float(per)
      dictTOR = collections.OrderedDict(sorted(dictTOR.items(), key=lambda x:x[1]))
    elif float(per) > dictTOR.values()[0]:
      dictTOR.pop(dictTOR.keys()[0])
      dictTOR[name] = float(per)
      dictTOR = collections.OrderedDict(sorted(dictTOR.items(), key=lambda x:x[1]))

  if team == "PHI":
    if len(dictPHI) < 3:                # Find the top 3 players in PER
      dictPHI[name] = float(per)
      dictPHI = collections.OrderedDict(sorted(dictPHI.items(), key=lambda x:x[1]))
    elif float(per) > dictPHI.values()[0]:
      dictPHI.pop(dictPHI.keys()[0])
      dictPHI[name] = float(per)
      dictPHI = collections.OrderedDict(sorted(dictPHI.items(), key=lambda x:x[1]))

  if team == "WAS" or team == "WSB":
    if len(dictWAS) < 3:                # Find the top 3 players in PER
      dictWAS[name] = float(per)
      dictWAS = collections.OrderedDict(sorted(dictWAS.items(), key=lambda x:x[1]))
    elif float(per) > dictWAS.values()[0]:
      dictWAS.pop(dictWAS.keys()[0])
      dictWAS[name] = float(per)
      dictWAS = collections.OrderedDict(sorted(dictWAS.items(), key=lambda x:x[1]))

  # WESTERN CONFERENCE
  if team == "POR":
    if len(dictPOR) < 3:                # Find the top 3 players in PER
      dictPOR[name] = float(per)
      dictPOR = collections.OrderedDict(sorted(dictPOR.items(), key=lambda x:x[1]))
    elif float(per) > dictPOR.values()[0]:
      dictPOR.pop(dictPOR.keys()[0])
      dictPOR[name] = float(per)
      dictPOR = collections.OrderedDict(sorted(dictPOR.items(), key=lambda x:x[1]))

  if team == "LAC" or team == "SDC":
    if len(dictLAC) < 3:                # Find the top 3 players in PER
      dictLAC[name] = float(per)
      dictLAC = collections.OrderedDict(sorted(dictLAC.items(), key=lambda x:x[1]))
    elif float(per) > dictLAC.values()[0]:
      dictLAC.pop(dictLAC.keys()[0])
      dictLAC[name] = float(per)
      dictLAC = collections.OrderedDict(sorted(dictLAC.items(), key=lambda x:x[1]))

  if team == "MEM" or team == "VAN":
    if len(dictMEM) < 3:                # Find the top 3 players in PER
      dictMEM[name] = float(per)
      dictMEM = collections.OrderedDict(sorted(dictMEM.items(), key=lambda x:x[1]))
    elif float(per) > dictMEM.values()[0]:
      dictMEM.pop(dictMEM.keys()[0])
      dictMEM[name] = float(per)
      dictMEM = collections.OrderedDict(sorted(dictMEM.items(), key=lambda x:x[1]))

  if team == "NOP" or team == "NOH" or team == "NOK":
    if len(dictNOP) < 3:                # Find the top 3 players in PER
      dictNOP[name] = float(per)
      dictNOP = collections.OrderedDict(sorted(dictNOP.items(), key=lambda x:x[1]))
    elif float(per) > dictNOP.values()[0]:
      dictNOP.pop(dictNOP.keys()[0])
      dictNOP[name] = float(per)
      dictNOP = collections.OrderedDict(sorted(dictNOP.items(), key=lambda x:x[1]))

  if team == "UTA":
    if len(dictUTA) < 3:                # Find the top 3 players in PER
      dictUTA[name] = float(per)
      dictUTA = collections.OrderedDict(sorted(dictUTA.items(), key=lambda x:x[1]))
    elif float(per) > dictUTA.values()[0]:
      dictUTA.pop(dictUTA.keys()[0])
      dictUTA[name] = float(per)
      dictUTA = collections.OrderedDict(sorted(dictUTA.items(), key=lambda x:x[1]))

  if team == "SAC":
    if len(dictSAC) < 3:                # Find the top 3 players in PER
      dictSAC[name] = float(per)
      dictSAC = collections.OrderedDict(sorted(dictSAC.items(), key=lambda x:x[1]))
    elif float(per) > dictSAC.values()[0]:
      dictSAC.pop(dictSAC.keys()[0])
      dictSAC[name] = float(per)
      dictSAC = collections.OrderedDict(sorted(dictSAC.items(), key=lambda x:x[1]))

  if team == "LAL":
    if len(dictLAL) < 3:                # Find the top 3 players in PER
      dictLAL[name] = float(per)
      dictLAL = collections.OrderedDict(sorted(dictLAL.items(), key=lambda x:x[1]))
    elif float(per) > dictLAL.values()[0]:
      dictLAL.pop(dictLAL.keys()[0])
      dictLAL[name] = float(per)
      dictLAL = collections.OrderedDict(sorted(dictLAL.items(), key=lambda x:x[1]))

  if team == "OKC" or team == "SEA":
    if len(dictOKC) < 3:                # Find the top 3 players in PER
      dictOKC[name] = float(per)
      dictOKC = collections.OrderedDict(sorted(dictOKC.items(), key=lambda x:x[1]))
    elif float(per) > dictOKC.values()[0]:
      dictOKC.pop(dictOKC.keys()[0])
      dictOKC[name] = float(per)
      dictOKC = collections.OrderedDict(sorted(dictOKC.items(), key=lambda x:x[1]))

  if team == "DAL":
    if len(dictDAL) < 3:                # Find the top 3 players in PER
      dictDAL[name] = float(per)
      dictDAL = collections.OrderedDict(sorted(dictDAL.items(), key=lambda x:x[1]))
    elif float(per) > dictDAL.values()[0]:
      dictDAL.pop(dictDAL.keys()[0])
      dictDAL[name] = float(per)
      dictDAL = collections.OrderedDict(sorted(dictDAL.items(), key=lambda x:x[1]))

  if team == "DEN":
    if len(dictDEN) < 3:                # Find the top 3 players in PER
      dictDEN[name] = float(per)
      dictDEN = collections.OrderedDict(sorted(dictDEN.items(), key=lambda x:x[1]))
    elif float(per) > dictDEN.values()[0]:
      dictDEN.pop(dictDEN.keys()[0])
      dictDEN[name] = float(per)
      dictDEN = collections.OrderedDict(sorted(dictDEN.items(), key=lambda x:x[1]))

  if team == "HOU":
    if len(dictHOU) < 3:                # Find the top 3 players in PER
      dictHOU[name] = float(per)
      dictHOU = collections.OrderedDict(sorted(dictHOU.items(), key=lambda x:x[1]))
    elif float(per) > dictHOU.values()[0]:
      dictHOU.pop(dictHOU.keys()[0])
      dictHOU[name] = float(per)
      dictHOU = collections.OrderedDict(sorted(dictHOU.items(), key=lambda x:x[1]))

  if team == "SAS":
    if len(dictSAS) < 3:                # Find the top 3 players in PER
      dictSAS[name] = float(per)
      dictSAS = collections.OrderedDict(sorted(dictSAS.items(), key=lambda x:x[1]))
    elif float(per) > dictSAS.values()[0]:
      dictSAS.pop(dictSAS.keys()[0])
      dictSAS[name] = float(per)
      dictSAS = collections.OrderedDict(sorted(dictSAS.items(), key=lambda x:x[1]))

  if team == "PHO":
    if len(dictPHO) < 3:                # Find the top 3 players in PER
      dictPHO[name] = float(per)
      dictPHO = collections.OrderedDict(sorted(dictPHO.items(), key=lambda x:x[1]))
    elif float(per) > dictPHO.values()[0]:
      dictPHO.pop(dictPHO.keys()[0])
      dictPHO[name] = float(per)
      dictPHO = collections.OrderedDict(sorted(dictPHO.items(), key=lambda x:x[1]))

  if team == "MIN":
    if len(dictMIN) < 3:                # Find the top 3 players in PER
      dictMIN[name] = float(per)
      dictMIN = collections.OrderedDict(sorted(dictMIN.items(), key=lambda x:x[1]))
    elif float(per) > dictMIN.values()[0]:
      dictMIN.pop(dictMIN.keys()[0])
      dictMIN[name] = float(per)
      dictMIN = collections.OrderedDict(sorted(dictMIN.items(), key=lambda x:x[1]))

  if team == "GSW":
    if len(dictGSW) < 3:                # Find the top 3 players in PER
      dictGSW[name] = float(per)
      dictGSW = collections.OrderedDict(sorted(dictGSW.items(), key=lambda x:x[1]))
    elif float(per) > dictGSW.values()[0]:
      dictGSW.pop(dictGSW.keys()[0])
      dictGSW[name] = float(per)
      dictGSW = collections.OrderedDict(sorted(dictGSW.items(), key=lambda x:x[1]))

# Dictionary that holds the sum of the PERs of the top 3 players
dictALL = {}
dictALL["DET"] = sum(dictDET.values())
dictALL["LAC"] = sum(dictLAC.values())
dictALL["TOR"] = sum(dictTOR.values())
dictALL["BRK"] = sum(dictBRK.values())
dictALL["SAS"] = sum(dictSAS.values())
dictALL["CHA"] = sum(dictCHA.values())
dictALL["POR"] = sum(dictPOR.values())
dictALL["MIL"] = sum(dictMIL.values())
dictALL["BOS"] = sum(dictBOS.values())
dictALL["UTA"] = sum(dictUTA.values())
dictALL["HOU"] = sum(dictHOU.values())
dictALL["ORL"] = sum(dictORL.values())
dictALL["PHO"] = sum(dictPHO.values())
dictALL["DEN"] = sum(dictDEN.values())
dictALL["MIA"] = sum(dictMIA.values())
dictALL["WAS"] = sum(dictWAS.values())
dictALL["LAL"] = sum(dictLAL.values())
dictALL["NOP"] = sum(dictNOP.values())
dictALL["MEM"] = sum(dictMEM.values())
dictALL["OKC"] = sum(dictOKC.values())
dictALL["GSW"] = sum(dictGSW.values())
dictALL["DAL"] = sum(dictDAL.values())
dictALL["IND"] = sum(dictIND.values())
dictALL["ATL"] = sum(dictATL.values())
dictALL["SAC"] = sum(dictSAC.values())
dictALL["PHI"] = sum(dictPHI.values())
dictALL["MIN"] = sum(dictMIN.values())
dictALL["NYK"] = sum(dictNYK.values())
dictALL["CHI"] = sum(dictCHI.values())
dictALL["CLE"] = sum(dictCLE.values())
#dictALL = collections.OrderedDict(sorted(dictALL.items(), key=lambda x:x[1]))


# Dictionary mapping a team to its win percentage in the regular season
dictWinPercentage = {}
with open('teamData/teamstats_1990.csv', 'r') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  for row in reader:
    # Ignore the header
    if row[0] == "srs":
      continue
    srs,ratio,team = row[0],row[1],row[2]
    dictWinPercentage[alias[team]] = ratio


# Dictionary showing winner of regular season series between a pair of teams,
# in terms of the team listed first in the pair.
# e.g. for (Tm1, Tm2)
#   Tm1 won = 1
#   Tm2 won = -1
#   tie = 0
dictSeasonResults = {}
with open('seasonData/seasongames_1990.csv', 'r') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  for row in reader:
    if row[0] == "team2Score":
      continue
    tm2pts,tm1pts,tm1,tm2 = row[0], row[1], row[2], row[3]
    tm1 = alias[tm1]
    tm1pts = int(tm1pts)
    tm2 = alias[tm2]
    tm2pts = int(tm2pts)
    if (tm1,tm2) in dictSeasonResults:
      if tm1pts > tm2pts:
        dictSeasonResults[tm1,tm2] += 1
      else:
        dictSeasonResults[tm1,tm2] -= 1
    elif (tm2,tm1) in dictSeasonResults:
      if tm2pts > tm1pts:
        dictSeasonResults[tm2,tm1] += 1
      else:
        dictSeasonResults[tm2,tm1] -= 1
    else:
      if tm1pts > tm2pts:
        dictSeasonResults[tm1,tm2] = 1
      else:
        dictSeasonResults[tm1,tm2] = -1
for matchup in dictSeasonResults:
  if dictSeasonResults[matchup] > 0:
    dictSeasonResults[matchup] = 1
  elif dictSeasonResults[matchup] < 0:
    dictSeasonResults[matchup] = -1


# Dictionary showing winner of a playoffs matchup in terms of the team
# listed first.
# e.g. for (Tm1,Tm2)
#   Tm1 won = 1
#   Tm2 won = 0
dictPlayoffResults = {}
with open('playoffData/playoffgames_1990.csv', 'r') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  for row in reader:
    if row[0] == "team2Score":
      continue
    tm2pts,tm1pts,tm1,tm2 = row[0], row[1], row[2], row[3]
    tm1 = alias[tm1]
    tm1pts = int(tm1pts)
    tm2 = alias[tm2]
    tm2pts = int(tm2pts)
    if (tm1,tm2) in dictPlayoffResults:
      if tm1pts > tm2pts:
        dictPlayoffResults[tm1,tm2] += 1
      else:
        dictPlayoffResults[tm1,tm2] -= 1
    elif (tm2,tm1) in dictPlayoffResults:
      if tm2pts > tm1pts:
        dictPlayoffResults[tm2,tm1] += 1
      else:
        dictPlayoffResults[tm2,tm1] -= 1
    else:
      if tm1pts > tm2pts:
        dictPlayoffResults[tm1,tm2] = 1
      else:
        dictPlayoffResults[tm1,tm2] = -1
for matchup in dictPlayoffResults:
  if dictPlayoffResults[matchup] > 0:
    dictPlayoffResults[matchup] = 1
  else:
    dictPlayoffResults[matchup] = 0


# Write data to trainingdata_1990.csv
header = 0
data = open("trainingData/trainingdata_1990.csv", 'w')
for tm1,tm2 in dictPlayoffResults:
  if header == 0:
    #header
    header = 1
    data.write("tm1,tm1PER,tm1winPerc,tm2,tm2PER,tm2winPerc,seasonSeries,outcome\n")
  if (tm1,tm2) in dictSeasonResults:
    data.write(tm1 + "," + str(dictALL[tm1]) + "," + str(dictWinPercentage[tm1]) + "," + \
                      tm2 + "," + str(dictALL[tm2]) + "," + str(dictWinPercentage[tm2]) + "," + \
                      str(dictSeasonResults[tm1,tm2]) + "," + str(dictPlayoffResults[tm1,tm2]) + "\n")
  elif (tm2,tm1) in dictSeasonResults:
    data.write(tm1 + "," + str(dictALL[tm1]) + "," + str(dictWinPercentage[tm1]) + "," + \
                      tm2 + "," + str(dictALL[tm2]) + "," + str(dictWinPercentage[tm2]) + "," + \
                      str(-1*dictSeasonResults[tm2,tm1]) + "," + str(dictPlayoffResults[tm1,tm2]) + "\n")
  # Rare case that the teams never played in the regular season
  else:
    print tm1,
    print tm2
    data.write(tm1 + "," + str(dictALL[tm1]) + "," + str(dictWinPercentage[tm1]) + "," + \
                      tm2 + "," + str(dictALL[tm2]) + "," + str(dictWinPercentage[tm2]) + "," + \
                      "0" + "," + str(dictPlayoffResults[tm1,tm2]) + "\n")

data.close()