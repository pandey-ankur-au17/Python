def by_while_loop():  
    n=int(input("Enter a line="))
    coloum=1
    while coloum<(n//2 + n%2 +1):
      print(" "*(n-coloum),end="")
      
      rows=1
      while rows<coloum+1:
        print(rows,end="")
        rows=rows+1

      rows1=coloum-1
      while rows1>0:
        print(rows1,end="")
        rows1=rows1-1
      print()

      coloum=coloum+1


    coloum=n//2
    while coloum>0:
      print(" "*(n-coloum),end="")
      

      rows=1
      while rows<(coloum+1):
        print(rows,end="")
        rows=rows+1

      rows1=1
      while rows1<coloum:
        print(rows1,end="")
        rows1=rows1+1
      print()
        
      coloum=coloum-1

# uncomment below line to check code
by_while_loop()