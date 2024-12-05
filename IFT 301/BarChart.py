import matplotlib.pyplot as plt

ingredients = ['Spinach', 'Sausage', 'Prawns', 'Pineapple', 'Mushroom']
proportions = [0.28, 0.18, 0.08, 0.28, 0.16]

plt.barh(ingredients, proportions, color='#715381') 

plt.xlabel('Proportion of Total')
plt.title('Ingredient Proportions')
plt.gca().invert_yaxis()  

plt.show()