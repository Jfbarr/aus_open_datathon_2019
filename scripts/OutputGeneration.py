from scripts import MatchWinProbCalc as MWPC
import numpy as np

""" If there is not data for a player, return default_prob as the probability they win a rally on their serve
    Note that the below function takes a summary_dataframe with an index of player names and a column title P_Win_Serve.
    Thus to change the probabilities being run through the model, we need only create a new dataframe of rally probabilities 
    indexed by player. These probabilities could be empirical lifetime averages, averages over the last tournament, averages over
    the court type to be used in the upcoming tournament, the result of bayesian inference etc.
"""
def probability_return(summary_dataframe, player, default_prob):
    try:
        if summary_dataframe.loc[player, 'P_Win_Serve'] != np.nan:
            result = summary_dataframe.loc[player, 'P_Win_Serve']
        else:
            result =  default_prob
    except:
        result =  default_prob
    return result


# Generates a DF that can be outputed to a CSV in a format approriate for submission

def generateOutputDF(DF, sampleSub, default_prob, matchType = 'twoOfThree'):
    indexes = list(sampleSub.index.values) 

    # Change probabilities in submission dataset to align with the developed model
    for x in indexes:
        if matchType == 'twoOfThree':
            sampleSub.at[x, 'player_1_win_probability'] = MWPC.match_win_2_of_3(
                probability_return(DF, sampleSub.loc[x, 'player_1'], default_prob) ,\
                probability_return(DF, sampleSub.loc[x, 'player_2'], default_prob))
        else:
            sampleSub.at[x, 'player_1_win_probability'] = MWPC.match_win_3_of_5(
                probability_return(DF, sampleSub.loc[x, 'player_1'], default_prob) ,\
                probability_return(DF, sampleSub.loc[x, 'player_2'], default_prob))
    
    return sampleSub

