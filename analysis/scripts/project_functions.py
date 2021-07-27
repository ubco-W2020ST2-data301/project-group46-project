import pandas as pd
import numpy as np

def changeStateToInt(state):
        if state == 'failed':
            return 0
        elif state == 'successful':
            return 1
        elif state == 'canceled':
            return 2
        elif state == 'live':
            return 3
        elif state == 'undefined':
            return 4
        elif state == 'suspended':
            return 5
        else:
            return -1

def load_and_process(url_or_path_to_csv_file):
        
        #np.where(x.state == 'successful', 1, 0)
        
        # Main Method Chain For Data Analysis Pipeline
        dataFrame = (pd.read_csv(url_or_path_to_csv_file, nrows=1000)
                    .rename(columns={"name": "Name"})
                    .assign(stateInt=lambda x: x['state'].apply(changeStateToInt))
                    .assign(duration=lambda x: (pd.to_datetime(x['deadline']) - pd.to_datetime(x['launched'])))
                    .assign(percentFunded=lambda x: (x['usd_pledged_real']/x['usd_goal_real']*100))
                    .assign(durationInt=lambda x: x['duration'].dt.days)
                    .drop(['ID', 'usd pledged', 'goal'], axis=1)
                    .dropna())
        # Pipeline explanation:
        # read_csv: Creates a DataFram from the Kickstarter Project data csv file from the path given to the function
        # rename: Renames the columns so that they are easier to read
        # assign 1: creates a new column in the dataframe called 'stateInt' which is a mapping of the state columns values of
                  # successful/failure to integer values of 0 and 1 so that graphs can be made.
        # assign 2: Creates a new column called 'duration' which is the duration of each Kickstarter project.
                  # This is calculated by the difference between the 'launched' date and the 'deadline' date
        # assign 3: Creates a new column called 'percentFunded' to measure how close a project was to their funding goal. 
        # assign 4: Creates a new columns from the 'duration' column but has changed the type to int so that analysis can be
                    # done where numeric values are needed
                    # Referenced for help on converting date_time column to int column:
                    # https://stackoverflow.com/questions/25646200/python-convert-timedelta-to-int-in-a-dataframe
        # drop: Drops the columns that are not used in the data analysis
        # dropna: Drops the rows in the dataset that have a NaN value
        
        
        # For help of creating the 'duration' column: 
        # https://www.geeksforgeeks.org/convert-the-column-type-from-string-to-datetime-format-in-pandas-dataframe/
        # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html
        
        
        return dataFrame
                     
        # pandas functions reference:
        # drop: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html?highlight=drop#pandas.DataFrame.drop
        # dropna: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html?highlight=dropna#pandas.DataFrame.dropna
        # apply: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.apply.html?highlight=apply#pandas.Series.apply
        # assign: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.assign.html?highlight=assign#pandas.DataFrame.assign
