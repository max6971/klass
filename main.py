import pandas as pd
import numpy as np


data ={
    'name' : ['Иван', 'Петр', 'Анна', 'Юлия', 'Сергей', 'Светлана', 'Юрий', 'Илья', 'Кристина', 'Кирилл'],
  'Mathimatic' : [ 4, 5, 4, 3, 5, 4, 3, 5, 5, 5],
  'Russian_language': [4, 3, 5, 3, 4, 4, 5, 5, 4, 4],
  'Russian history': [4, 5, 4, 3, 5, 4, 5, 3, 4, 5 ],
  'physics' : [4, 5, 4, 3, 5, 4, 5, 4, 5, 3],
  'chemistry': [4, 5, 3, 4, 5, 5, 4, 5, 4, 3]
  }
df = pd.DataFrame(data)
print(df)
#print(df.describe())
print(f"Средняя оценка по математике - {df['Mathimatic'].mean()}")

print(f"Средняя оценка по русскому языку - {df['Russian_language'].mean()}")

print(f"Средняя оценка по русской истории -{df['Russian history'].mean()}")

print(f"Средняя оценка по физике - {df['physics'].mean()}")

print(f"Средняя оценка по химии - {df['chemistry'].mean()}")


print(f"Медиальная оценка по математике - {df['Mathimatic'].median()}")

print(f"Медиальная оценка по русскому языку - {df['Russian_language'].median()}")

print(f"Медиальная оценка по русской истории - {df['Russian history'].median()}")

print(f"Медиальная оценка по физике - {df['physics'].median()}")

print(f"Медиальная оценка по химии - {df['chemistry'].median()}")


print(f"Стандартное отклонение оценок по математике - {df['Mathimatic'].std()}")

print(f"Стандартное отклонение оценок по русскому языку - {df['Russian_language'].std()}")

print(f"Стандартное отклонение оценок по русской истории - {df['Russian history'].std()}")

print(f"Стандартное отклонение оценок по физике - {df['physics'].std()}")

print(f"Стандартное отклонение оценок по химии - {df['chemistry'].std()}")

#df.boxplot(column='Mathimatic')

Q1 = df['Mathimatic'].quantile(0.25)
Q3 = df['Mathimatic'].quantile(0.75)
IQR = Q3 - Q1
print(f"Первый квартиль оценок по математике - ", Q1)
print(f"Третий квартиль оценок по математике - ", Q3)
print(f"Межквартальный размах оценок по математике - ", IQR)