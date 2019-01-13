import pandas as pd

# Create dataframes for lossing and winner player stats
# for each game
def summariseLifetimePlayerStats(DF, stats):
    winnerDF = DF.loc[:, DF.columns.str.startswith('Winner')]
    loserDF = DF.loc[:, DF.columns.str.startswith('Loser')]
    # Drop Ranks
    winnerDF = winnerDF.drop('Winner_Rank', axis = 1)
    loserDF = loserDF.drop('Loser_Rank', axis = 1)
    
    # Rename Variables
    winnerDF.columns = ['Player'] + stats
    loserDF.columns = ['Player'] + stats
    
    # Combine winners and losers into a single DF
    combinedDF = pd.concat([winnerDF, loserDF])
    # Group by unique player names
    combinedDF = combinedDF.groupby(['Player'])

    # Calculate tournament summary statistics
    statsToSum = {x:'sum' for x in stats}
    combinedDF = combinedDF[stats].agg(statsToSum)
    
    return combinedDF


# Create dataframes for lossing and winner player stats
# for each game 
def summarisePlayerTournStats(DF, stats):
    # Drop Winners/losers, ranks, retirement indicator and date
    winnerDF = DF.drop(['Loser', 'Loser_Rank', 'Winner_Rank', \
                        'Retirement_Ind', 'Tournament_Date', \
                        'Round_Description'], axis = 1)
    loserDF = DF.drop(['Winner', 'Loser_Rank', 'Winner_Rank', \
                       'Retirement_Ind', 'Tournament_Date', \
                       'Round_Description'], axis = 1)
    # Rename winner/loser to player
    winnerDF.columns.values[0] = "Player" 
    loserDF.columns.values[0] = "Player"
    # Find the remainin columns that need to be dropped
    dropFromWinner = winnerDF.loc[:, winnerDF.columns.str.startswith('Loser')].columns
    dropFromLoser = loserDF.loc[:, loserDF.columns.str.startswith('Winner')].columns
    # Drop the columns
    winnerDF = winnerDF.drop(dropFromWinner, axis = 1)
    loserDF = loserDF.drop(dropFromLoser, axis = 1)
    
    # Rename Variables
    winnerDF.columns = ['Player', 'Tournament', 'Court_Surface'] + stats
    loserDF.columns = ['Player', 'Tournament', 'Court_Surface'] + stats
    
    # Combine winners and losers into a single DF
    combinedDF = pd.concat([winnerDF, loserDF])
    # Group by unique player names
    combinedDF = combinedDF.groupby(['Player', 'Tournament', \
                                    'Court_Surface'])

    # Calculate tournament summary statistics
    statsToSum = {x:'sum' for x in stats}
    combinedDF = combinedDF[stats].agg(statsToSum)
    
    return combinedDF


# Create dataframes for lossing and winner player stats
# for each game  
def summarisePlayerSurfaceStats(DF, stats):

    # Drop Winners/losers, ranks, retirement indicator and date
    winnerDF = DF.drop(['Loser', 'Loser_Rank', 'Winner_Rank', \
                        'Retirement_Ind', 'Tournament_Date', \
                        'Round_Description', 'Tournament'],
                         axis = 1)
    loserDF = DF.drop(['Winner', 'Loser_Rank', 'Winner_Rank', \
                       'Retirement_Ind', 'Tournament_Date', \
                       'Round_Description', 'Tournament'],
                       axis = 1)
    # Rename winner/loser to player
    winnerDF.columns.values[0] = "Player" 
    loserDF.columns.values[0] = "Player"
    # Find the remainin columns that need to be dropped
    dropFromWinner = winnerDF.loc[:, winnerDF.columns.str.startswith('Loser')].columns
    dropFromLoser = loserDF.loc[:, loserDF.columns.str.startswith('Winner')].columns
    # Drop the columns
    winnerDF = winnerDF.drop(dropFromWinner, axis = 1)
    loserDF = loserDF.drop(dropFromLoser, axis = 1)
    
    # Rename Variables
    winnerDF.columns = ['Player', 'Court_Surface'] + stats
    loserDF.columns = ['Player', 'Court_Surface'] + stats
    
    # Combine winners and losers into a single DF
    combinedDF = pd.concat([winnerDF, loserDF])
    # Group by unique player names
    combinedDF = combinedDF.groupby(['Player', 'Court_Surface'])

    # Calculate tournament summary statistics
    statsToSum = {x:'sum' for x in stats}
    combinedDF = combinedDF[stats].agg(statsToSum)
    
    return combinedDF

# Creates new columns relating to serve stats
def addServeStatistics(lifetimeDF):
    # Total Serves Won
    lifetimeDF = lifetimeDF.assign(Total_Serves_Won = 
                         lifetimeDF['Total_FirstServes_Won'] +
                         lifetimeDF['Total_SecondServes_Won'])
    # Total serves
    lifetimeDF = lifetimeDF.assign(Total_Serves = 
                         lifetimeDF['Total_FirstServes_In'] +
                         lifetimeDF['Total_SecondServes_In'] +
                         lifetimeDF['Total_DoubleFaults'])
    # Probability of winning a serve
    lifetimeDF = lifetimeDF.assign(P_Win_Serve = 
                         lifetimeDF['Total_Serves_Won'] /
                         lifetimeDF['Total_Serves'])
    return lifetimeDF