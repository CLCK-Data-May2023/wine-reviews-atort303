# add your code here
import pandas as pd
import numpy as np
df = pd.read_csv("data/winemag-data-130k-v2.csv.zip", compression = 'zip')
summary = df.groupby('country').agg(count=('country', 'count'), points=('points', 'mean')).reset_index()
summary.columns = ['country', 'count', 'points']
summary['points'] = summary['points'].round(1)
print(summary)
summary.to_csv('data/reviews-per-country.csv', index=False)












#country_reviews = df.country.value_counts()
# print(country_reviews)
#point_review = df.groupby("country").points.agg(['mean'])
# print(point_review)
#point_review = point_review.round(1)
# print(point_review)
# print(df.groupby(['country']).points.agg(['mean']))
# print(country_reviews)
#series_1 = country_reviews
#series_2 = point_review
#new_df = pd.concat([series_1, series_2], axis =1)
#print(new_df)
# ew_df.to_csv("data/reviews-per-country.csv", index = True)
# new_df.to_csv('wine-reviews-atort303/reviews_per_country.csv', index = True)
