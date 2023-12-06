import os
import art
import game_data
import random

class HigherLowerGame:

    def __init__(self):
        """Constructor which initialize the game"""
        self._score = 0
        self.stat = True
        self._selectedAccounts = []
        self._randomDataItem()
    
    def _randomDataItem(self):
        """Set the two data items to be compared"""
        if not self._selectedAccounts:
            self._selectedAccounts.append(game_data.data[(int) (100 * random.random()) % (len(game_data.data)-1)])
        if len(self._selectedAccounts) > 1:
            self._selectedAccounts.reverse()
            self._selectedAccounts.pop()
            self._selectedAccounts.append(game_data.data[(int) (100 * random.random()) % (len(game_data.data)-1)])
        else:
            account = game_data.data[(int) (100 * random.random()) % (len(game_data.data)-1)]
            while True:
                account = game_data.data[(int) (100 * random.random()) % (len(game_data.data)-1)]
                if account["follower_count"] != self._selectedAccounts[0]["follower_count"]:
                    break
            self._selectedAccounts.append(account)
    
    def _compare(self, toggl):
        """Verifie the user choise is right."""
        if toggl == (self._selectedAccounts[0]['follower_count'] > self._selectedAccounts[1]['follower_count']):
            self._randomDataItem()
            self._score += 1
        else:
            self.stat = False

    def play(self):
        """Launch the game"""
        
        while True:
            os.system("clear")
            print(art.logo)
            if self._score:
                print("You're right! Current score: {}".format(self._score))
            print("Compare A : {}, a {}, from {}.".format(self._selectedAccounts[0]['name'],self._selectedAccounts[0]['description'], self._selectedAccounts[0]['country']))
            print(art.vs)
            print("Against B : {}, a {}, from {}.".format(self._selectedAccounts[1]["name"], self._selectedAccounts[1]['description'], self._selectedAccounts[1]['country']))
            awnser = input("Who has more followers? Type 'A' or 'B': ").capitalize()
            if awnser == 'B':
                self._compare(False)
            if awnser == 'A':
                self._compare(True)
            if not self.stat:
                break
        
        os.system("clear")
        print(art.logo)
        print("Sorry, that's wrong. Final Score: {}".format(self._score))
        while True:
            continue


game = HigherLowerGame()
game.play()




        



    
        
    
        
    
    
    
