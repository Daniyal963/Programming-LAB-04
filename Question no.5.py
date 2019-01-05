print("Daniyal Ali - 18b-096-CS(A)")
print("Lab-4 - 09/Nov/2018")
print("Question no.5")
#Code
initial_value = eval(input("Enter the initial value for the range :"))
final_value = eval(input("Enter the final value for the range :"))
numbers = range(initial_value,final_value)
sum = 0
for value in numbers:
    sum = sum + value
    print("The sum is", sum)
