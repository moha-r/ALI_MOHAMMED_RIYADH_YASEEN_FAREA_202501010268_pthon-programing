choice = "y"

# Iteration: Loop continues as long as user enters 'y'
while choice.lower() == "y":
    
    # Inputs: Getting the 3 quiz marks from the user
    quiz_1 = float(input("Enter Quiz 1 mark: "))
    quiz_2 = float(input("Enter Quiz 2 mark: "))
    quiz_3 = float(input("Enter Quiz 3 mark: "))
    
    # Process: Calculating the average
    average = (quiz_1 + quiz_2 + quiz_3) / 3
    
    # Output: Displaying the average
    print(f"The average mark is: {average:.2f}")
    
    # Selection: Checking if the student passes or fails
    if average >= 50:
        print("Status: Pass")
    else:
        print("Status: Fail")
        
    # Input: Asking if the user wants to continue
    choice = input("Continue? Select Y/N: ")

print("Program Ended")
