'''
    This script was written in python 3.x.
    In order to run this script, please make sure your python version is 3.x or above.
    How to run:
        python thabit2.py
    or if it doesn't work use this one:
        python3 thabit2.py
    Author: Pedja <pedja.terzic@hotmail.com>
'''

from mpmath import *
print("                        ***** THABIT 2 *****\n\n\n")
while True:
    n=int(input("Enter the exponent : "))
    T=3*2**n+1
	
    def jacobi(a,q):
        j=1
        while a != 0:
            while a%2==0:
                a=a/2
                if q%8==3 or q%8==5:
                    j=-j
            #interchange(a,q)
            c=a
            a=q
            q=c
            if a%4==3 and q%4==3:
                j=-j
            a=fmod(a,q)
        if q==1:
            return j
        else:
            return 0
    
    if n < 3:
        print("Exponent must be greater than two")
    elif n%4==3:
        print("3*2^"+str(n)+"+1 is composite")
    else:
        if n%4==1:
            s=32672
        elif n%12==2:
            s=1692
        elif n%12==6 or n%12==10:
            s=21868
        elif n%12==8:
            s=50542
        else:
            d=3
            while not(jacobi(d-2,T)==-1 and jacobi(d+2,T)==-1):
                d=d+1
            s=d**3-3*d
			
        
        ctr=1
        while ctr<=n-2:
            s=(s**2-2)%T
            ctr=ctr+1
        if s==0:
            print("3*2^"+str(n)+"+1 is prime")
        else:
            print("3*2^"+str(n)+"+1 is composite")
    try_again = ""
    # Loop until users opts to go again or quit
    while not(try_again == "1") and not(try_again == "0"):
        try_again = input("Press 1 to try again, 0 to exit. ")
        if try_again in ["1", "0"]:
            continue  # a valid entry found
        else:
            print("Invalid input- Press 1 to try again, 0 to exit.") 
    # at this point, try_again must be "0" or "1"
    if try_again == "0":
        break 