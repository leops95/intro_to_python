# This Python script has been written for the course "Introduction to Python"
# at the University of Basel, Spring semester 2023
# Questions or suggestions ? leo.picard@unibas.ch


##############################################################################
# SCIENTIFIC COMPUTING
##############################################################################

# PACKAGES

import numpy
# draw two random values (normally distributed)

print(numpy.random.randn(2))


import numpy as np
from numpy import cos, pi

print(np.sin(np.pi)) # "np" is way shorter than "numpy"

print(cos(pi)) # with "from" we can even omit "np." !


##############################################################################

# LOADING A DATASET

import os # to navigate between paths
import pandas as pd

os.chdir("/home/picard0001/Desktop/intro_to_python")
df = pd.read_csv("data_raw/Alabama_2022.csv")


##############################################################################

# SUMMARY STATISTICS

df.dtypes

df["metaphor_score"].mean()
df["metaphor_score"].std()
df["metaphor_score"].max()
df["metaphor_score"].describe()
df["arg1"].value_counts()
df["speaker"].describe()


##############################################################################

# DATA MANIPULATION

# Drop the filename column
df = df.drop(columns = ["filename"])

# Rename the state column
df = df.rename(columns = {"st_name": "state"})

# Filter out bad metaphor scores
df = df[df["metaphor_score"] >= 0.7]

# Create a new metaphor column
df["metaphor"] = df["arg0"] + " " + df["arg1"]


##############################################################################

# APPLY

# Recode the gender variable from int to str
def recode_party(gender):
    gender_str = ""
    if gender == 1:
        gender_str = "Woman"
    else:
        gender_str = "Man"
    return gender_str

df["gender_str"] = df.apply(lambda x: recode_party(x["gender"]),
                            axis = 1)


##############################################################################

# APPEND

import os
import glob # to store many file names
import pandas as pd

os.chdir("/home/picard0001/Desktop/intro_to_python")

files = glob.glob("data_raw/*_2022.csv") # star = "any"

df = pd.DataFrame() # creates an empty dataframe

for file in files:
    data = pd.read_csv(file)
    df = df.append(data)


##############################################################################

# MERGE

df_party = pd.read_csv("data_raw/political_party.csv")

df_merged = df.merge(df_party, on = "st_name", indicator = True,
                     how = "outer") # or "left", "right", "inner"

# print the output of the merge
print(df_merged['_merge'].value_counts())

df_merged = df.merge(df_party, on = "st_name", indicator = True,
                     validate = "m:1") # or "many_to_one"


##############################################################################

# COLLAPSE
df_merged = df_merged[df_merged["metaphor_score"] >= 0.7]
df_merged["nb_metaphors"] = 1

df_collapsed = df_merged.groupby("party",
                                 as_index = False)["nb_metaphors"].sum()

print(df_collapsed)

    
##############################################################################

# RESHAPE
df_collapsed["statistic"] = "metaphor frequency"

df_wide = df_collapsed.pivot(index = "statistic",
                             columns = "party",
                             values = "nb_metaphors")

print(df_wide)


##############################################################################

# PLOTTING DATA

import matplotlib.pyplot as plt
import numpy as np

x_vals = np.linspace(0,10,10)
y_vals = np.linspace(0,6,10)

plt.plot(x_vals, y_vals)
plt.ylabel("y-axis"); plt.xlabel("x-axis")
plt.savefig("plot_example.png") # save as png
plt.savefig("plot_example.pdf") # save as pdf
plt.show()


df_bar = df_merged.groupby(["party", "gender"], as_index = False)["nb_metaphors"].sum()

df_bar = df_bar.pivot(index = "party",
                      columns = "gender",
                      values = "nb_metaphors")

ax = df_bar.plot.bar(stacked = True, rot = 0)
ax.set_ylabel("Metaphor frequency"); ax.set_xlabel("Party")
ax.legend(["Men", "Women"])

plt.tight_layout(); plt.savefig("plot_example2.pdf")
plt.show()

