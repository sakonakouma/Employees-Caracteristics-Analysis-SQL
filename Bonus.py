#Import dependencies
# Pandas
import pandas as pd

import psycopg2

# Matplotlib
import matplotlib.pyplot as plt

# NumPy
import numpy as np

import scipy.stats as st

from config import password

from sqlalchemy import create_engine
engine = create_engine(f'postgresql://postgres:{password}@localhost:5432/EmployeeSQL')
connection = engine.connect()

data_employees = pd.read_sql("select * from data_employees", connection)
data_employees.head()

# Salaries analysis 
data_salaries = pd.read_sql("SELECT * from data_salaries", connection)
data_salaries.head()

data_salaries.min()


employees_salary = pd.merge(data_employees, data_salaries, on = "emp_no")
employees_salary
employees_salary2= employees_salary.rename(columns={"emp_title":"title_id"})
employees_salary2


# Create a histogram to visualize the most common salary ranges for employees.
x = employees_salary2['salary']
plt.hist(x, bins=15)
plt.show()

#Create a bar chart of average salary by title
titles_salary= pd.read_sql('select * from data_titles', connection)
titles_salary

# Merging tables
emp_salary_title = pd.merge(employees_salary2, titles_salary, on = "title_id")
emp_salary_title

title_avg = emp_salary_title.groupby(['title']).mean()['salary'] 
title_avg.round(2)

x_axis = title_avg.index.values
x_axis


y_axis = title_avg.index.values
y_axis

#bar chart using pyplot
plt.bar(x_axis, y_axis)
plt.xticks(rotation = 45)
plt.title("Average Salary per Job Title")
plt.xlabel("Job Title")
plt.ylabel("Salary ($)")
plt.show()