height = input( "enter your height in m: " )
weight = input( "enter your weight in kg: ")

BMI = round( float( weight ) / float( height ) ** 2 )

print( BMI )