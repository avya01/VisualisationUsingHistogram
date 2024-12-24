import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("Penguins Data (1).csv")
bin = [0, 10, 20, 30, 40, 50, 60]

plt.hist(data["Culmen Length (mm)"], label="Culmen Length", bins = bin, color="red")
plt.hist(data["Culmen Depth (mm)"], label="Culmen Depth", bins = bin, color="blue")
plt.hist(data["Flipper Length (mm)"], label="Flipper Length", bins = bin, color="yellow")
plt.hist(data["Body Mass (g)"], label="Body Mass", bins = bin, color="green")
plt.legend()
plt.show()