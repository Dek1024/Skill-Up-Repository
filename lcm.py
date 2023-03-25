#Code for geting LCM of two numbers

def main():
    n1 = input("Enter the first natural number.")
    n2 = input("Enter the first natural number.")
    if "." in n1:
        print("Invalid entry")
        return
    if "-" in n1:
        print("Invalid entry")
    if "." in n2:
        print("Invalid entry")
        return
    if "-" in n2:
        print("Invalid entry")
    n1 = int(n1)
    n2 = int(n2)

    t1 = n1
    t2 = n2
    if n1 == 1:
        fac1 = [1]
    else:
        fac1 = [1]
        dd1 = 2
        while(dd1 <= n1):
            if t1 % dd1 == 0:
                dr1 = t1/dd1
                fac1.append(dr1)
                t1 = dr1
                if dr1 == 1:
                    break
                continue
            else:
                dd1 += 1

        if n2 == 1:
            fac2 = [1]
        else:
            fac2 = [1]
            dd2 = 2
            while(dd2 <= n2):
                if t2 % dd2 == 0:
                    dr2 = t2/dd2
                    fac2.append(dr2)
                    t2 = dr2
                    if dr2 == 1:
                        break
                    continue
                else:
                    dd2 += 1

    l1 = len(fac1)
    l2 = len(fac2)
    ans = []
    for i in range(0,l1,1):
        for j in range(0,l2,1):
            if l1[i] == fac1[j]:
                ans.append(l1[i])
    return ans

while():
    sol = main()
    print(sol)
    restart = input("Do you want to try another time. (Answer with yes or no)").lower()
    if restart == "yes":
        continue
    else:
        exit
