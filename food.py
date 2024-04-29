#this project is designed to find out people's preference over vegetable loss, and make a comparsion 
#between vegetable loss and meat loss

import pandas as pd

#read the files and convert sheets into dictionaries
filelist = ['legumes.xlsx', 'potatoes.xlsx', 'vegcan.xlsx', 'vegfr.xlsx', 'vegfrz.xlsx', 'vegprc.xlsx', 'vegtot.xlsx', 'veg.xlsx']
for f in filelist:
    fh = pd.read_excel(f,sheet_name=None)
print(fh)

#%%
#create dataframes by using dictionaries' keys



df = {}
for k in fh.keys():
    subdf = pd.DataFrame({k: fh["key", "value"]})
    
    
    
    #%%
    subdf = pd.DataFrame({fh: fh[k]})


#%%
for k in fh:
    df = pd.DataFrame(fh.keys)
    
#%%  
legumes = pd.DataFrame()


def Df(filename):
    df = pd.DataFrame(filename)
    return df


    for value, i in fh:
        df = pd.DataFrame([value], index=[0])
        #df = df.append(i, ignore_index=True)
              
#%%       
        
    subdf = pd.DataFrame(fh)
    df = df.extend(subdf) 
    
#%%

for f in file_list:
    fh = pd.read_excel(f, sheet_name=None)
    

# Optionally, reset the index of the DataFrame after appending
df.reset_index(drop=True, inplace=True)

#%%
legumes = rexcel('legumes.xlsx')
potatoes = rexcel('potatoes.xlsx')
vegcan = rexcel('vegcan.xlsx')
vegfr = rexcel('vegfr.xlsx')
vegfrz = rexcel('vegfrz.xlsx')
vegprc = rexcel('vegprc.xlsx')
vegtot = rexcel('vegtot.xlsx')
veg = rexcel('veg.xlsx')

#%%
legume = pd.DataFrame(legumes)
potato = pd.DataFrame(potatoes)

colloc = [0]
colname = ["year"]

legumes.raname(columns=colname)

# Assuming 'legumes' is your DataFrame
col_index = 0  # Index of the column you want to rename
new_column_name = "year"  # New name for the column

# Rename the specific column using iloc and rename
legumes.rename(columns={legumes.columns[col_index]: new_column_name}, inplace=True)
#%%
total_veg_loss = pd.concat([legumes, potatoes, vegcan, vegfr, vegfrz, vegprc, vegtot, veg])
#%%
total_veg_loss = total_veg_loss.merge()