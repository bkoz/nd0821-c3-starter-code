# API project

## Census Data

### Steps

#### Data Cleaning

###### Backup the original dataset.
```
cp census.csv census-raw.csv
```

##### Data Cleaning
I used the following `vim` command to remove the spaces after a comma.
```
:1,$s/, /,/g
```
```
df.columns = df.columns.str.replace(' ', '')
```

###### TODO: Remove duplicate rows.
```
df.drop_duplicates()
```

##### Data Processing


