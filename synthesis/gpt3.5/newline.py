# Prompt the user for input
user_input = input("Enter a string: ")

# Add a character 'x' at the end of the input string
user_input += 'x'

# Check if the last character is 'x'
if user_input[-1] == 'x':
        print("The string ends with 'x'")

        # Check if the second-to-last character is a newline
        if user_input[-2] == '\n':
                print("The string ends with a newline character")
