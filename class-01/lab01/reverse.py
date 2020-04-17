from textwrap import dedent
user_prompt = "** Enter any numbers separated by comma **\n"
output_text = "** Here is your output in reverse order **\n"

def reverse(user_input):
    input_list = user_input.split(",")   
    output_string = "" 
    while len(input_list) !=  0:
        output_string += input_list.pop() + ","
    return output_string
    
if __name__ == "__main__":    
    input_numbers = input(dedent(user_prompt))
    output_string = reverse(input_numbers)
    print(output_text, output_string.rstrip(","))

