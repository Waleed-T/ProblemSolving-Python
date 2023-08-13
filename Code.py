#Exercise 1: DVD Club Points

#A Video club that awards points to its customers based on the number of videos
#purchased each month. The points are awarded as follows:

#   • If a customer purchases 0 dvd’s, the earning is 0 points
#   • If a customer purchases 1 dvd, the earning is 5 points
#   • If a customer purchases 2 dvd’s,the earning is 15 points
#   • If a customer purchases 3 dvd’s, the earning is 30 points
#   • If a customer purchases 4 or more dvd’s, the earning is 60 points

#Write a program that asks the user to enter the number of videos that he or she
# has purchased this month, then displays the number of points awarded.

#Solution:

number_of_dvds = int(input("Enter the number of dvds: "))
toast = ""
#using input function to set a prompt for the user to enter required no. of DVDs and then converting the value into an
#integer value for python to recognize it as such and use it accordingly. In the second line, we are just sampling a
#toast format that will be repopulated based on the conditions mentioned below


if number_of_dvds < 0:
    toast = "Error. Enter a positive number. \n" + \
              "Re-run program and try again."
else:
    toast = "You are awarded "

    if number_of_dvds >= 0 and number_of_dvds < 1:
        toast += "0 "
    elif number_of_dvds >= 1 and number_of_dvds < 2:
        toast += "5 "
    elif number_of_dvds >= 2 and number_of_dvds < 3:
        toast += "15 "
    elif number_of_dvds >= 3 and number_of_dvds < 4:
        toast += "30 "
    elif number_of_dvds >= 4:
        toast += "60 "

#using conditional statements along with the action statements to deal with different scenarios

    toast += "points."

#using the addition assignment operator here to add the value of the right operand to the toast variable and
#assign the result to the toast variable

print(toast)

#printing the resultant value of the toast variable as affected by the conditional statements above

#------------------------------
 
#Exercise 2: BMI

#Write a program that calculates the BMI ( Body Mass Index ) for a user.
#Let the program ask the user for needed input:
 #   • the weight ( in kg )
#    • the height ( in meter )

#Then, display the BMI value on the screen with a message.
#The message depends on the BMI index, if the person is:
#Under weight: < 18.5
#Normal weight: 18.5 - 24.99
#Over weight: 25.0 - 29.99
#Obesity: BMI of 30 or greater
#Formula: BMI = weight / (height**2)

#Solution:

weight_in_kgs= float(input("Please enter your weight in kgs: "))
height_in_mtrs= float(input("Please enter your height in mtrs: "))

#deploying an input function to take input from the user in terms of weight and height and then applying float function
#on top in order to convert the resultant value to floating point value (decimal value)

BMI = round((weight_in_kgs / (height_in_mtrs**2)),2)

#using the weight and height values extracted from the input functions above and using them in the BMI formula with the
#resultant value rounded to two decimal places

print(f"Your BMI value is {BMI}")

if BMI < 18.5:
    print("You are underweight")
elif BMI >= 18.5 and BMI<=24.99:
    print("You have a normal weight")
elif BMI >= 25 and BMI<=29.99:
    print("You are over weight")
elif BMI >= 30:
    print("You are obese")

#concluding health status after applying conditional values

#------------------------------
 
#Exercise 3: Property Tax

#A county collects property taxes on the assessment value of property, which is 60 percent of the property’s
#actual value

#For example, if an acre of land is valued at $10,000, its assessment value is $6,000

#The property tax is then 72¢ for each $100 of the assessment value. The tax for the acre assessed at $6,000 will
#be $43.20

#Write a program that asks for the actual value of a piece of property and displays the assessment value and
#property tax.

#Solution:

actual_land_value= float(input("Please enter land value in USD: "))

#prompting the user to enter the actual value of the land using input function and convering it into floating point value
#and then storing the value in the "actual_land_value" variable

assessment_value=round((actual_land_value*0.60),1)

#determining the assessment value from the actual value of the land and rounding it to 1 decimal point using round function
#and then storing the value in the "assessment_value" variable

property_tax=round((assessment_value*(0.72/100)),1)

#calculating the property tax payable by simply applying the mathematical formula described in the requirement and rounding
#subsequently and then storing the value in the "property_tax" variable

print(f"Your land assessment value is ${assessment_value}")
print(f"Your property tax payable is ${property_tax}")

#displaying the value of the above calculated variables in combination of the f-string method

#------------------------------
 
#Exercise 4: Sum of Numbers

#Write a program using a while loop and within the loop asks the user to enter a series of positive numbers

#The user should enter a negative number to signal the end of the series

#After all the positive numbers have been entered, the program should display their sum

#Solution:

sum = 0
number = 1

#declaring variables

while number > 0:
    number = int(input('Please enter a positive number here: '))
    if number > 0:
        sum = sum + number
print("The summation of all the positive numbers entered above, (excluding negative numbers) is", sum)

#simply using while loop in combination with conditional statement while prompting user to repeatedly enter positive
#numbers and breaking the loop upon entering a negative number and in the end printing the sum upon break of the operation

#------------------------------
 
#Exercise 5: Maximum of Two Values

#Write a function named my_max that accepts two integer values as arguments and returns the value that is the greater
#of the two

#For example, if 12 and 19 are passed as arguments to the function, the function should return 19.

#Use the function in a program that prompts the user to enter two integer values
#The program should display the value that is the greater of the two

#Solution:

#1st method with user defined input values

x = int(input("Enter first value: "))
y=  int(input("Enter second value: "))

#defining 'x' and 'y' variables

def my_max(x, y):
    if x >= y:
        return x
    else:
        return y

#defining the "my_max" function with 'x' and 'y' as arguments and applying conditional statements associated with an action

#print(my_max(x, y))

print(f"The highest value of the two integers is {my_max(x, y)}")

#displaying the maximum value variable using print function and f-string on 'my_max' variable

"""2nd method with user defined input values"""

print("2nd method")

x = int(input("Enter first value: "))
y=  int(input("Enter second value: "))

#defining 'x' and 'y' variables using input function

my_max = max(x, y)

#using max function here to pick the maximum value of the two integers

print(f"The highest value of the two integers is {my_max}")

#using the 'max' function on 'x' and 'y' arguments and storing them in 'my_max' variable and then displaying the
#maximum value using print function along with f-string

#------------------------------
 
#Exercise 6: Test Average and Grade

#Write a program that asks the user to enter five test scores. The program should display a letter grade
#for each score and the average test score. Write the following functions in the program:

#   • calc_average This function should accept five test scores as arguments
#     and return the average of the scores

#   • determine_grade This function should accept a test score as an argument and return a letter grade for
#     the score based on the following grading scale:

#Score Letter Grade
#   90-100 A
#   80-89 B
#   70-79 C
#   60-69 D
#   Below 60 F

#Solution:

def calc_average(compiled_list):
    total=0
    for x in compiled_list:
        total+=x
    average=total/len(compiled_list)
    return average

#creating 'calc_average' function with a loop of 'compiled_list' and calculating the average

def determine_grade(compiled_average):
    average="F"
    if compiled_average>=90:
        average="A"
    elif compiled_average>=80 and compiled_average<=89:
        average="B"
    elif compiled_average >= 70 and compiled_average <=79:
        average = "C"
    elif compiled_average>=60 and compiled_average<=69:
        average="D"
    elif compiled_average<=89:
        average="F"
    return average

#defining 'determine_grade' and combining it with conditional statements to cover the entire grading criteria

compiled_list=[]

while (True):
    scores=input ('Please enter the test scores here to find the grade awarded and say "stop" to find the grade: ')

    if scores=="stop":
        break
    compiled_list.append(float(scores))

#this statement creates conditional to break the operation of prompting for the next scores with the word stop and then
#appending to the compiled_list with floating point value of scores

compiled_average=calc_average(compiled_list)
letter_grade=determine_grade(compiled_average)

print(("The student's cumulative average is ") + str(compiled_average) + ' and received a/an ' + str(letter_grade) + " in this course")

#displaying the 'compiled_average' and 'letter_grade' with a a predefined print command format

#------------------------------
