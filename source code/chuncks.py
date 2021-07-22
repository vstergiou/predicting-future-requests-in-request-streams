'''
import pandas as pd
xl = pd.ExcelFile("./dokimastiko.xlsx")
i=0
for sheet_name in xl.sheet_names:
  reader = xl.parse(sheet_name, chunksize=9)
  for chunk in reader:
      print(i)
      i=i+1

'''
import os
import pandas as pd
file_name = './dokimastiko.xlsx'
nrows = 10

xl = pd.ExcelFile(file_name)

# In this case, there was only a single Worksheet in the Workbook.
sheetname = xl.sheet_names[0]

# Read the header outside of the loop, so all chunk reads are
# consistent across all loop iterations.
df_header = pd.read_excel(file_name, sheetname=sheetname, nrows=1)
print(f"Excel file: {file_name} (worksheet: {sheetname})")

chunks = []
i_chunk = 0
# The first row is the header. We have already read it, so we skip it.
skiprows = 1
while True:
    df_chunk = pd.read_excel(
        file_name, sheetname=sheetname,
        nrows=nrows, skiprows=skiprows, header=None)
    skiprows += nrows
    # When there is no data, we know we can break out of the loop.
    if not df_chunk.shape[0]:
        break
    else:
        print(f"  - chunk {i_chunk} ({df_chunk.shape[0]} rows)")
        chunks.append(df_chunk)
    i_chunk += 1

df_chunks = pd.concat(chunks)
# Rename the columns to concatenate the chunks with the header.
columns = {i: col for i, col in enumerate(df_header.columns.tolist())}
df_chunks.rename(columns=columns, inplace=True)
df = pd.concat([df_header, df_chunks]) 
print(df)