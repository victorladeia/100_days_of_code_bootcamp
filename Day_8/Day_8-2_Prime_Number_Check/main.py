def prime_checker( number ):
    for num in range(2, number):
        if number % num == 0:
            print( "It's not a prime number" )
            break
        elif num == number - 1:
            print( "It's a prime number" )

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)