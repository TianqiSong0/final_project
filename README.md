# Introduction of the project
This project aims to identify whether the percent of logistical losses for fresh food has been decreased in 2006 and in 2011. To achieve the goal, the project will:

## Data part
1. Use `pandas` to read the excel sheets from USDA
    + redefine header; and skip title and footnote lines
        + `pd.read_excel(file,sheet_name=None, header=1, skiprows=2, nrows=6)` demand 
2. Drop unneeded tabs/keys
    + `del` demand
3. Select the targeted columns that will be used by creating a new empty DataFrame
    + `for` loop with `pd.DataFrame()` demand
4. Drop unneeded rows. In this case are dry foods since their logistical losses did not change over time
    + `for` loop with `.drop()` demand
5. Drop unavailable data which are those years that are not 2006 or 2011
    + `.drop(index=["column_name1", "column_name2"])` demand

## Plot part
1. Import `matplotlib.pyplot` 
2. Divide data into four catagories as one plot will be too unfriendly to read: 
    + [% of loss from retail/institutional to consumers (decreased>=50%)](decreased_over50.png)
    + [% of loss from retail/institutional to consumers (decreased<50%)](decreased_small_than50.png)
    + [% of loss from retail/institutional to consumers (increased>=50%)](increased_over50.png)
    + [% of loss from retail/institutional to consumers (increased<50%)](increased_small_than50.png)

    ```
    decreased_above50 = pd.DataFrame()
    decreased_below50 = pd.DataFrame()
    increased_above50 = pd.DataFrame()
    increased_below50 = pd.DataFrame()
    ```
3. Transpose and sort values
    + `.transpose()` and `.sort_values(by="column_name", ascending=False)` demand 
4. Create four groups of horizontal bar plots
    + `dataframe.plot(kind='barh')`
        + add grid
            + `plt.grid(True)`
        + flip over bar orders 
            + `plt.gca().invert_yaxis()`
        + add title
            + `plt.title('% of loss from retail/institutional to consumers')`
        + show
            + `plt.show()`
5. Create total average losses bar plot
    + calculate the mean by creating a new column 
        + `.mean()` demand 
    + create a bar plot for only one column in the DataFrame
        + `DataFrame['selected column'].plot(kind='bar')`
    + rotate x axis title 
        + `plt.xticks(rotation=0)`
    + add grid 
    + add title 
        + `plt.title('Average total losses for fresh veg per year')`
    + show