# Q1.


print("\t Question 01 \n")


def tower_of_honie(number_of_dics,a,b,c):
    if number_of_dics > 0:
        tower_of_honie(number_of_dics -1, a, c, b)
        print(f"Move disc {number_of_dics} from {a} to {c}")
        tower_of_honie(number_of_dics -1, b,a,c)


number_of_dics = 3   
tower_of_honie(3, "a", 'b', 'c')  
print()


# Q2


print("\t Question 02 \n")

# Using Recurrsion.

print("Using recurrsion. \n")


def pascel_triangle(n,list1):             # n = number of lines 
    if n == 0 :
        return
    
    pascel_triangle(n-1,list1)      

    l = len(list1)
    list2 = list1.copy()             
    list1.append(1)

    for counter in range(0,l):              
        if counter == 0:
            list1[0] = 1
        else:
            list1[counter] = list2[counter] + list2[counter-1]
    
    proper_pattern(list1)   
def proper_pattern(list1):
    print(" "*(number - len(list1)), end = "")

    for item in list1:
        print(item , end = " ")
    print()
number = int(input("Enter the number(natural number) of line to print: "))
print()
initial_list = []
pascel_triangle(number,initial_list)





# Using iteration.
print("\n Using iteration.\n")

output_list = []

for counter in range(number):
    if len(output_list) == 0:
        temp_list = []
    else:
        temp_list = output_list[counter - 1].copy()

    temp_list.append(1)
    
    if counter > 1:
        for j in range(1,len(output_list[counter - 1])):
            temp_list[j] = output_list[counter - 1][j] + output_list[counter - 1][j - 1]

    output_list.append(temp_list)

for lst in output_list:
    proper_pattern(lst)



# Q3.

print("\n\t Question 3 \n")


num_1 = int(input("Please enter a number: "))
num_2 = int(input("Please enter second number(number must not be zero): "))
print()
quotient_reminder = divmod(num_1, num_2)
print(f"The quotient and reminder of the values are {quotient_reminder}")
print("\n\tPart A\n")
check = callable(divmod)
if check == True:
    print("It is callable.")
elif check == False:
    print("It is not callable.")


print("\n\t Part B\n")
if quotient_reminder == (0,0):
    print("Both values are zero.")
elif quotient_reminder[0] == 0:
    print("Only quotient is zero")
elif quotient_reminder[1] == 0:
    print("Only reminder is zero.")
else:
    print("Both are non zero.")
print("\n\t Part C \n")


new_result = quotient_reminder.__add__((4,5,6))
print(f"Result after adding values: {new_result} \n")

value_greater_than_4 = []
for counter in range(len(new_result)):
    if new_result[counter] > 4:
        value_greater_than_4.append(new_result[counter])
print(f"Values greater than 4: {value_greater_than_4}")
print()
print("\n\t Part D \n")

converting_to_set = set(new_result)
print(f"After converting the above result into set {converting_to_set} \n")
print("\n\t Part E \n")

converting_to_immutable = frozenset(converting_to_set)
print("Now set is immutable")

print("\n\t Part f \n")
print(f"Max value in the set is {max(converting_to_immutable)}")
print(f"Hash value is: {hash(converting_to_immutable)}")

# Q4.

print("\n\t Question 4 \n")
class Student():
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        print(f"Object created for {self.name}")
    def show_info(self):
        print(f'The name of the student is {self.name}')
        print(f'The roll number of {self.name} is {self.rollno}')





    #Destructor
    def __del__(self):
        print(f"Destructor deleted {self.name}'s record.")



# Creating objects
student_1 = Student("Honey", 21105100)
student_2 = Student("Lucy", 21105008)
student_3 = Student("Bunny", 21105067)
print()

# details of student
student_1.show_info()
print("\n")
student_2.show_info()
print("\n")
student_3.show_info()
print('\n')

#destructor.
del student_1
del student_2
del student_3

# Q5


print("\n\t Question 05\n")


class factory():
    #store
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        print(f"Object created named {self.name}.")
    #show
    def show_info(self):
        print("\tShowing info of the employee.")
        print(f"Name of the employee working in this factory is {self.name}")
        print(f"Salary of {self.name} is {self.salary}.")

    #update salary 
    def update_salary(self,new_salary):
        self.salary = new_salary
        print(f"Updated salary of the employee {self.name} is {self.salary}\n")

    #delete the data 
    def __del__(self):
        print(f"Record of the employee {self.name} is deleted.")
    
# Crating objects
Mehak = factory('Mehak', 40000)
Ashok = factory("Ashok", 50000)
Viren = factory('Viren', 60000)
print()
# Calling function 
Mehak.show_info()
print()
Ashok.show_info()
print()
Viren.show_info()
print()
#update the salary of the employee.
print("Updating mehak's salary.")
Mehak.update_salary(70000)

#remove data of the employee
print("Calling destructor to delete viren's record.")
del Viren

# Q6 
print("\n\t Question 6 \n")

# Taking inputs from the friends.
utter_word = input("George's Word : ")
print()
new_word = input("Barbie's Word : ")
print()
count_list_uttered_word = [0]*26
count_list_new_word = [0]*26
for letter in utter_word:
    count_list_uttered_word[ord(letter.lower()) - ord('a')] += 1




for letter in new_word:
    count_list_new_word[ord(letter.lower()) - ord('a')] += 1




if count_list_uttered_word == count_list_new_word:

    while True:

        
        check = input("Please enter whether the new word have meaning or not(Yo or No): ")
        print()
        if check == "Yo":
            print("passed the friendship test.")
            break
        elif check == "No":
            print("failed the friendship test")
            break
        else:
            print("Please enter a valid input.(Yo or No)")


else:
    print("failed the friendship test")
