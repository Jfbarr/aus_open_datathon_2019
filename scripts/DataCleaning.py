import numpy as np

# Function to replace "." with NaN in a dataframe
def replaceMissingWithNaN(dataFrame):
    for column in list(dataFrame.columns.values):
        if (dataFrame[column].dtype.name == 'object'):
            # Different encodings for none in the database
            dataFrame[column] = dataFrame[column].replace({".":np.nan})


# Function to replace "." and NaN with 0 in a slice
def replaceMissingWithZero(sliceDF):
    # Different encodings for none in the database
    sliceDF = sliceDF.replace({np.nan:0})
    return sliceDF



# Encodes the variables fed into the functions as catagorical, boolean and numeric
# preseving missing data if specified, changin to zeros otherwise
def changeDataTypes(dataFrame, catagorical, boolean, numeric):
    for variable in list(dataFrame.columns.values):
        if variable in catagorical:
            dataFrame[variable] = dataFrame[variable].astype('category')
        elif variable in boolean:
            dataFrame[variable] = dataFrame[variable].astype('bool')
        elif variable in numeric:
            # Keep as a float as can't save variables as ints and keep NaNs
            dataFrame[variable] = dataFrame[variable].astype('float64')
        else:
            # Replaces missing with zeros and then saves as integers
            dataFrame[variable] = replaceMissingWithZero(dataFrame[variable])
            dataFrame[variable] = dataFrame[variable].astype('int64')    