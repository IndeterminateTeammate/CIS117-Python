#This is my First Python Programming assignment
#Sean Fay
#31 August 06

#Introduction plus user input
print("Hello, what is your name?")
name = input()
print("Hello, " + name + "! Nice to meet you.")

#ID displayed in f-strings
my_id = 6666529
print(f"{my_id:08d}")
print(f"{my_id:.2f}")
print(f"{my_id:b}")
print(f"{my_id:#x}")

#first digit from my ID
first=my_id//1000000
print(f"first digit {first}")

#last digit from my ID
last=my_id%10
print(f"last digit {last}")

#Summation of first and last digits from my ID
print(f"sum of the first and last digits: {first+last}")