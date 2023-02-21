import matplotlib.pyplot as plt
plt.hist([135]*8+[140]*12+[145]*16+[150]*8,[135,140,145,150,155])
plt.xlabel('heights')
plt.ylabel('no of students')
plt.show()
