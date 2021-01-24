def printer(res):
	
	for elt in res:
		len_ = max(len(str(elt[0])),len(str(elt[2])))+2
		str_ = '%'+ str(len_) +'d'
		print(str_ % elt[0])
	for elt in res:
		len_ = max(len(str(elt[0])),len(str(elt[2])))+1
		str_ = '%'+ str(len_) +'d'
		for x in elt[1]:
			if x == "+":
				print('+', end = '')
			elif x == "-":
				print('-', end = '')
			else:
				print(str_ % x)
	print('-' * (len_ +1))
			

def liste_len(problems):
	len_ = len(problems)
	if len_ > 5:
		print("Error: Too many problems.")
		return(0)
	return(1)
def get_solution(x1,operation ,x2,ans = False):
	liste = []
	try:
		x1 =	int(x1)
		x2 =	int(x2)
	except:
		return('Error: Numbers must only contain digits.')
	if len(str(x1)) > 4 and len(str(x2) > 4):
		return('Error: Numbers cannot be more than four digits.')
	if operation == "+":
		liste = [x1,'+',x2,'-']
		if(ans == True):
			liste.append(x1+x2)
			return(liste)
		return(liste)
	elif operation == "-":
		liste = [x1,'-',x2,'-----']
		if(ans == True):
			liste.append(x1-x2)
			return(liste)
		return(litse)
	else:
		 return("Error: Operator must be '+' or '-'.")

def arithmetic_arranger(problems,get_ans = False):
	error = liste_len(problems)
	affichage = []
	if error == 0:
		return("")
	for x in problems:
		res = x.split()
		affichage.append(get_solution(res[0],res[1] ,res[2],get_ans))
	return affichage

print(arithmetic_arranger(["32 - 6698","12 + 6698"],True))
printer([[1,'+',234]])