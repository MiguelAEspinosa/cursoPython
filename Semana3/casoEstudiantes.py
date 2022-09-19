import numpy as np
import pandas as pd
import matplotlib as plt

data_students = pd.read_csv("C:\\Users\\mespinosa\\Documents\\pythonFundamental\\Semana3\\clean_students_complete.csv")
data_students.head()

data_students.set_index("student_id")