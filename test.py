import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
import numpy as np

payment_data = pd.read_csv('datasets/payments_son.csv')


x_train, x_test, y_train, y_test = train_test_split(payment_data[['GradeAvg','SoftwareXP',
                                                                'ElectronicsXP','MechanicalXP',
                                                                'ManagementXP','Projects',
                                                                'Languages','Master']],
                                                    payment_data['Payment'], test_size=0.1)


model = LinearRegression()
model.fit(x_train, y_train)


grade_avg = 2.5
software_xp = 0
electronics_xp = 9
mechanical_xp = 0
management_xp = 5
projects = 2
languages = 2
master = 1

infos = [grade_avg,software_xp,electronics_xp, mechanical_xp,management_xp,projects,languages, master]
infos_df = pd.DataFrame(np.array([infos]), columns = ['GradeAvg','SoftwareXP', 'ElectronicsXP','MechanicalXP','ManagementXP','Projects','Languages','Master'])

prediction = model.predict(infos_df)
print(prediction)
