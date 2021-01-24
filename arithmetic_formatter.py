def printer(res,get_ans):
	for elt in res:
		len_ = max(len(str(elt[0])),len(str(elt[2])))+2
		str_ = '%'+ str(len_) +'d'+ '    '
		if elt == res[len(res)-1]:
			str_ = '%'+ str(len_) +'d'
		print(str_ % elt[0] ,end = '')
	print('')
	for elt in res:
		len_ = max(len(str(elt[0])),len(str(elt[2])))+1
		str_ = '%'+ str(len_) +'d'+'    '
		if elt == res[len(res)-1]:
			str_ = '%'+ str(len_) +'d'
		for x in elt[1:]:
			if x == "+":
				print('+', end = '')
			elif x == "-":
				print('-', end = '')
			else:
				print(str_ % x ,end = '')
				break
	
	print('')
	

	for elt in res:
		len_ = max(len(str(elt[0])),len(str(elt[2])))+1
		
		print('-' * (len_ +1),end = '')
		if elt != res[len(res)-1]:
			print('    ',end='')
	if get_ans == True:
		print('')
		for elt in res:
			len_ = max(len(str(elt[0])),len(str(elt[2])))+2
			str_ = '%'+ str(len_) +'d'+'    '
			if elt == res[len(res)-1]:
				str_ = '%'+ str(len_) +'d'
			for x in elt[3:]:
				print(str_ % x ,end = '')		

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
		print('Error: Numbers must only contain digits.')
		return(0)
	if len(str(x1)) > 4 or len(str(x2)) > 4:
		print('Error: Numbers cannot be more than four digits.')
		return(0)
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
		 print('Error: Operator must be '+' or '-'.')
		 return(0)

def arithmetic_arranger(problems,get_ans = False):
	error = liste_len(problems)
	affichage = []
	if error == 0:
		return("")
	for x in problems:
		res = x.split()
		if get_solution(res[0],res[1] ,res[2],get_ans)== 0:
			return
		affichage.append(get_solution(res[0],res[1] ,res[2],get_ans))
	return printer(affichage,get_ans)
