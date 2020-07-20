# %%
import pandas as pd
from random import random


df = pd.read_csv("mock_names_phones.csv", header=0)
df

# %%


def permute_hon(hon):
    random_roll = random()
    if random_roll < 0.15:
        hon = hon.upper()
    if 0.15 < random_roll and random_roll < 0.3:
        hon = hon.lower()
    return hon

# %%


def permute_name(name):
    random_roll = random()
    if random_roll < 0.1:
        name = name.upper()
    if 0.1 < random_roll and random_roll < 0.2:
        name = name.lower()
    if 0.2 < random_roll and random_roll < 0.3:
        name = name[0].lower() + name[1:]
    return name

# %%


def permute_phone(phone):

    random_roll = random()
    if random_roll < 0.2:
        phone = " " + phone

    random_roll = random()
    if random_roll < 0.2:
        phone = phone.replace("-", " ")

    random_roll = random()
    if random_roll < 0.15:
        phone = phone.replace(" ", "")

    random_roll = random()
    if random_roll < 0.3:
        phone = "+" + " " + phone
    elif 0.3 < random_roll and random_roll < 0.5:
        phone = "00" + phone[1:]

    random_roll = random()
    if random_roll < 0.1:
        phone = phone[-4:]

    return phone
# %%


for i, row in df.iterrows():
    if row["hon"] == "Honorable":
        row["hon"] = "Miss"

    row["name"] = permute_hon(row["hon"]) + " " + permute_name(row["name"])
    row["phone number"] = permute_phone(row["phone number"])

df.drop("hon", axis=1, inplace=True)
df

# %%
df.to_csv("mock_names_phones.csv")

# %%
