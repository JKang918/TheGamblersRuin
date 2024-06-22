import matplotlib.pyplot as plt
import numpy as np

#gambler_money: initial stake of a gambler
#casino_money: casino's wealth
#win_probability(P): the probability of winning a bet
##assumptions: 
        # 1. P is constant throughout the game
        # 2. winner gets +1, loser gets -1
def gambler_ruin(gambler_money, casino_money, win_probability):
    
    #array to record gambler's money after each bet
    history = []
    bets = 0

    #either one of them reaches 0, the game ends
    while gambler_money > 0 and casino_money > 0:
        #np.random.rand() produces values from 0 to 1 following uniform distribution
        bet_result = np.random.rand()
        #this occures with a chance of P
        if bet_result < win_probability:
            gambler_money += 1
            casino_money -= 1
        #this occures with a chance of 1 - P
        else:
            gambler_money -= 1
            casino_money += 1
        
        #at the end of every bet
        #1. record the gambler's wealth
        #2. increase bets by 1
        history.append(gambler_money)
        bets += 1
    
    #the one whose wealth reaches 0 is the loser
    if gambler_money == 0:
      loser = "gambler"
    else:
      loser = "casino"
    
    return history, bets, loser

def plot_gambler_ruin(gambler_money, casino_money, win_probability):
    history, bets, loser = gambler_ruin(gambler_money, casino_money, win_probability)

    plt.figure(figsize=(10, 6))
    plt.plot(history, label="Gambler's Money")
    plt.axhline(y=0, color='r', linestyle='--', label='Bankruptcy Line')
    plt.xlabel('Number of Bets')
    plt.ylabel('Gambler\'s Money')
    plt.title('Gambler\'s Ruin Simulation')
    plt.legend()
    plt.grid(True)
    plt.show()

    print(f"The {loser} went bankrupt after {bets} bets.")
    
    #if the gambler beats casino, print additional message
    if loser == "casino":
      print("Wow! You beat casino!")

# Example usage
gambler_money = 50          #usually small
casino_money = 5000         #usually large
win_probability = 0.5       

plot_gambler_ruin(gambler_money, casino_money, win_probability)