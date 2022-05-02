#P,N=get_Numbers()Total,Average= calculation(P, N) display(Total,Average)

def get_Numbers():
    P =eval(input("Enter a number"))
    N =eval(input("Enter the second number"))
    return P,N

def calculation(P,N):
    T= P + N
    A= (P+N)/2
    return T, A

def display(Total,Average):
    print("The total is :",Total)
    print("The average is :",Average)

def printLine():
    print("================================================")
    

def main():
    printLine()
    P,N = get_Numbers()
    Total,Average= calculation(P, N)
    display(Total,Average)
    printLine()
    

main()

