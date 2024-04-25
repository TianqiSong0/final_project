#this project is designed to find people's preference over vegetable loss, and make a comparsion 
#between vegetable loss and meat loss

import pandas as pd

fruitveg = pd.read_excel('fruitveg.xlsx')
legumes = pd.read_excel('legumes.xlsx', sheet_name="PccLegumes")
PccDryBeans = pd.read_excel('legumes.xlsx', sheet_name="PccDryBeans")
DryBeans = pd.read_excel('legumes.xlsx', sheet_name="DryBeans")
PintoBeans = pd.read_excel('legumes.xlsx', sheet_name="PintoBeans")
NavyBeans = pd.read_excel('legumes.xlsx', sheet_name="NavyBeans")
GreatNorthernBeans = pd.read_excel('legumes.xlsx', sheet_name="GreatNorthernBeans")
RedKidneyBeans = pd.read_excel('legumes.xlsx', sheet_name="RedKidneyBeans")
DryLimaBeans = pd.read_excel('legumes.xlsx', sheet_name="DryLimaBeans")
BlackBeans = pd.read_excel('legumes.xlsx', sheet_name="BlackBeans")
BlackeyeBeans = pd.read_excel('legumes.xlsx', sheet_name="BlackeyeBeans")
GarbanzoBeans = pd.read_excel('legumes.xlsx', sheet_name="GarbanzoBeans")
SmallWhiteBeans = pd.read_excel('legumes.xlsx', sheet_name="SmallWhiteBeans")
SmallRedBeans = pd.read_excel('legumes.xlsx', sheet_name="SmallRedBeans")
PinkBeans = pd.read_excel('legumes.xlsx', sheet_name="PinkBeans")
CranAndMiscbeans = pd.read_excel('legumes.xlsx', sheet_name="CranAndMiscbeans")
potatoes = pd.read_excel('potatoes.xlsx', sheet_name="Pcc")
SweetPotatoes = pd.read_excel('potatoes.xlsx', sheet_name="SweetPotatoes")


vegcan = pd.read_excel('vegcan.xlsx')
vegfr = pd.read_excel('vegfr.xlsx')
vegfrz = pd.read_excel('vegfrz.xlsx')
vegprc = pd.read_excel('vegprc.xlsx')
vegtot = pd.read_excel('vegtot.xlsx')
veg = pd.read_excel('veg.xlsx')
total_veg_loss = pd.concat([fruitveg, legumes, potatoes, vegcan, vegfr, vegfrz, vegprc, vegtot, veg])
#%%
total_veg_loss = total_veg_loss.merge()