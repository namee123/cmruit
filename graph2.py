import matplotlib.pyplot as plt
# x-cor of left sides of bar
left=[1,2,3,4,5]

#y -cord of height of bar
height=[10,24,36,40,5]

#label for bar
tick_label=['one','two','three','four','five']

#plotting a bar chart
plt.bar(left,height,tick_label=tick_label,
		width=0.8,color=['red','black'])

plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('bar graph')
plt.show()