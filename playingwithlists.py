numbers = [34,81,11,7,91,63,2,0,-5,99]
sum = 0
for number in numbers:
    sum += number

print("Sum= ",sum)

print("Average=",sum/len(numbers))

numbers.sort()

print(f"Smallest number: {numbers[0]} and Largest number: {numbers[-1]}")