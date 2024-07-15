# Introduction of the project
This project aims to identify whether the percent of logistical losses for food has been decreased in 2006 and in 2011. 
To achieve the goal, the project will:

## Data part
1. Use `pandas` to read the excel sheets from USDA to create a dataframe 
2. Drop unneeded tabs/keys
3. Select the targeted columns that will be used 
4. Drop unneeded rows. In this case are dry foods since their logistical losses did not change 
5. Drop unavailable data which are those years are not 2006 or 2011

## Plot part
1. Import `matplotlib.pyplot` 
2. Divide data into four catagories as one plot will be too unfriendly to read: 
    + [% of loss from retail/institutional to consumers (decreased>=50%)](decreased_over50.png)
    + [% of loss from retail/institutional to consumers (decreased<50%)](decreased_small_than50.png)
    + [% of loss from retail/institutional to consumers (increased>=50%)](increased_over50.png)
    + [% of loss from retail/institutional to consumers (increased<50%)](increased_small_than50.png)
3. Transpose and sort values
4. Create four groups of plots
5. Create total average losses plot