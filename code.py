import pandas as pd

# # DataFrame
# # saba, mubashara, sana are the columns name 
# # to specify the row name we have to use index=
# df = pd.DataFrame ({'Saba': ['Employed', 'Unmarried'], 'Mubashara': ['Student', 'Unmarried'], 'Sana':['Housewife', 'Married']}, index=['Work Status', 'Matrial Status'])
# print(df)

# # Series
# series = pd.Series(['saba',  'mubashara', 'sana'], index=['obj 1', 'obj 2', 'obj 3'], name='Participants name')
# print (series)

# # some functions for files
# data = pd.read_csv("name_of_file.csv", index_col=0) #reading CSV file
# data.shape # size of the file
# data.head() #first five lines of code
