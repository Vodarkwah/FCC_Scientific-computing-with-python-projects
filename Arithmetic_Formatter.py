import re       #imports the regex library


def arithmetic_arranger(arith_list, solution=True):
    
    first_num=[]            # collects data from arith_list into a list 'firstnum'
    operator=[]
    second_num=[]
    dashes=[]
    total=[]

    if len(arith_list)>5:           # Items shouldnt be more than 5
        return 'Error: Too many problems.'

    for expr in arith_list: # for every expression in arith_list
        
        # FILTERING SRITERIA
        if re.search('[^\s0-9.+-]',expr): # Looking for the char in the list stated
            if re.search('[/]',expr) or re.search('[*]', expr):  # if '/' or '*' char in list return error
                return "Error: Operator must be '+' or '-'."
            return ' Error: Numbers must only contain digits.' # error for all other conditions

        
        first_num.append(expr.split(' ')[0]) # collects the first no of every iterated variable
        operator.append(expr.split(' ')[1])
        second_num.append(expr.split(' ')[2])
        
        # CRITERIA FOR LENGTH CHECKING
        if len(first_num) or len(second_num) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        # ADDITIION AND SUBTRACTION CRITERIA
        if operator == '+':
            sum = str(int(first_num) + int(second_num))
        elif operator == '-':              # you can also use "elif operator == '-'"
            sum = str(int(first_num) - int(second_num))

        total.append(sum)       # Collects all the summed data into list file 'Total'
        
        
        # Construction of the arranger

        length = max(len(first_num), len(second_num))         # returns the largest of the 2 arguments
        top  = str(first_num).rjust(length)         
        down = operator + " " +str(second_num).rjust(length-1)  # lenght - 1 because the operator will also take space

        dashes = ""
        for l in range(length):
            dashes += '-'    # increment of varible '-' until iteration is complete
        
        #  CREATION OF SPACE BETWEEN 2 OR MORE PROBLEMS/ENTRIES
        upper_exp = ""
        lower_exp = ""
        hyphen_exp =""
        sum_exp = ""

        if expr != arith_list[-1]:  # if iter val != the last item in list repeat no + spaces
            upper_exp += top + "    "
            lower_exp += down + "    "
            hyphen_exp += dashes + "    "
            sum_exp += sum + "    "
            
        else:                       # if expr = the last item in arith_list, just repeat the numbers
            upper_exp += top 
            lower_exp += down 
            hyphen_exp += dashes 
            sum_exp += sum 

    if solution:
        arranged_problem = upper_exp +'\n' + lower_exp + '\n' + hyphen_exp + '\n' + sum_exp 
    else:
        arranged_problem = upper_exp +'\n' + lower_exp + '\n' + hyphen_exp  
    return arranged_problem




#arithmetic_arranger(['32 + 8', '1 - 3801', '9999 + 9999', '523 - 49'], True)
#arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])