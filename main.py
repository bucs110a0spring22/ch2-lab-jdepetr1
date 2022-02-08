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

print("Cost per week:", cost_per_week,"\n")


#Part B
rand_list = ["Chocolate", 493, 12.21, "Wow!", 96]
rand_result = random.choice(rand_list)
print("Random choice result:", rand_result, type(rand_result))