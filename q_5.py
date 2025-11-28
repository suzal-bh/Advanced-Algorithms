# simple 2 player shooting game simulator.

import time
import threading

class player:
    def __init__( self, name, status, location, targetting_order ):
        self.name = name
        self.status = status # status is boolean, True if alive, False if dead.
        self.location = location # each player's land has 10 location where they can hide, 1, 2, ..., 10.
        self.targetting_order = targetting_order 
        # a player can send a missile to one of the 10 locations of the other player.
        # the player keep sending missile until hitting the hiding location of the other player.
        # a currently destroyed location does not worth sending a missile again.
        # so the player just choose which location should be targeted first, then second, then third so a list of 10 non-repeating integers 1, 2, ..., 10. I.e. a permutation.

# players keep launching missiles if they are still alive.
# they don't know if the other player is dead or alive before the end of the game.
# setting and launching each missile takes 1 second.
def player_action( player1, player2 ):
    if player1.status == False:
        return()
    print( f"{player1.name} is ready." )
    for i in range( 10 ):
        time.sleep( 1 )
        print( f"location {player1.targetting_order[ i-1 ]} of {player2.name}'s land is attacked." )
        if player2.status == True and player2.targetting_order[ i-1 ] == player1.location:
            player1.status = False
            print( f"{player1.name} is dead." )
            break


# running the game.
P1 = player( "Ahmad", True, 5, [ 4, 6, 3, 7, 2, 8, 5, 9, 10, 1 ] )
P2 = player( "Bahman", True, 7, [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] )


print( "Game started." )

t1 = threading.Thread(target=player_action, args=(P1, P2))
t2 = threading.Thread(target=player_action, args=(P2, P1))

t1.start()
t2.start()

t1.join()
t2.join()

if P1.status and not P2.status:
    print(f"{P1.name} won.")
elif P2.status and not P1.status:
    print(f"{P2.name} won.")
else:
    print("Withdraw.")

print("Game finished")
