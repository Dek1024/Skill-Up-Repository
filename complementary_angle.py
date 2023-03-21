#Getting a comac complelemtray angle for a given number
a = input("Enter an anglr between 0 to 90 degrees")
a = float(a)
if (a <0 or a > 90):
    print("Invalid number")
    exit()
print("The complementary angle is", 90 - a)
