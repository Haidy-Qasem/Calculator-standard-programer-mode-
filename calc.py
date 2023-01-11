





while True:
	
	print("For Standard Mode Press 1")
	print("For Programmer Mode Press 2")
	print("For Exit Press c")
	Mode=input("Enter your Mode")
	if Mode=='c':
		break
	elif Mode== '1' :
		
		print("1.Add")
		print("2.Subtract")
		print("3.Division")
		print("4.Multiply")
		operation=int(input("enter your operation\n"))	
		a= float(input('enter num1\n'))
		b= float(input("enter num2\n"))
		if operation == 1:
		   sum1=a+b
		   print(sum1)
		   		   
		elif operation == 2:
		   sub1=a-b
		   print(sub1)   
		elif operation == 3:
		   if b== 0 :
			   print("Error")
		   else :
			   div1=a/b

			   print(div1)  
		elif operation == 4:
		   mul1=a*b
		   print(mul1)
		else:
			print("Invalid Choice")
	elif Mode== '2' :
		print("1.Add")
		print("2.Subtract")
		print("3.Division")
		print("4.Multiply")
		print("5.decimal to binary")
		print("6.binary to decimal")
		print("7.decimal to hexa")
		print("8.hexa to deciaml")
		print("9.decimal to octal")
		print("0.octal to decimal")
		operation=int(input("enter your operation\n"))
		
		
		if operation == 1:
			a= int(input('enter num1\n'))
			b= int(input("enter num2\n"))
			sum=a+b
			print(bin(sum))
			   
		elif operation == 2: 
			a= int(input('enter num1\n'))
			b= int(input("enter num2\n"))
			sub=a-b
			print(bin(sub))   
		elif operation == 3:
			a= int(input('enter num1\n'))
			b= int(input("enter num2\n"))
			if b== 0 :
				print("Error")
			else :
				div=a/b
				print(bin(div))  
		elif operation == 4:
			a= int(input('enter num1\n'))
			b= int(input("enter num2\n"))
			mul=a*b
			print(bin(mul))
		elif operation == 5:
			num = int(input('Enter your number:'))
			print(num,"=" ,bin(int(num)))
		elif operation == 6:
			num = int(input('Enter your number: '))
			print(num, "=", int(str(num), 2))
		elif operation == 7:
			num = int(input('Enter your number: '))
			print(num,"=" ,hex(int(num)))
		elif operation == 8:
			num = int(input('Enter your number: '))
			print(num, "=" ,int(str(num), 16))
		elif operation == 9:
			num = int(input('Enter your number: '))
			print(num, "=" ,oct(int(num)))
		elif operation == 0:
			num = int(input('Enter your number: '))
			print(num,"=" ,int(str(num),8)) 

		else:
			print("Invalid Choice")

	else:
			print("Invalid Choice")
