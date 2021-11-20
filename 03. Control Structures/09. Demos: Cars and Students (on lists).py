# Demo 1:
# 'BMW, Mercedes, Mustang, Mazda' elemanlarına sahip bir liste oluştur
cars = ['BMW','Mercedes','Mustang','Mazda']
result = len(cars) # how many elements in the list?


result = cars[0]        # the first element of the list
#result = cars[3]
result = cars[-1]       # the last element of the list


cars[-1]= 'Toyota'      # to turn Mazda into Toyota
result = cars

result = 'Mercedes' in cars     # Mercedes is an element from the list? # to use 'in' operator 

result = cars[-2]               # the second element from the end

result = cars[0:3]              # to print the first three elements of the list
# result = cars[:3]             # to print the first three elements of the list
# result = cars[-2:]            # to print the first three elements of the list

# Listenin son 2 elemanı yerine 'Audi' ve 'Jeep' değerlerini ekle
cars[-2:] = ['Audi', 'Jeep']    # to add 'Audi' and 'Jeep' values instead of the last two elements of the list
result = cars

result = cars + ['Lamborghini', 'Nissan']       # to add 'Lamborghini' and 'Nissan' values on the list

del cars[-1]            # delete the last element of the list
result = cars

result = cars[::-1]     # to reverse list elements

####################################

# Demo 2:
# to store data below in a list
        # studentA: Franz Kafka 2010, (70, 60, 70)
        # studentB: Lewis Carroll 1999, (80, 80, 70)
        # studentC: Ernest Hemingway 1998, (80, 70, 90)
        
studentA = ['Franz', 'Kafka', 2010,[70, 60, 70]]
studentB = ['Lewis', 'Carroll', 1999, [80, 80, 70]]
studentC = ['Ernest', 'Hemingway', 1998, [80, 70, 90]]
        # the list elements give person information
        
# to print list elements
result = studentA[0]
result = studentB[1]
result = studentC[3]     # to pass another list from inside the list
result = studentC[3][1]  # 1.index from inner list 

# result = f'Franz Kafka 9 y/o and grade mean 66'
result = f'{studentA[0]} {studentA[1]} {2020-studentA[2]} y/o and grade mean {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}'
print(result)

