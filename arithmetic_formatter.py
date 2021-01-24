
def problem_len(problems):
	len_ = len(problems)
	if len_ > 5:
		print("Error: Too many problems.")
	return(0)
def get_solution(x1,operation ,x2,ans = False):
	if operation == "+":
		if(ans == True):
			return(x1 + x2)
		return
	elif operation == "-":
		if(ans == True):
			return(x1 - x2)
		return
	else:
		 return("Error: Operator must be '+' or '-'.")

def arithmetic_arranger(problems,get_ans = False):

	error = problem_len(problems)
	if error == 0:
		return("")
	arranged_problems = problems
	return arranged_problems[1]
	

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49","123 + 49","123 + 49"]))
print(get_solution(1,"5",2))