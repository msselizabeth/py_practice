import matplotlib.pyplot as plt
import pandas as pd

# date_range_weekly = pd.date_range(start='2023-01-01', periods=3, freq='W')
# print("\nWeekly Date Range:")
# print(date_range_weekly)

x = [1, 2, 3, 4, 5]
y = [4, 6, 1, 3, 8]

plt.plot(x, y, marker="o", linestyle="-", label='text for legend')

# Labels for axis
plt.xlabel("X - axis", color='green')
plt.ylabel("Y - axis", color='orange')

#  Plot title
plt.title("Plot example title", fontsize=16, loc="left")

# add text to the plot
plt.text(x[0]+0.05, y[0] - 0.10 , "bla bla bla", color='pink')
plt.legend()

plt.savefig('my_graph.png') 
plt.show()

# ----- Plot Dots -----
# plt.scatter(x, y)
# plt.show()
