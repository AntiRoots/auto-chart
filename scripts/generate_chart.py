import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/data.csv")

plt.figure(figsize=(8, 5))
plt.bar(df["month"], df["value"], color='skyblue')
plt.xlabel("Month")
plt.ylabel("Value")
plt.title("Automaatne Graafik")
plt.tight_layout()
plt.savefig("docs/chart.png")
