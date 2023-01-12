#Q3.1 Calculate the multiplication and sum of two numbers:
number1 = 20
number2 = 30
print("The result is ", number1 * number2)

number1 = 40
number2 = 30
print("The result is ", number1 + number2)

#Q3.2.	Print the sum of the current number and the previous number

x=0
for i in range(10):
    print ("Current Number ",i," Previous Number ",x," Sum:", i+x)
    x = i


#Q3.3 3.	Display three string “Name”, “Is”, “James” as “Name**Is**James”

print('Name', 'Is', 'Chi','AI1701_PFP191', sep='**')


#Q4. Write a program to accept 3 real numbers a, b, c, then:
#Q4.1.Convert Decimal number to octal using print() output formatting

num = 79
print("The octal number of decimal number",num,"is",'%o'%num)

#Q4.2.	Display float number with 2 decimal places using print()

num = 458.541315
print("Display :", '%.2f'%num)
