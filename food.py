#this project is designed to find people's preference over vegetable loss, and make a comparsion 
#between vegetable loss and meat loss

import pandas as pd
fruitveg = pd.read_csv('fruitveg.csv')
legumes = pd.read_csv('legumes.csv')
potatoes = pd.read_csv('potatoes.csv')
vegcan = pd.read_csv('vegcan.csv')
vegfr = pd.read_csv('vegfr.csv')
vegfrz = pd.read_csv('vegfrz.csv')
vegprc = pd.read_csv('vegprc.csv')
vegtot = pd.read_csv('vegtot.csv')
veg = pd.read_csv('veg.csv')
total_veg_loss = pd.DataFrame()