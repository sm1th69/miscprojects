import pandas as pd
import os

#set directory
os.chdir("/users/keatondavis/desktop/test")
#list files 
excel_names = ["/users/keatondavis/desktop/test/test1.xlsx", "/users/keatondavis/desktop/test/test1.xlsx"]
excels = [pd.ExcelFile(name) for name in excel_names]

#convert xlsx to dataframe
frames = [pd.read_excel(x, header=None,index_col=None) for x in excels]
#remove first header row
frames[1:] = [df[1:] for df in frames[1:]]

combined = pd.concat(frames)
#write combined file to combine.xlsx
combined.to_excel("combine.xlsx", header=False, index=False)