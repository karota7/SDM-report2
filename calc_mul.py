#!/usr/bin/python3

import re
                
def calc(A,B):
        a = A
        b = B
        if isinstance(a,int) and isinstance(b,int):
                if 0<a and a<1000 and 0<b and b<1000:
                        valid=True
                else:
                        valid=False
        else:
                valid=False
                
        if valid:
                ans=a*b
                return ans
        else:
                return -1
        
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
