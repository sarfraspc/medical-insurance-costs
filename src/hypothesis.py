import pandas as pd
from scipy.stats import ttest_ind

df=pd.read_csv('insurance.csv')
print(df.head())

smoker_charges=df[df['smoker']=='yes']['charges']
non_smoker_charges=df[df['smoker']!='yes']['charges']

t_test,p_value=ttest_ind(smoker_charges,non_smoker_charges)

print(t_test)
print(p_value)

if p_value < 0.05:
    print("reject H₀: smokers have significantly different charges.")
else:
    print("fail to reject H₀: no significant difference.")