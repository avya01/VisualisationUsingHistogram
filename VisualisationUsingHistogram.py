import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("Penguins Data (1).csv")
bin = [0, 10, 20, 30, 40, 50, 60]

plt.hist(data["Culmen Length (mm)"], bins = bin, color="red")
plt.hist(data["Culmen Depth (mm)"], bins = bin, color="blue")
plt.hist(data["Flipper Length (mm)"], bins = bin, color="yellow")
plt.hist(data["Body Mass (g)"], bins = bin, color="green")
plt.show()