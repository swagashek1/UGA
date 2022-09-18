"""Assess a betting strategy.
#  %s/\t//g
#  %s/ $//g
#  %s/\s\+$//

Copyright 2022, University of Georgia
Copyright 2022, Georgia Institute of Technology

Template code for CSCI x170

The University of Georgia & Georgia Institute of Technology
asserts copyright ownership of this template and all derivative
works, including solutions to the projects assigned in this course. Students
and other users of this template code are advised not to share it with others
or to make it available on publicly viewable websites including repositories
such as github and gitlab.  This copyright statement should not be removed
or edited.

We do grant permission to share solutions privately with non-students such
as potential employers. However, sharing with other current or future
students of CSCI x170 OR G-Tech's CS 7646 is prohibited and subject to being
investigated as a
UGA & GT honor code violation.

-----do not edit anything above this line---

Student Name: 	Abhishek Murugappan (replace with your name)
UGA User ID: 	am93029 (replace with your User ID)
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def author():
    return 'am93029' 		# replace ingrid with your UGA username.

def gtid():
    return 811515011 		# replace with your UGA ID number

def get_spin_result(win_prob):
    result = False

    if np.random.random() <= win_prob:
        result = True
    return result
def simulation(win_prob,runs):
    df=pd.DataFrame()
    for x in range(runs):
        winplotsmall = []
        count=0;

        x = 0
        winnum=0

        episode_winning = 0
        count = 0
        while (episode_winning < 80 and count<300):
            won = False
            bet_amount = 1

            while (not won ):

                count = count + 1
                won = get_spin_result(win_prob)

                if won:

                    episode_winning = episode_winning + bet_amount
                else:
                    episode_winning = episode_winning - bet_amount
                    bet_amount = bet_amount * 2
                winplotsmall.append(episode_winning)
        while(count <300):
               winplotsmall.append(winplotsmall[count-1])
               count+=1
        df = pd.concat([df, pd.DataFrame(winplotsmall)], axis=1)

    return df;

def simulationBankroll(win_prob,runs,bankroll):
    df=pd.DataFrame()
    for y in range(runs):
        winplotsmall = []
        count=0;

        x = 0
        winnum=0

        episode_winning = 0
        count = 0
        while (episode_winning < 80 and count<300):
            won = False
            bet_amount = 1
            while not won:

                count = count + 1
                won = get_spin_result(win_prob)

                if won:
                    episode_winning = episode_winning + bet_amount
                else:
                    episode_winning = episode_winning - bet_amount
                    if episode_winning == -bankroll:

                        winplotsmall.append(episode_winning)
                        break
                    else:
                        if bet_amount*2 >=episode_winning+bankroll:
                            bet_amount=episode_winning+bankroll
                        else:
                            bet_amount = bet_amount * 2

                winplotsmall.append(episode_winning)
            if episode_winning == -bankroll:

                count-=1
                break

        while( len(winplotsmall)<300):
               winplotsmall.append(winplotsmall[len(winplotsmall)-1])
               count+=1
        df = pd.concat([df, pd.DataFrame(winplotsmall[0:300])],axis=1)

    return df;

def experiment1(win_prob):
    plt.axis([0, 300, -256, 100])

    df=simulation(win_prob,10)
    plt.plot(df)
    plt.title("Simple Simulator 10 times")
    plt.xlabel("Number of Spins")
    plt.ylabel("Winnings")
    plt.savefig('experiment1figure1.png')
    plt.clf()

    plt.axis([0, 300, -256, 100])
    df = simulation(win_prob,1000)
    plt.plot(df.mean(axis=1),label="Mean")
    plt.plot(df.mean(axis=1) - df.std(axis=1),label="Mean-Standard Deviation")
    plt.plot(df.mean(axis=1) + df.std(axis=1),label="Mean+Standard Deviation")
    plt.legend()
    plt.title("Simple Simulator 1000 times Mean")
    plt.xlabel("Number of Spins")
    plt.ylabel("Winnings")
    plt.savefig('experiment1figure2.png')
    plt.clf()

    plt.axis([0, 300, -256, 100])
    plt.plot(df.median(axis=1),label="Median")
    plt.plot(df.median(axis=1) - df.std(axis=1),label="Median-Standard Deviation")
    plt.plot(df.median(axis=1) + df.std(axis=1),label="Median+Standard Deviation")
    plt.legend()
    plt.title("Simple Simulator 1000 times Median")
    plt.xlabel("Number of Spins")
    plt.ylabel("Winnings")
    plt.savefig('experiment1figure3.png')
    plt.clf()

def experiment2(win_prob,bankroll):


    plt.axis([0, 300, -256, 100])
    df = simulationBankroll(win_prob,1000,bankroll)
    plt.plot(df.mean(axis=1),label="Mean")
    plt.plot(df.mean(axis=1) - df.std(axis=1),label="Mean-Standard Deviation")
    plt.plot(df.mean(axis=1) + df.std(axis=1),label="Mean+Standard Deviation")
    plt.legend()
    plt.title("Realistic Gambling Simulator 1000 times Mean")
    plt.xlabel("Number of Spins")
    plt.ylabel("Winnings")
    plt.savefig('experiment2figure1.png')
    plt.clf()
    #df.to_csv('exp2.csv', sep=',')
    #print(len(df[df.iloc[299]==80)/len(df.iloc[299]))
    #print(df.iloc[299])
    plt.axis([0, 300, -256, 100])
    plt.plot(df.median(axis=1),label="Median")
    plt.plot(df.median(axis=1) - df.std(axis=1),label="Median-Standard Deviation")
    plt.plot(df.median(axis=1) + df.std(axis=1),label="Median+Standard Deviation")
    plt.legend()
    plt.title("Realistic Gambling Simulator 1000 times Median")
    plt.xlabel("Number of Spins")
    plt.ylabel("Winnings")
    plt.savefig('experiment2figure2.png')
    plt.clf()

def test_code():

    win_prob = 0.474 # set appropriately to the probability of a win
    np.random.seed(gtid())  # do this only once
    win_prob = (36 / 2) / (2 + 36)
    experiment1(win_prob)
    experiment2(win_prob,256)






    #(get_spin_result(win_prob)) # test the roulette spin
    #print(winnum/x) # test the roulette spin


    # add your code here to implement the experiments

if __name__ == "__main__":
    test_code()
