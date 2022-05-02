#ID=29467721
def tokenization(exp):
    """This function will return the math formula as a single list.
    
    Input:
        string_formula {str} : The string formula to convert
    Returns:
        {list} : The list of the formula converted.
    """
    
    math_stuff = ['+', '-', '/', '*', '^', '(', ')']
    num_stuff = '0123456789.'
    # used to store the final output
    output = []
    # used to accumulate numbers before converting to float
    acc = ''
    # loop for each character
    for char in exp:
        # now we must decide if it's added to output
        # or accumulates into a float!
        if char in math_stuff:
            # flush acc if it has anything
            if acc:
                output.append(float(acc))
                acc = ''
            # add the math symbol to the output
            output.append(char)
        elif char in num_stuff:
            #accumulate the math stuff
            acc += char
        else:
            pass
    # return our list
    return output
        
print(tokenization("(3.1 + 6*2^2) * (2 - 1)"))

def has_precedence(op1,op2):
    operators = "^*/-+"
    return operators.index(op1) < operators.index(op2)
    
#print(has_precedence("+","/"))

def highest_operator(expression):
    operators = " ^*/-+ "
    for operator in operators:
        if operator in expression:
            return expression.index(operator)
        
   
def solve(x, operator, y):
    """calculates a single operation"""
    if operator == '+':
        return x + y
    if operator == '-':
        return x - y
    if operator == '*':
        return x * y
    if operator == '/':
        return x / y
    if operator == '^':
        return x ** y
        
def simple_evaluation(expression):
    if len(expression) == 1:
        return expression[0]
    result=[]
    while len(expression) > 1:
        
        operator_index = highest_operator(expression)
        
        operator_char = expression[operator_index]
        left_int = expression[operator_index - 1]
        right_int = expression[operator_index + 1]
        
        result = solve(left_int, operator_char, right_int)
        
        expression[operator_index - 1 : operator_index + 2]=[result]
        
    return float(result)

#print(simple_evaluation([2, "+", 3, "*", 4, "^", 2, "+", 1]))

       
def complex_evaluation(expression): 

    while "(" in expression:
        start = expression.index("(")
        end = expression.index(")")
        sub_l = expression[start+1:end]
        
        if "(" in sub_l:
            #("Dealing with nested Brackets here!")
            open_brackets = sub_l.count("(")
            s = end
            while open_brackets > 0:
                s = expression.index(")", s+1)
                if "(" in expression[end+1:s]:
                    open_brackets += 1
                end = s
                open_brackets -= 1
            sub_l = [complex_evaluation(expression[start+1:s])]

        expression[start:end+1] = [simple_evaluation(sub_l)]        
        #print(expression)
    while len(expression) > 1:
        operator_index = highest_operator(expression)
        operator_char = expression[operator_index]
        left_int = expression[operator_index - 1]
        right_int = expression[operator_index + 1]
        result = solve(left_int, operator_char, right_int)
        
        expression[operator_index - 1 : operator_index + 2]=[result]
        
    if len(expression) == 1:
        result =  expression[0]
    return float(result)

#print(complex_evaluation(["(",4,"^",3,")","^",2]))
#print(complex_evaluation(["(","(", 2, "-", 7, ")", "*", 4, "^", "(", 2, "+", 1, ")","+",3,"*","(",2, "-", 7,")","-",5,")"]))
#print(complex_evaluation(["(", 2, "-", 7, ")", "*", 4, "^", "(", 2, "+", 1, ")","/",4]))
    
#print(complex_evaluation(["(","(", 2, "-", 7, ")", "*", 4, "^", "(", 2, "+", 1, ")","+",3,"*","(",2, "-", 7,")","-",5,")"]))
#print(complex_evaluation(["(", 2, "-", 7, ")", "*", 4, "^", "(", 2, "+", 1, ")","+",4]))
#print(complex_evaluation(["(", 2, "-", 7, ")", "*", 4, "^", "(", 2, "+", 1, ")","+","(",4,"*",4,")"]))
#print(complex_evaluation(["(",-3,"*","(", 2, "-", 7, ")", "*", 4, "^", "(", 2, "+", 1, ")","-",45,")"]))
#print(complex_evaluation(["(",3,"*","(",2, "-", 7,")","-",5,")","/","(",3,"*","(",2, "-", 7,")","-",5,")"]))

def evaluation(expression):
    Tokenized_expr=tokenization(expression)
    Ans=complex_evaluation(Tokenized_expr)
    
    return float(Ans)
#print(evaluation("((2-70)*4^(2+1) +( 1+4))"))
#print(evaluation("((2-70)*4^(2+1) +( 1+4)+8)"))
#print(evaluation("((4^3)^2 )"))


#ID=29467721




