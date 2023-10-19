# function to find the average of two numbers
def average_of_two_numbers(x, y):
    average = 0
    for value in x, y:
        average += value/(2)
    return average
print(average_of_two_numbers(50,70))
    
        
    

#ii)   
# program that allows user input and finding the minimum number
python_mark = int(input("Enter python mark:"))
html_mark = int (input("Enter html mark:"))
java_mark = int(input("Enter java mark:"))
if python_mark<html_mark and python_mark<java_mark:
    print(f"{python_mark} is the minimum number")
elif html_mark<python_mark and html_mark<java_mark:
    print(f"{html_mark} is the minimum number")
else:
    print(f"{java_mark} is the minimum number")