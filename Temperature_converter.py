#Temperature converter 


from termcolor import colored # Importing the termcolor module to add colors to the output.

def c2f(c): # Defining function named c2f(celcius to fahrenheit) which takes 1 argument c.
    f = c*(9/5)+32 
    return f 

def f2c(f): # Defining function named f2c(fahrenheit to celcius) which takes 1 argument f.
    c = 5*(f-32)/9 
    return c 

def create_dialog(title): # Defining a function named create_dialog which takes 1 argument title
    length = len(title) # Calculating the length of the title
    dashes = '-'*(length+12) # Creating a string of dashes based on the length of the title
    spaces2 = ' '*(length+12)
    spaces = ' '*((len(dashes)-length)//2) # Creating a string of spaces to center the title
    
    print(colored(f'''
    |{dashes}|   
    |{spaces2}|  
    |{spaces}{title}{spaces}| 
    |{spaces2}|
    |{dashes}|
            ''','green' )) 
    # Printing the top border with dashes.
    # Printing an empty line with spaces.
    # Printing the title with spaces on both sides.
    # Using green color for the output.

def main():
    create_dialog('Temperature Converter')
    print(colored('''
    Please Select Your Tool:
    1. Fahrenheit to Celcius
    2. Celcius to Fahrenheit
    3. Exit
                  ''','cyan'))
    choice = int(input(colored('Your choice: ','yellow'))) # Printing a message to ask for user’s choice
    
    
    if choice==1:
        create_dialog("Fahrenheit to Celcius")
        fahrenheit = float(input(colored("Enter the temperature in fahrenheit: ",'light_red')))
        result=f2c(fahrenheit) # calling the funtion(Fahrenheit to Celcius) and storing it in result.
        print(colored(f"The temperature in Celcius is {result}",'magenta')) # printing the result
        
    elif choice == 2:
        create_dialog("Celcius to Fahrenheit")
        celcius = float(input(colored("Enter the temperature in celcius: ",'light_red')))
        result=c2f(celcius) # calling the function(Celcius to Fahrenheit) and storing it in result.
        print(colored(f"The temperature in Fahrenheit is {result}",'light_cyan')) # printing the result.
        
    elif choice == 3:
        print(colored('Thanks For Using My Tool','cyan'))
        exit(0)
        # Exiting the program with code 0 (no error)
    else:
        # If none of the choices match, then
        main()
        # Calling the main function again to repeat the process
        
if __name__=="__main__":
     # Checking if this file is run directly and not imported from another file
    main()
    # Calling the main function