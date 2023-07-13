# Getting user's height:
height = float( input( "Enter your height in m: " ) )

# Getting user's weight:
weight =  float( input( "Enter your weight in kg: " ) )

# Calculating BMI

bmi = weight / height ** 2

if bmi < 18.5:
    condition = "are underweight."
elif ( bmi >= 18.5 and bmi < 25 ):
    condition = "have a normal weight."
elif ( bmi >= 25 and bmi < 30 ):
    condition = "are slight overweight."
elif ( bmi >=30 and bmi < 35 ):
    condiiton = "are obese."
else:
    condition = "are clinically obese."

print( f"Your BMI is { round( bmi ) }, you { condition }" )