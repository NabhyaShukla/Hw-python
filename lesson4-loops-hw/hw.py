print("This program checks if the input number is an Armstrong number or not.")
num = int(input("Enter a number: "))
order = 0
tempo = num
while tempo > 0:
    order += 1
    tempo = tempo // 10


sum = 0
while tempo > 0:
    digit = tempo % 10
    sum += digit ** order
    tempo = tempo // 10


if sum == num:

    print("This input number is an Armstrong number")
else:

    print("This input number is not an Armstrong number")
