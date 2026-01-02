# Pandas

## DataFrames

In Pandas, we mainly work with **DataFrames**.

A DataFrame is a table-like structure with **rows and columns**, where each column can have a different data type.

We can create a DataFrame using:
pd.DataFrame() _Example on line 8_

---

## Series

A **Series** is a one-dimensional array-like structure.

- It represents a single column of data
- It has an index (row labels)
- It can have a name

Example:
A column in a DataFrame is a Series.
pd.Series() _Example on line 12_

---

## Reading a CSV file

To read a CSV file:
pd.read*csv('file_name.csv') \_Example on line 16*

`read_csv()` also has many useful parameters like:

- `sep` (separator)
- `header`
- `index_col`

---

## Checking data

To check the size of the dataset:
df.shape _Example on line 17_

To view the first 5 rows:
df.head() _Example on line 18_

---

## Saving data

To save a DataFrame to a CSV file:
df.to_csv('file_name.csv', index=False)
