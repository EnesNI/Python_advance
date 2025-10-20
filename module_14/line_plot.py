import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("*avgIQpercountry.csv")

avg_iq_per_continent = df.groupby('Continent')['Average IQ'].mean()