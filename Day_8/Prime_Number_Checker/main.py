#Write your code below this line ๐

def prime_checker(number):
    count = 0
    for num in range(1, (number+1) ):
        if number % num == 0:
            count += 1
    
    if ( count == 2 ):
        print("It's a prime number.")
    else:
        print( "It's not a prime number." )

#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)