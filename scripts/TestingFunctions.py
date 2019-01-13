from scripts import MatchWinProbCalc as MWPC
from scripts.OutputGeneration import probability_return 

# Summarise testing data
def summariseTesting(DF):
    DF = DF[['Winner', 'Loser']]
    DF.columns = ['Player_1', 'Player_2']
    DF['Label'] = 1
    return DF



# Return the probabilities of player one winning in each match up
def predictProb(trainingDF, unknownDF, default_prob):
    predictions = list()
    for player_1, player_2 in zip(unknownDF['Player_1'], unknownDF['Player_2']):
        predictions.append(MWPC.match_win_2_of_3(
            probability_return(trainingDF, player_1, default_prob),
            probability_return(trainingDF, player_2, default_prob)))
            
    return predictions