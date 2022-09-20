print("\n")
for i in range(1,6):
    for j in range(1,6):
        if((j==1 and i<=5) or (i==3 and j<5) or (j==4 and i<=5)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(1,6):
        if((j==1 and i<=4) or (i%2!=0 and j<5)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(1,6):
        if((j==1 and i<=5) or (i==5 and j<5)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(1,6):
        if((j==1 and i<=5) or (i==5 and j<5)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(1,6):
        if((j==1 and i<=5) or (i==5 and j<5) or (i==1 and j<5) or (j==4 and i<=5)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    #print("\n \n")
print("\n")
print("~~~~~~~WELCOME TO KOTAK MAHINDRA BANK ATM~~~~~~~\n ")
print("           ENTER YOUR CARD//// \n")
Balance=10000
PIN=4123
Number=int(input("ENTER YOUR 4 DIGIT PIN -"))
ch=1
print("\n")
while(ch==1):
    if PIN==Number:
        print("_____________________")
        print("|     MENU          |\n_____________________")
        print("| 1.DEPOSIT AMOUNT  |\n_____________________")
        print("| 2.DISPLAY BALANCE |\n_____________________")
        print("| 3.WITHDRAW CASH   |\n_____________________")
        print("| 4.PRINT PASSBOOK  |\n_____________________")
        print("| 5.EXIT            |")
        print("_____________________\n")
        ch1 = int(input("ENTER YOUR CHOICE -"))
        if (ch1 == 1):
            DA = int(input("ADD MONEY TO DEPOSIT -"))
            Balance += DA
            print("TOTAL BALANCE AVAILABLE=", Balance)
        if (ch1 == 2):
            print("TOTAL ACCOUNT BALANCE -", Balance)
        if (ch1 == 3):
            Amount = int(input("ENTER WITHDRAWL AMOUNT -"))
            if (Amount % 100 == 0):
                if (Amount <= Balance):
                    if (Amount <= 1000):
                        if (Amount % 200 == 0):
                            n = Amount // 200
                            n1 = n - 1  # 200
                            N = n1 * 200
                            n3 = Amount - N
                            n4 = n3 // 100  # 100
                            print("PLEASE COLLECT YOUR CASH", Amount)
                            print("200*", n1)
                            print("100*", n4)
                        else:
                            n = Amount // 200  # 200
                            n1 = Amount % 200
                            n2 = n1 // 100  # 100
                            print("PLEASE COLLECT YOUR CASH>>>>>>", Amount,"<<<<<<<")
                            print("200*", n)
                            print("100*", n2)

                    if (Amount <= 2500 and Amount > 1000):
                        if (Amount % 500 == 0):
                            n = Amount // 500
                            n1 = n - 1  # 500
                            N = n1 * 500
                            n2 = Amount - N
                            n3 = n2 // 200  # 200
                            n4 = n2 % 200
                            n5 = n4 // 100  # 100
                            print("COLLECT YOUR CASH", Amount)
                            print("500*", n1)
                            print("200*", n3)
                            print("100*", n5)
                        else:
                            n0 = Amount // 500  # 500
                            n1 = n0 * 500
                            n2 = Amount - n1
                            if (n2 % 200 == 0):
                                n = n2 // 200
                                n3 = n - 1  # 200
                                N = n3 * 200
                                n5 = n2 - N
                                n4 = n5 // 100  # 100
                                print("PLEASE COLLECT YOUR MONEY", Amount)
                                print("500*", n0)
                                print("200*", n3)
                                print("100*", n4)
                            else:
                                n = n2 // 200  # 200
                                n1 = n % 200
                                n2 = n1 // 100  # 100
                                print("PLEASE COLLECT YOUR MONEY", Amount)
                                print("500*", n0)
                                print("200*", n)
                                print("100*", n2)

                    if (Amount > 2500):
                        if (Amount % 2000 == 0):
                            n = Amount // 2000
                            n1 = n - 1  # 2000
                            n2 = n1 * 2000
                            print(n2)
                            r = Amount - n2
                            n3 = r // 500
                            N = n3 - 1  # 500
                            n4 = N * 500
                            # r1=r-n4
                            n5 = r - n4
                            n6 = n5 // 200  # 200
                            n7 = n5 % 200
                            n8 = n7 // 100  # 100
                            print("PLEASE COLLECT YOUR CASH", Amount)
                            print("2000*", n1)
                            print("500*", N)
                            print("200*", n6)
                            print("100*", n8)
                        else:
                            N = Amount // 2000  # 2000
                            l = N * 2000
                            l1 = Amount - l
                            n0 = Amount % 2000
                            if (n0 % 500 == 0):
                                n = n0 // 500
                                n1 = n - 1  # 500
                                N1 = n1 * 500
                                n2 = n0 - N1
                                n3 = n2 // 200  # 200
                                n4 = n2 % 200
                                n5 = n4 // 100  # 100
                                print("COLLECT YOUR CASH", Amount)
                                print("2000*", N)
                                print("500*", n1)
                                print("200*", n3)
                                print("100*", n5)
                            else:
                                n = n0 // 500  # 500
                                n1 = n * 500
                                n2 = n0 % 500
                                if (n2 % 200 == 0):
                                    nn = n2 // 200
                                    n3 = nn - 1  # 200
                                    n6 = n3 * 200
                                    n5 = n2 - n6
                                    n4 = n5 // 100  # 100
                                    print("PLEASE COLLECT YOUR MONEY", Amount)
                                    print("2000*", N)
                                    print("500*", n)
                                    print("200*", n3)
                                    print("100*", n4)
                                else:
                                    nn = n2 // 200  # 200

                                    n3 = nn * 200
                                    n4 = n2 - n3
                                    n5 = n4 // 100  # 100
                                    print("PLEASE COLLECT YOUR MONEY", Amount)
                                    print("2000*", N)
                                    print("500*", n)
                                    print("200*", nn)
                                    print("100*", n5)

                    Balance = Balance - Amount
                    print("BALANCE >>>> ", Balance)
                else:
                    print("BALANCE INSUFFICIENT")
            else:
                print("ENTER AMOUNT MULTIPLE OF 100")

        if (ch1 == 4):
            print("PLEASE INSERT YOUR PASSBOOK")
        if (ch1 == 5):
            print("THANK YOU FOR COMMUNICATING KOTAK BANK ATM ")
    else:
        print("WRONG PIN plrase try again")
    ch=int(input("PRESS 1 TO CONTINUE OR PRESS 0 TO QUIT"))
       
