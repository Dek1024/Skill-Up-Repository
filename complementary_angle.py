#Getting a complelemtray angle for the given angle
def main():
    a = input("Enter an anglr between 0 to 90 degrees")
    a = float(a)
    if (a <0 or a > 90):
        print("Invalid number")
        exit()
    print("The complementary angle is", 90 - a)

main()

while(1):    
    restart = print("Do you want to test the code again (answer by typing yes or no) ?").lower()
    if restart == "yes":
        main()
    else:
        exit()
