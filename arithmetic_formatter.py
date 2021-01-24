
def liste_len(problems):
	len_ = len(problems)
	if len_ > 5:
		print("Error: Too many problems.")
		return(0)
	return(1)
def get_solution(x1,operation ,x2,ans = False):
	try:
		x1 =	int(x1)
		x2 =	int(x2)
	except:
		return('Error: Numbers must only contain digits.')
	if len(str(x1)) and len(str(x2)):
		return('Error: Numbers cannot be more than four digits.')
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
	error = liste_len(problems)
	
	if error == 0:
		return("")
	res = problems[0].split()

	return get_solution(res[0],res[1] ,res[2],get_ans)
	

print(arithmetic_arranger(["32 + 6698"],True))
#print(get_solution(1,"+",2))