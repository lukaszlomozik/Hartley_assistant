import pandas as pd

data_frame = pd.read_excel('Szablon.xlsx')
print(data_frame)

for row in data_frame.values:
    for i in row:
        print(float(i))