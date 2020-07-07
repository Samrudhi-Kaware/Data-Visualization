import numpy as np
import matplotlib.pyplot as plt

salaries = [30, 40, 50, 60, 90]
labels = ['HTML', 'Python', 'ML', 'DevOps', 'Device Driver']
explode = [0, 0, 0.1, 0, 0]

plt.title('Salaries of different job title')
plt.pie(salaries, labels=labels, explode=explode, shadow=True,
            autopct='%1.2f%%', wedgeprops={'edgecolor': 'black'})
plt.tight_layout()
plt.savefig('salaries.png')
plt.show()
