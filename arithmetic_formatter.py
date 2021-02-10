def printer(res,get_ans):
	result = ''
	for elt in res:
		len_ = max(len(str(elt[0])),len(str(elt[2]))) + 2
		str_ = ( (len_ - len(str(elt[0]))) * ' ') + str(elt[0])+ '    '
		if elt == res[len(res)-1]:
			str_ =  (len_ - len(str(elt[0]))) * ' ' + str(elt[0]) 
		result = result + str_
	result = result + '\n'
	for elt in res:
		len_ = max(len(str(elt[0])),len(str(elt[2])))+1	
		for x in elt[1:]:
			if x == "+":
				result = result + '+'
			elif x == "-":
				result = result + '-'
			else:
				str_ =  (len_ - len(str(elt[2])) ) * ' ' + str(x) +'    '
				if elt == res[len(res)-1]:
					str_ =  (len_ - len(str(elt[2]))) * ' ' + str(x) 
				result = result + (str_)
				break
	result = result + '\n'
	for elt in res:
		len_ = max(len(str(elt[0])),len(str(elt[2])))+1
		result = result + ('-' * (len_ +1))
		if elt != res[len(res)-1]:
			result = result+ '    '
	result = result + '\n'
	if get_ans == True:
		for elt in res:
			len_ = max(len(str(elt[0])),len(str(elt[2])))+2
			
			for x in elt[3:]:
				str_ = (len_ - len(str(elt[3]))) * ' '+ str(x) +'    '
				if elt == res[len(res)-1]:
					str_ = (len_ - len(str(elt[3]))) * ' ' + str(x) 
				result = result + str_
	return(result)	

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
	if len(str(x1)) > 4 or len(str(x2)) > 4:
		return('Error: Numbers cannot be more than four digits.')
	if operation == "+":
		liste = [x1,'+',x2]
		if(ans == True):
			liste.append(x1+x2)
			return(liste)
		return(liste)
	elif operation == "-":
		liste = [x1,'-',x2]
		if(ans == True):
			liste.append(x1-x2)
			return(liste)
		return(liste)
	else:
		 return('Error: Operator must be \'+\' or \'-\'.')

def arithmetic_arranger(problems,get_ans = False):
	error = liste_len(problems)
	affichage = []
	if error == 0:
		return("")
	for x in problems:
		res = x.split()
		if not(isinstance(get_solution(res[0],res[1] ,res[2],get_ans),list)):
			return(get_solution(res[0],res[1] ,res[2],get_ans))
		affichage.append(get_solution(res[0],res[1] ,res[2],get_ans))
	return printer(affichage,get_ans)
