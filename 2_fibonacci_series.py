# A program to generate first n numbers of the fibonacci series
def main():
    n = input("Enter a whole number value of n for first n numbers of the fibonacci series.")
    n = int(n)
    if n <= 0:
        print("Invalid entry")
        return None
    if n == 1:
        series = [0]
        return series
    if n == 2:
        series = [0,1]
        return series
    else:
        index = 3
        temp1 = 0
        temp2 = 1
        series = [0,1]
        while(index <= n):
            temp = temp2
            temp2 = temp2 + temp1
            temp1 = temp
            series.append(temp2)
            index += 1
        return series

output = main()
print(output)

while(1):
    loop = input("Do you want to list another fibonacci series (Answer with yes or no) ?").lower()

    if loop == "yes":
        output = main()
        print(output)

    else:
        exit()
