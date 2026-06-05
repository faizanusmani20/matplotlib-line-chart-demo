import matplotlib.pyplot as plt 

x = [2021, 2022, 2023, 2024, 2025]
y1 = [8, 20, 30, 41, 52]
y2 = [18, 40, 70, 81, 22]
y3 = [58, 70, 30, 11, 12]

# marker= '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'

line_style1 = dict(marker='.', color='purple', linestyle='--', markersize=20, markerfacecolor='red')
line_style2 = dict(marker='*', color='red', linestyle='solid', markersize='20', markerfacecolor='blue')
line_style3 = dict(linestyle='-.', marker='v', markersize='20', markeredgecolor='purple', linewidth='3')

plt.title("This is Title (Data)", fontsize='20', family='Arial', fontweight='bold', color='Blue')
plt.xlabel("This is X Axis (Year)", fontsize='20', family='Arial', fontstyle='italic', color='Red')
plt.ylabel("This is Y Axis (Students)", fontsize='20', family='Arial', fontstyle='italic', color='Green')

plt.tick_params(axis='both', colors='Gold')

plt.plot(x, y1, **line_style1)
plt.plot(x, y2, **line_style2)
plt.plot(x, y3, color='pink', **line_style3)   # Another method to color a line

plt.xticks(x)

plt.grid()  # We can set line width, specific axis, linestyle (--, -., etc.), color, etc.

plt.show()