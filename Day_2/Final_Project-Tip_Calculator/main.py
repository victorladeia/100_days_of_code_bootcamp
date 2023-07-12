# Write a Greeting message:
print( "Welcome to the Tip Calculator!" )

# Get the total bill:
bill = float( input( "What was the total bill? $" ) )

#Get tip percentage:
tip_percentage = int( input( "What percentage tip would you like to give? 10, 12, or 15? " ) )

# Get amount of people:
people_number = int( input( "How many people to split the bill? " ) )

# Calculate tip:
tip = bill * ( tip_percentage / 100 )

# Add tip to total
total_bill = bill + tip

# Divide the bill for people number:
individual_bill = round( total_bill / people_number, 2)
individual_bill = "{:.2f}".format( individual_bill )

# print result
print( f"Each pearson should pay ${ individual_bill }" )