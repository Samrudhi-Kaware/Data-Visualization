import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

ages = np.arange(18, 30)
salaries_python = np.random.randint(20, 80, size=len(ages))
salaries_ml = np.random.randint(40, 120, size=len(ages))

ax1.plot(ages, salaries_python, label="Python", color="red")
ax1.plot(ages, salaries_ml, label="ML", color="green")

salaries = [30, 40, 50, 60, 90]
labels = ['HTML', 'Python', 'ML', 'DevOps', 'Device Driver']
explode = [0, 0, 0.1, 0, 0]

ax2.pie(salaries, labels=labels, explode=explode, shadow=True,
            autopct='%1.0f%%', wedgeprops={'edgecolor': 'black'})

plt.tight_layout()
plt.show()