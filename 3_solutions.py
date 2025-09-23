# This Python was created for the crash course "Introduction to Python"
# at the University of Basel, Fall semester 2025
# Questions or suggestions? leo.picard@unibas.ch


##############################################################################
# SOLUTIONS TO EXERCISES
##############################################################################

# EXERCISE 1

# example
number1 = 2
number2 = 10

number3 = number2
number2 = number1
number1 = number3
del number3

# best
number1 = 2
number2 = 10

number1, number2 = number2, number1


##############################################################################

# EXERCISE 2

# example 1
listname = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = []

for elem in listname:
    elem = 9 - elem
    new_list.append(elem)

# example 2
listname = range(0, 10)
new_list2 = [9-x for x in listname]

# best
listname = list(range(0, 10))
listname.sort(reverse = True)


##############################################################################

# EXERCISE 3

# one example among many
def printValues(how):
    l = []
    for i in range(1,21):
        if how == "even":
            if i%2 == 0:
                l.append(i**2)
        elif how == "odd":
            if i%2 != 0:
                l.append(i**2)
        else:
            return print("The odd/even parameter was misspelled")

    return l

print(printValues(how = "odd"))
print(printValues(how = "even"))
print(printValues(how = "test"))


##############################################################################

# EXERCISE 4
import os
import glob # to store many file names
import pandas as pd

os.chdir("/home/username/Desktop/intro_to_python")

files = glob.glob("data_raw/*_2022.csv") # star = "any"

df = pd.DataFrame() # creates an empty dataframe

for file in files:
    data = pd.read_csv(file)
    df = df.append(data)

# Drop the filename column
df = df.drop(columns = ["filename"])

# Rename the state column
df = df.rename(columns = {"st_name": "state"})

# Filter out bad metaphor scores
df = df[df["metaphor_score"] >= 0.7]

# Create a new metaphor column
df["metaphor"] = df["arg0"] + " " + df["arg1"]

# Collapse by state
df["nb_metaphors"] = 1
df_plot = df[["state", "nb_metaphors"]]
df_plot = df_plot.groupby("state", as_index = False).sum()

# Sort values from greatest to smallest
df_plot = df_plot.sort_values('nb_metaphors', ascending = False)

# Plot data
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
ax = df_plot.plot.bar(x = "state", y = "nb_metaphors")
ax.set_ylabel("Metaphor frequency"); ax.set_xlabel("State")
ax.get_legend().remove()
plt.tight_layout()
plt.savefig("plot_example3.pdf", dpi = 300)
