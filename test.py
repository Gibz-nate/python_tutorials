'''names = ["jack bronson", "jill mcarty", "john denver"]

names_dict = {}
for name in names:
    # .split() returns a list of strings
    # where each string is a single word from the original
    name_list = name.split()
    print(name_list)
    # here we update the dictionary
    names_dict[name_list[0]] = name_list[1]

print(names_dict)'''
# Prints: {'jack': 'bronson', 'jill': 'mcarty', 'john': 'denver'}

# grades = {"type": {"student": {"name": "Allan", "courses": {"math_1050": {"current_grade": "B"}, "English_1010": {"current_grade": "A-"}}}}}

# for grade in grades.items():
#     pass
# print(grade)

# wage = float(input("Enter your salary to calculate expenditure: "))
# def salary_splitter(salary):
#     tax = 10/100 * salary
#     food = 20/100 * salary
#     utilities = 30/100 * salary
#     savings = 10/100 * salary
#     investments = 30/100 * salary
#     expenditure = tax + food + utilities + savings + investments 

#     print(f" \n tax:{tax} \n food:{food} \n utilities:{utilities} \n savings:{savings} \n investments:{investments}")
#     print(f"expenditure:{expenditure}")

# salary_splitter(wage)


# dict1 = {'player1': 10, 'player2': 15}

# for kv in dict1:
#     print(dict1[kv])



# def total():
#     unpurchased_items = []
#     receipt = {}
#     total = 0
#     for item in pinned_list:
#         if item not in items_purchased:
#             unpurchased_items.append(item)

#     for item in items_purchased:
#         receipt[item] = item_prices[item]

#     for value in receipt[item]:
#         total += value

#     return unpurchased_items, receipt, total        

# fruits = {'apple','orange','banana','apple'}

# for fruit in fruits:
#     print(fruit)


# total = {1,4,3,2} -  {1,2,3}

# print(total)


# mdict = {'price':10, 'gold':120}


# values = mdict.values()
# for value in values:
#     print(value)


# def purchase_item(price, gold_available):
#     if gold_available < price:
#         raise Exception(f"{gold_available:.2f} is not enough for {price:.2f}")
#     return gold_available - price


# print(purchase_item(10, 120))

# triangle
number = 9

for i in range(1, number):
    print(i)


