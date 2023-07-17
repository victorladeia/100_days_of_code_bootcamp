# Greetings:

print( """
Volcanoes volcanoes volcanoes

                      ooO
                     ooOOOo
                   oOOOOOOoooo
                 ooOOOooo  oooo
                /vvv\
               /V V V\ 
              /V  V  V\          
             /         \          AAAAH!  RUN FOR YOUR LIVES!
            /           \               /
          /               \   	  o          o
__       /                 \     /-   o     /-
/\     /                     \  /\  -/-    /\
                                    /\

                      ooO
                     ooOOOo
                   oOOOOOOoooo
                 ooOOOooo  oooo
                /vvv\
               /V V V\ 
              /V  V  V\          
             /     V   \          AAAAH!  RUN FOR YOUR LIVES!
            /      VV   \               /
 ____      /        VVV    \   	  o          o
 /\      /        VVVV     \     /-   o     /-
/  \   /           VVVVVVV   \  /\  -/-    /\
                    VVVVVVVVVVVVV   /\
""" )

cross_road_decision = input( "You're at a cross road. Where do you want to go? Type 'left' or 'right' " )

if cross_road_decision == 'right':
    print( "Game Over.")
else:
    lake_decision = input( "You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. " )
    if lake_decision == 'swim':
        print( "Game Over." )
    else:
        door_decision =  input( "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? " )
        if door_decision == 'yellow':
            print( "You Win!")
        else:
            print( "Game Over." )