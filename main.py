import random
#Part A
weeks = 16
classes = 5
tuition = 6000

classes_per_week = 12 # I created
print("Classes per week:", classes_per_week, type(classes_per_week))


cost_per_week = ((tuition / classes) / weeks)
cost_per_class = cost_per_week / classes_per_week # I created
print("Cost per class:", cost_per_class, type(cost_per_class))

print("Cost per week:", cost_per_week)


#Part B
randomList = ["Chocolate", 493, 12.21, "Wow!", 96]
randomResult = random.choice(randomList)
print("Random choice result:", randomResult, type(randomResult))