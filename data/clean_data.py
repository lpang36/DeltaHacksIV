import pandas

df = pandas.read_csv('test.csv')
df = df.drop(['Id','DayOfWeek','PdDistrict','Address'],1)
df['Dates'] = df['Dates'].apply(lambda x: int(x.split('-')[0]))
df.to_csv('cleaned.csv')