import pandas as pd

df = pd.read_csv('updated_data_clear.csv')
print(df.columns)
print(df.dtypes)
df = df.dropna()


df['Radius'] = df['Radius'].apply(lambda x:x.replace('$','').replace(',','')).astype('float') 
print(df.dtypes)

radiuses = df['Radius'].to_list()
masses = df['Mass'].to_list()
def conversion(radiuses,masses):
    for i in range(0,len(radiuses)):
        radiuses[i] = radiuses[i]*6.957e+8
        masses[i] = masses[i]*1.989e+30     
conversion(radiuses,masses)

gravity =[]
def gravity_cal(radiuses,masses):
    gravitational_constant = 6.674e-11
    for index in range(0,len(masses)):
        gravitational_value = (masses[index]*gravitational_constant)/((radiuses[index])*(radiuses[index]))
        gravity.append(gravitational_value)
gravity_cal(radiuses,masses)

df["Gravity"] = gravity
df.to_csv("star_data_gravity.csv")
