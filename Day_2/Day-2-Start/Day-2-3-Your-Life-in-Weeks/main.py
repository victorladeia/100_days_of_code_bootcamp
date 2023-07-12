# Getting user's age:
age = input( "What is your current age?" )

left_age_in_years = 90 - int( age )

left_age_in_months = left_age_in_years * 12

left_age_in_weeks = left_age_in_years * 52

left_age_in_days = left_age_in_years * 365

print( f"You have {left_age_in_days} days, {left_age_in_weeks} weeks, and {left_age_in_months} months." )



