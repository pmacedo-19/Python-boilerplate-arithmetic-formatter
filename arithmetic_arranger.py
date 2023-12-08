def arithmetic_arranger(problems, calc=None):
    arranged_problems = []
    if (len(problems) > 5):
        return "Error: Too many problems."

    else:
        results_list = []
        x = 0
        # Split the problems into lists of numbers and operators
        for problem in problems:
          p_list = problem.split(' ')
          
          # Error Check
          if p_list[0].isdigit() is False or p_list[2].isdigit() is False:
            return "Error: Numbers must only contain digits."
          if p_list[1] != "+" and p_list[1] != "-":
            return "Error: Operator must be '+' or '-'."
          if len(p_list[0]) > 4 or len(p_list[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

          # Making operations
          if p_list[1] == "+":
            x = int(p_list[0]) + int(p_list[2])
          if p_list[1] == "-":
            x = int(p_list[0]) - int(p_list[2])

          # Better variable names for the display process organization
          number1 = int(p_list[0])
          number2 = int(p_list[2])
          n1_len = len(p_list[0])
          n2_len = len(p_list[2])
          x_len = len(str(x))
          
          # Calculate the results 
          if isinstance(calc, bool):
                       
            if n1_len > n2_len:
              results_list.append(' ' * 2 + str(number1) + '\n' + p_list[1][0] + ' ' * (n1_len - n2_len + 1) + str(number2) + '\n' + '-' * (n1_len + 2) + '\n' + ' ' * (n1_len - x_len + 2) + str(x))  
            else: 
              results_list.append(' ' * (n2_len - n1_len + 2) + str(number1) + '\n' + p_list[1][0] + ' ' + str(number2) + '\n' + '-' * (n2_len + 2) + '\n' + ' ' * (n2_len - x_len + 2) + str(x))

          # Just print the results
          else:
            if n1_len > n2_len:
              results_list.append(' ' * 2 + str(number1) + '\n' + p_list[1][0] + ' ' * (n1_len - n2_len + 1) + str(number2) + '\n' + '-' * (n1_len + 2))
            else: 
              results_list.append(' ' * (n2_len - n1_len + 2) + str(number1) + '\n' + p_list[1][0] + ' ' + str(number2) + '\n' + '-' * (n2_len + 2))

        # Split each string based on newline character '\n'
        separated_results = [result.split('\n') for result in results_list]
        
        # Transpose the list to print each element in the first line and so on
        transposed_results = ['    '.join(line) for line in zip(*separated_results)]
        
        # Add each line to the arranged_problems list
        arranged_problems = '\n'.join(transposed_results)

    return arranged_problems