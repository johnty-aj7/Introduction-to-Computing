# Question - 1 

print("Q 1")
# Taking string input from the user 
user_input = input("Enter the string: ")

# Converting upercase letters to lower case and storing it in list.

user_input = user_input.lower()

print()

count_dict = {}

# Empty disc for counting words.

# Spliting the string in the list


user_words = user_input.split(" ")

# Checking if input string is a single word or not so that we can count different words of the string 
if len(user_words) == 1:
    
    user_words = user_input

# For loop is used to count the occurance of words and characters.

for word in user_words:
    
    if word in count_dict:
        
        count_dict[word] += 1
    else:
        count_dict.update({word : 1})
        

# Result.

if len(user_input) == 0:
    
    print("No word or sentence found.")
else:

    print("Number of each word/character in string is:" ,count_dict , "\n")



#QUESTION - 2 

print("Q 2")

#Taking input from user
day=int(input('Please enter Day- '))

month=int(input('Please enter Month- '))

year=int(input('Please enter Year- '))


#Removing all the invalid cases

if day>30 and month in {2,4,6,9,11}:
    condition=False
    
elif day>31 and month in {1,3,5,7,8,10,12}:
    condition=False
    
elif (day==29 or day==30) and month==2 and year%4!=0:
    condition=False
    
elif day==30 and month==2 and year%4==0:
    
    condition=False
else:
    condition=True


#After checking the condition, following if-else statement is executed
if condition:

    #checking and changing for new year
    if day==31 and month==12:
        n_year=year+1
    else:

        n_year=year
    if month==12 and day==31:
        n_month=1
        
    else:
        n_month=month
#changing dates
    #checking for months with 31 days
        
    if month in {1,3,5,7,8,10,12}:
        if day==31:
            next_day=1
            
            if month!=12:
                n_month=month+1
                
            else:
                n_month=1
        else:
            next_day=day+1
            
    #checking for the month of february
    elif month==2:
        
        if year%4==0:
            
            if day==29:
                next_day=1
                
                n_month=3
            else:
                
                next_day=day+1
        else:
            if day==28:
                next_day=1
                
                n_month=3
            else:
                next_day=day+1
                    
    #covering all the remaining cases
    else:
        if day==30:
            
            next_day=1
            n_month=month+1
        else:
            
            next_day=day+1
    #printing the calculations
            
    print(f"Next Date is: {next_day}/{n_month}/{n_year}")
    
else:
    #gives a warning and ends the program

    
    print("That's not a valid date")
    

# Question - 3

print("Q3")
 
# Taking given and output list from the user

given_list = []
output_list = []

max_input = int(input("total number of terms : "))

print()
for i in range(max_input):
    tmp_num = int(input(f"Enter the {i + 1} number: "))
    
    given_list.append(tmp_num)
print()

# for loop is used to calculate sqaure and adding it in tuple.

for num in given_list:
    temp_tuple = (num,num*num)
    output_list.append(temp_tuple)

# Result
print(output_list)
print("\n")



#QUESTION - 4 

print("Q 4")

# Taking input from the user:

grade_num = int(input("Enter the grade number: "))
print()

# Validity check

if 4 <= grade_num <= 10:

    # Grade corresponding to the input.
    if grade_num == 10:
        print("Your grade is 'A+' and Outstanding Performance")
    elif grade_num == 9:
        print("Your grade is 'A' and Excellent Performance")
    elif grade_num == 8:
        print("Your grade is 'B+' and Very Good Performance")
    elif grade_num == 7:
        print("Your grade is 'B' and Good Performance")
    elif grade_num == 6:
        print("Your grade is 'C+' and Average Performance")
    elif grade_num == 5:
        print("Your grade is 'C' and Below Average Performance")
    else:
        print("Your grade is 'D' and Poor Performance")

else:

# If grade is invalid
    print("grade is Invalid.")
    
print("\n")



#Question - 5

print("Q 5")


alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

for row in range(0,6):
    
    column=0
    counter=0
    while column<11:
        
        if column<row or column>11-row-1:
            print(" ", end="")

        else:
            print(alphabets[counter], end="")
            counter=counter+1
        column=column+1
        
    print("")
    



#Question - 6 

print("Q6")
                  
# 1st run
repeat="Y"
                  
# Empty dictionary

dic={}
dic2={}
                  
# List containing Y or N

liste=["Y","y","n","N"]
                  
# Main code
while repeat=="Y" or repeat=="y":
    # Taking input name and sid from the user
    
    
    name = str(input("Enter student name:"))
    
    sid = int(input("Enter student SID:"))
    
    if sid<0:
        print("\nError\nSID can't be negative\n")
        
    else:
        # Updating dictionary with 'sid':'name'
        
        dic.update({sid: name})
        
        # Updating dictionar 2 with 'name':'sid'
        
        dic2.update({name:sid})
        # Asking if want to enter more input or not
        

        repeat = str(input("Enter Y to continue or N to end:"))
    if repeat=="N" or repeat=="n":
        break

    elif (not (repeat in liste)):
        print("\nError\nPlease enter valid input['Y' or 'N']")
        
        repeat=str(input("\nEnter Y to continue or N to end:"))

# a

# Printing the dictionary

print("\n Question 6(a) \n")

print("The Dictionary containing {'SID':'Name'} is shown below")
print(dic)

# b

# Sorting according to name

print("\n Question 6(b) \n")
list_k=sorted(dic2)
dic3={}

for ele in list_k:
    dic3.update({dic2.get(ele):ele})
    
print("The Dictionary after sorting according to name:")

print(dic3)

# c

# Sorting according to SID

print("\n Question 6(c) \n")
sort_dic = sorted(dic)

dic4 = {}
for va in sort_dic:
    dic4.update({va: dic.get(va)})
    
print("The Dictionary after sorting according to SID:")
print(dic4)

# d

print("\n Question 6(d) \n")
# Taking input SID to be searched
enter_sid = int(input("Enter SID to get name of student:"))

# Searching for sid as key in dic
output_name = str(dic.get(enter_sid))
# Printing name with key sid

print(f"Name of student with SID {enter_sid} is {output_name}.")
print("\n")



#QUESTION - 7

print(" Q 7")

number=int(input("Total elements of Fibonacci sequence that you want(must be greater than 1)- "))

#using the formula of the sum of previous two terms is equal to the present term.
a_n1=1
a_n2=0
n=0
#initializing sum with first two terms

sum=a_n1+a_n2

#printing the initial two terms as the recursion is not valid on them

print(f"Fibonnaci sequence with {number} terms")
print(a_n2)

print(a_n1)

#Printing the remaining fibonnaci terms
while n<number-2:
    
    a_n=a_n2+a_n1
    
    a_n2=a_n1
    
    a_n1=a_n
    
    print(a_n)
    
    n=n+1
    
    sum+=a_n
#printing the program end prompt
    
print(f"Sum of total {number} terms of sequence is {sum}")
print("END")



#Question - 8 

print(" Q 8")

# Given sets

Set1= {1, 2, 3, 4, 5}

Set2= {2, 4, 6, 8}

Set3= {1, 5, 9, 13, 17}

# Intersection of set 1 & 2 is to be subtracted from union of both sets

print("\n Question 8(a) \n")

set_notboth=Set1^Set2

print(f"set with elements not common in both is {set_notboth}")

# Intersection of three sets and 2 at a time to be subtracted from total union of these three sets

print("\n Question 8(b) \n")

set_onlyinone=Set1^Set2^Set3

print(f"Set of elements that is only present in one set is {set_onlyinone}")

# Intersection of two at a time and subtract intersection of three of these sets

print("\n Question 8(C) \n")

set_onlyintwo=(Set1|Set2|Set3)-(Set1^Set2^Set3)-(Set1&Set2&Set3)

print(f"Set of elements that is only present in two set is {set_onlyintwo}")

# Simply we write 1-10 and subtract set 1 from this

print("\n Question 8(d) \n")

new_set1=set()
for n in range(1,11):
    new_set1.add(n)
    
not_common_1=new_set1- Set1


print(f"set of all integers in the range 1 to 10 that are not in Set1 {not_common_1}")

# Simply we write 1-10 and subtract set 1,2,3 from this

print("\n Question 8(e) \n")

new_set2=set()
for n in range(1,11):
    new_set2.add(n)
    
not_common_2=new_set2 - (Set1|Set2|Set3)


print(f"set of all integers in the range 1 to 10 that are not in Set1 and Set2 and Set3 {not_common_2}")
