# joel moore    spring 2025     CSC284_classListS.py

'''
This program is modified by each CSC284 student in the following way:

1. each student adds their name to the list below
2. run the program and print the list
3. update the program in HJMoore11/CSC284

'''
# ============================define list, lastName, firstName

CSC284_2025SP=[
    'Moore, Joel',
    'Student, Test',
    'Miller, CMille81',
    'Aguirre, Jason'  # Added my name
    'Muin, Emmanuel'
    'Kelly, Jamiyah'

]

# ============================sort the list

CSC284_2025SP.sort()

# =====================================print the list

print('2025SP CSC284 Alpahbetical Class List ')
for name in CSC284_2025SP:
    print(f'  {name}')
