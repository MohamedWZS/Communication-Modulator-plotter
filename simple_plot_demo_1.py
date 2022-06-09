from matplotlib import pyplot as plt

# prints the available styles you can use 
print(plt.style.available)

# apply the style you like
plt.style.use("fivethirtyeight")

# apply the xkcd comic style
plt.xkcd()

# Median Developer Salaries by Age
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
        56000, 62316, 64928, 67317, 68748, 73752]

# plotting the first line
# the 3rd and 4th argument is for formatting
# the colors can be in hex-code
# the 5th argument is a label argument for better identification for legend
plt.plot(ages_x, dev_y, color="g", linestyle="--", label="All Devs") 

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

# plotting the second line
# the 3rd, 4th, 5th argument is for formatting
# the colors can be in hex-code
# the 6th argument is a label argument for better identification for legend
plt.plot(ages_x, py_dev_y, color="#444444", marker="o", linewidth="3", label="Python Devs") 

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

# plotting the third line
# the 3rd and 4th argument is for formatting
# the colors can be in hex-code
# the 5th argument is a label argument for better identification for legend
plt.plot(ages_x, js_dev_y, color="y", marker="o", label="Js Devs") 

plt.xlabel("Ages")                      # labelling the x-axis
plt.ylabel("Median Salary (USD)")       # labelling the y-axis
plt.title("Median Salary (USD) by Age") # giving a title to the plot

plt.legend(["All Devs", "Python Devs", "Js Devs"]) # applying legend

# apply a grid line
plt.grid(True)

# adjust the padding of the plot
plt.tight_layout()

# saves the plot image in the current directory
# if you want to save it in another directory just write the full path of this directory
plt.savefig("simple_plot.png")

plt.show()