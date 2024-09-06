#question 1 task 1

try:
    temperature_input = float(input("What is the temperature in Farhrenheit: "))

#question 1 task 2
            
    Celsius = (temperature_input - 31) * 5/9
except ValueError:
    print("Please enter a temperature only in numbers.")

#question 1 task 3
        
else:
    print(f"{temperature_input} degrees Fahrenheit is {Celsius} degrees Celsius.")

#question 1 task 4
        
finally:
    print("Thank you for using this weather application. Have a good day.")