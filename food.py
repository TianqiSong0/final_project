#This project aims to identify whether the percent of logistical losses for food has been decreased in 2006 and in 2011

#preperation: check on where the repository has been stored; and if the document has been stored in the same place
#import os
#print(os.getcwd())
#path = 'legumes.xlsx'
#if os.path.isfile(path):
#    print("yes")
#else:
#    print("no")
#%% #data part
import pandas as pd

#read the files and convert all sub-sheets into one dictionary, so that a key refers to a sub-sheet (dataframe); set the 
#second line as the header 
filelist = ['veg.xlsx']
raw_data = {} 
for f in filelist:
    fh = pd.read_excel(f,sheet_name=None, header=1, skiprows=[2,3,4,5], nrows=51)
    for k, v in fh.items():
        raw_data[k] = v
        
#drop the unneeded keys and those related values
del raw_data['TableOfContents']
del raw_data['Fresh vegetables']
del raw_data['Canned vegetables'] 
del raw_data['Frozen vegetables'] 
del raw_data['Total dehydrated vegetables']
del raw_data['Dry edible beans'] 
del raw_data['Legumes']
del raw_data['Vegetables']
                  
#check if the header has been changed 
#for k, v in raw_data.items():
#    print(v.columns.values)  
#%%
#refer all 'Loss from retail/ institutional to consumer level' columns by column 'Year'
refer = pd.DataFrame() 
for k, v in raw_data.items():
    refer[k] = v.set_index('Year')['Loss from retail/ institutional to consumer level']   

#drop canned, frozen, dehydrated and dry food whose logistic loss did not change over time
filter_ = ['Canned', 'canned', 'Frozen', 'frozen', 'Dehydrated', 'Dry', 'dry', 'Potato chips']
to_drop = []
for c in refer.columns:
    for word in filter_:
        if word in c:
            to_drop.append(c)
filtered = refer.drop(columns=to_drop)

#drop unavailable data (save 2006 and 2011 only)
#filtered = filtered.rename(index={2006: '1970-2006', 2011: '2011-2020'})
filtered_year = filtered.drop(index=[1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 
                                       1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 
                                       2000, 2001, 2002, 2003, 2004, 2005, 2007, 2008, 2009, 2010, 2012, 2013, 2014, 2015, 2016, 
                                       2017, 2018, 2019, 2020])
#filtered_year = filtered_year.transpose()#shortcut is .T

#%% #plots part
#import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 300

#use the trend of whether it decreased or increased and if the change rate is above 50% to be the threshold for spliting up data       
decreased_above50 = pd.DataFrame()
decreased_below50 = pd.DataFrame()
increased_above50 = pd.DataFrame()
increased_below50 = pd.DataFrame()

#for c in filtered_year.index:
#    if filtered_year.loc[c, 2006] > filtered_year.loc[c, 2011]:
#        if abs((filtered_year.loc[c, 2011] - filtered_year.loc[c, 2006]) / filtered_year.loc[c, 2011]) >= 0.5:
#            decreased_above50[c] = filtered_year[c]
#        else:
#            decreased_below50[c] = filtered_year[c]
#    else:
#        if abs((filtered_year.loc[c, 2011] - filtered_year.loc[c, 2011]) / filtered_year.loc[c, 2011]) >= 0.5:
#            increased_above50[c] = filtered_year[c]
#        else:
#            increased_below50[c] = filtered_year[c]

for c in filtered_year.columns:
    if filtered_year.loc[2006, c] > filtered_year.loc[2011, c]:
        if abs((filtered_year.loc[2011, c] - filtered_year.loc[2006, c]) / filtered_year.loc[2011, c]) >= 0.5:
            decreased_above50[c] = filtered_year[c]
        else:
            decreased_below50[c] = filtered_year[c]
    else:
        if abs((filtered_year.loc[2011, c] - filtered_year.loc[2006, c]) / filtered_year.loc[2006, c]) >= 0.5:
            increased_above50[c] = filtered_year[c]
        else:
            increased_below50[c] = filtered_year[c]

#transpose and sort values
decreased_above50 = decreased_above50.transpose()
decreased_below50 = decreased_below50.transpose()
increased_above50 = increased_above50.T
increased_below50 = increased_below50.T
decreased_above50 = decreased_above50.sort_values(by=2006, ascending=False)
decreased_below50 = decreased_below50.sort_values(by=2006, ascending=False)
increased_above50 = increased_above50.sort_values(by=2006, ascending=False)
increased_below50 = increased_below50.sort_values(by=2006, ascending=False)

#plots 
#decreased_above50 = decreased_above50.reindex(columns=decreased_above50.columns[::-1])
decreased_above50.plot(kind='barh')
#plt.gca().yaxis.set_label_coords(2, 0.3)
plt.grid(True)
plt.gca().invert_yaxis()
plt.title('% of loss from retail/institutional to consumers (decreased>=50%)')

decreased_below50.plot(kind='barh')
plt.grid(True)
plt.gca().invert_yaxis()
plt.title('% of loss from retail/institutional to consumers (decreased<50%)')

increased_above50.plot(kind='barh')
plt.grid(True)
plt.gca().invert_yaxis()
plt.title('% of loss from retail/institutional to consumers (increased>=50%)')

increased_below50.plot(kind='barh')
plt.grid(True)
plt.gca().invert_yaxis()
plt.title('% of loss from retail/institutional to consumers (increased<50%)')
plt.show()

#total avg loss for all kinds of fresh vegs
filtered_year['Average fresh veg losses'] = filtered_year.mean(axis='columns')
filtered_year['Average fresh veg losses'].plot(kind='bar')
plt.xticks(rotation=0)
plt.grid(True)
plt.title('Average total losses for fresh veg per year')
plt.show()