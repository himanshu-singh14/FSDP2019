# -*- coding: utf-8 -*-
"""
Created on Wed May 22 18:13:15 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    URL shortening service Bitly
  Filename: 
    bitly.py
  Problem Statement:
    (usagov_bitly_data.json)
    In 2011, URL shortening service Bitly partnered with the US government website
    USA.gov to provide a feed of anonymous data gathered from users who shorten links
    ending with .gov or .mil. 
    In 2011, a live feed as well as hourly snapshots were available
    as downloadable text files. 
    This service is shut down at the time of this writing (2017),
    but we preserved one of the data files.
    In the case of the hourly snapshots, each line in each file contains a common form of
    web data known as JSON. (Use usagov_bitly_data.txt file from Resources)

    Replace the 'nan' values with 'Mising' and ' ' values with 'Unknown' keywords
    Print top 10 most frequent time-zones from the Dataset i.e. 'tz', with and without Pandas
    Count the number of occurrence for each time-zone
    Plot a bar Graph to show the frequency of top 10 time-zones (using Seaborn)
    From field 'a' which contains browser information and separate out browser capability(i.e. the first token in the string eg. Mozilla/5.0)
    Count the number of occurrence for separated browser capability field and plot bar graph for top 5 values (using Seaborn)
    Add a new Column as 'os' in the dataset, separate users by 'Windows' for the values in  browser information column i.e. 'a' that contains "Windows" and "Not Windows" for those who don't

Hint:
    http://1usagov.measuredvoice.com/2011/
    
"""

import pandas as pd
import numpy as np
from collections import Counter
import seaborn as sns

df = pd.read_json('material/usagov_bitly_data.json', lines = True)

# Replace the 'nan' values with 'Mising' and ' ' values with 'Unknown' keywords

df = df.replace([np.nan, ''],['Missing', 'Unknown'])

# Print top 10 most frequent time-zones from the Dataset i.e. 'tz', with Pandas

df['tz'].value_counts().head(10)

# Print top 10 most frequent time-zones from the Dataset i.e. 'tz', without Pandas

Counter(df['tz']).most_common(10)

# Count the number of occurrence for each time-zone

uniq_tz = df['tz'].value_counts()

# Plot a bar Graph to show the frequency of top 10 time-zones (using Seaborn)

sns.barplot(x = uniq_tz.index[0:11], y = uniq_tz[0:11])

# From field 'a' which contains browser information and separate out browser
# capability(i.e. the first token in the string eg. Mozilla/5.0)

#splitted_df = df['a'].apply(lambda x: x.split()[0])
splitted_df = df['a'].str.split(n=1,expand = True)


# Count the number of occurrence for separated browser capability field 
# and plot bar graph for top 5 values (using Seaborn)

uniq_browser = splitted_df[0].value_counts()[0:5]
sns.barplot(x = uniq_browser.index, y = uniq_browser)

# Add a new Column as 'os' in the dataset, separate users by 'Windows' for 
# the values in  browser information column i.e. 'a' that contains "Windows" 
# and "Not Windows" for those who don't

df['os'] = df['a'].apply(lambda x: 'Windows' if 'Windows' in x.replace('(', '').split() else 'Not Windows')
