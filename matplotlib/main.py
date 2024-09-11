import pandas as pd

df = pd.read_excel("C:/Users/sivav/Downloads/TestScore.xlsx")

# print(df)
import matplotlib.pyplot as plt

plt.plot(df["Month"], df["Mark"])
plt.title("Mountain Pandi Test Score")
plt.xlabel("Marks")
plt.ylabel("Months")
plt.grid(True)
plt.show()