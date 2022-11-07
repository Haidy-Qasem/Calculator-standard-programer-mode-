


while True:
	
	print("For Standard Mode Press 1")
	print("For Programmer Mode Press 2")
	print("For Exit Press c")
	Mode=input("Enter your Mode")
	if Mode=='c':
		break
	if Mode== '1' :
		a= float(input('enter num1\n'))
		operation=input("enter your operation\n")
		b= float(input("enter num2\n"))
		if operation == "+":
		   sum=a+b
		   print(sum)
		   
		if operation == "-":
		   sub=a-b
		   print(sub)   
		if operation == "/":
		   if b== 0 :
			   print("Error")
		   else :
			   div=a/b

			   print(div)  
		if operation == "*":
		   mul=a*b
		   print(sum)
	if Mode== '2' :
		a= int(input('enter num1\n'))
		operation=input("enter your operation\n")
		b= int(input("enter num2\n"))
		if operation == "+":
			   sum=a+b
			   print(bin(sum))
			   
		if operation == "-": 
		   sub=a-b
		   print(bin(sub))   
		if operation == "/":
		   if b== 0 :
			   print("Error")
		   else :
			   div=a/b

			   print(bin(div))  
		if operation == "*":
		   mul=a*b
		   print(bin(mul))



