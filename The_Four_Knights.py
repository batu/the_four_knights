#06.12.2013 21:03
import random
import Tkinter as tk

# The main deck class which will contain all 52 cards.
# The cards will have a suit and value and a location of the image attached 
# to them.
class Cards(object):
    def __init__(self, suit, value, location):
        self.suit = suit
        self.value = value
        if value == 14:
            self.name = "Ace of " + suit
        elif value == 11:
            self.name = "Jack of " + suit
        elif value == 12:
            self.name = "Queen of " + suit
        elif value == 13: 
            self.name = "King of " +suit
        else:
            self.name = str(value) + " of " + suit 
        
        self.location = location
            
        def __str__(self):
            return self.name
        
        def __repr__(self):
            return self.name
# The deck will consist of 52 cards.
class Deck(object):
    def __init__(self,cards):
        if type(cards) != list:
            raise("The hand must be an  list of cards.") 
        else:
            self.cards = cards
        self.deck_dealt_1 = []
        self.deck_dealt_2 = []
        self.stockades = []
            
# Shuffles the deck so the dealing is random.
    def shuffle(self):
            random.shuffle(self.cards)

# The main deck is dealt into player_1 and player_2 decks.
    def deal(self):
        stockades = []
        deck_dealt_1 = []
        deck_dealt_2 = []
       
        for counter in xrange(0,4):
            counter
            stockades += [self.cards[0]]
            del self.cards[0]
        
        for counter in xrange(0,24):
            counter
            deck_dealt_1 += [self.cards[0]]
            del self.cards[0]
        
        for counter in xrange(0,24):
            counter
            deck_dealt_2 += [self.cards[0]]
            del self.cards[0]
              
        self.stockades = Stockades(stockades)
        self.deck_dealt_1 = Player_deck(deck_dealt_1, 1)
        self.deck_dealt_2 = Player_deck(deck_dealt_2, 2) 
            
        return self.stockades, self.deck_dealt_1, self.deck_dealt_2     
        
    def __str__(self):
        print_list = ""
        for x in self.cards:
            print_list += x.name + ", "
        return print_list  
    
    def __repr__(self):
        print_list = ""
        for x in self.cards:
            print_list += x.name + ", "
        return print_list  
 
# The place where the extra 4 cards are stored.
class Stockades(object):
    def __init__(self, deck):
        if type(deck) != list:
            raise("The stockades must be an  list of cards.") 
        elif len(deck) > 4:
            raise("The stockades can not contain more than 4 cards")
        else:
            self.deck = deck

    def __repr__(self):
        print_list = ""
        for x in self.deck:
            print_list += x.name + ", "
        return print_list 

# The individual decks of the players.   
class Player_deck(object):
    def __init__(self, deck, player_no):
        if type(deck) != list:
            raise("The deck must be an  list of cards.") 
        elif len(deck) > 24:
            raise("The deck can not contain more than 24 cards")
        else:
            self.deck = deck
        self.player_no = player_no            
        self.hand_dealt = []
        
# The the function that deals cards to the player hands.        
    def draw_hand(self):
        try:
            hand_dealt = []
            for counter in xrange(0,6):
                counter
                hand_dealt += [self.deck[0]]
                del self.deck[0]
            self.hand_dealt = Player_hand(hand_dealt, self.player_no, None)
            return self.hand_dealt
        except:
                return
            
    def __repr__(self):
        print_list = ""
        for x in self.deck:
            print_list += x.name + ", "
        return print_list 

# A list of cards representing the hand.    
class Player_hand(object):
    def __init__(self, hand, player_no, index):
        self.hand = hand    
        self.player_no = player_no
        self.hand_dealt = []
        self.index = index
    
    def __repr__(self):
        print_list = ""
        for x in self.hand:
            print_list += x.name + ", "
        return print_list 

# Checks whether the hand has a card that can beat the cards in the battleground
# As in the game If you can not reinforce your card you lose the war( aka lose
# a point)
# This function will be used to check when a player wins a point.
    def is_reinforceable(self, battleground):
        for card in self.hand:
            if card.suit == "spades" and \
            battleground.winner.suit == "diamonds":
                return True
            elif card.suit == "diamonds" and \
            battleground.winner.suit == "clubs":
                return True
            elif card.suit == "clubs" and \
            battleground.winner.suit == "hearts":
                return True
            elif card.suit == "hearts" and \
            battleground.winner.suit == "spades":
                return True
                
            elif (card.suit == "spades" or card.suit == "clubs") and \
            (battleground.winner.suit == "spades" or \
            battleground.winner.suit == "clubs") and \
            (card.value > battleground.winner.value):
                return True
            
            elif (card.suit == "hearts" or card.suit == "diamonds") \
            and (battleground.winner.suit == "hearts" or \
                 battleground.winner.suit == "diamonds")and\
            (card.value > battleground.winner.value):
                return True
        return False
    
# The battleground class where the cards that are on the board are stored.
# This has a fight function which determines which player has to reinforce
# (aka put down a card that is "acceptable" as determined by the acceptable card function.    
class Battleground(object):
    def __init__(self,card_1, card_2):
        self.card_1 = card_1
        self.card_2 = card_2
        self.winner = None
        self.winner_player = None
        self.player_1_points = 0
        self.player_2_points = 0
        self.equilize = 0
        
# The fight function to determine the winner.
    def fight(self):
        
        if self.card_1.suit == "spades" and self.card_2.suit == "diamonds":
            self.winner = self.card_1
            self.winner_player = 1
        elif self.card_1.suit == "diamonds" and self.card_2.suit == "clubs":
            self.winner = self.card_1
            self.winner_player = 1
        elif self.card_1.suit == "clubs" and self.card_2.suit == "hearts":
            self.winner = self.card_1
            self.winner_player = 1
        elif self.card_1.suit == "hearts" and self.card_2.suit == "spades":
            self.winner = self.card_1
            self.winner_player = 1
        
        elif self.card_2.suit == "spades" and self.card_1.suit == "diamonds":
            self.winner = self.card_2
            self.winner_player = 2
        elif self.card_2.suit == "diamonds" and self.card_1.suit == "clubs":
            self.winner = self.card_2
            self.winner_player = 2
        elif self.card_2.suit == "clubs" and self.card_1.suit == "hearts":
            self.winner = self.card_2
            self.winner_player = 2
        elif self.card_2.suit == "hearts" and self.card_1.suit == "spades":
            self.winner = self.card_2
            self.winner_player = 2
            
        elif (self.card_1.suit == "spades" or self.card_1.suit == "clubs") and \
        (self.card_2.suit == "spades" or self.card_2.suit == "clubs") and \
        (self.card_1.value > self.card_2.value):
            self.winner = self.card_1
            self.winner_player = 1
            
        elif (self.card_1.suit == "hearts" or self.card_1.suit == "diamonds")  \
        and (self.card_2.suit == "hearts" or self.card_2.suit == "diamonds")and\
        (self.card_1.value > self.card_2.value):
            self.winner = self.card_1
            self.winner_player = 1
            
        elif (self.card_1.suit == "spades" or self.card_1.suit == "clubs") and \
        (self.card_2.suit == "spades" or self.card_2.suit == "clubs") and \
        (self.card_1.value < self.card_2.value):
            self.winner = self.card_2
            self.winner_player = 2
                     
        elif (self.card_1.suit == "hearts" or self.card_1.suit == "diamonds") \
        and (self.card_2.suit == "hearts" or self.card_2.suit == "diamonds")and\
        (self.card_1.value < self.card_2.value):
            self.winner = self.card_2
            self.winner_player = 2
            
        elif (self.card_1.suit == "spades" or self.card_1.suit == "clubs") and \
        (self.card_2.suit == "spades" or self.card_2.suit == "clubs") and \
        (self.card_1.value == self.card_2.value):
            self.winner = None
            self.winner_player = 0
            
        elif (self.card_1.suit == "hearts" or self.card_1.suit == "diamonds") \
        and (self.card_2.suit == "hearts" or self.card_2.suit == "diamonds")and\
        (self.card_1.value == self.card_2.value):
            self.winner = None
            self.winner_player = 0
        else:
            print "This is crashing sort the ifs"         
        
# each reinforce function calls this before hand. This function is checks whether
# the clicked card can win against the card on the battleground.
def acceptable_card(card,battleground):
    if battleground.equilize == 1:
        return True
    if battleground.winner == None:
        return True
    elif card.suit == "spades" and \
        battleground.winner.suit == "diamonds":
        return True
    elif card.suit == "diamonds" and \
    battleground.winner.suit == "clubs":
        return True
    elif card.suit == "clubs" and \
    battleground.winner.suit == "hearts":
        return True
    elif card.suit == "hearts" and \
    battleground.winner.suit == "spades":
        return True
        
    elif (card.suit == "spades" or card.suit == "clubs") and \
    (battleground.winner.suit == "spades" or \
    battleground.winner.suit == "clubs") and \
    (card.value > battleground.winner.value):
        return True
    
    elif (card.suit == "hearts" or card.suit == "diamonds") \
    and (battleground.winner.suit == "hearts" or \
         battleground.winner.suit == "diamonds")and\
         (card.value > battleground.winner.value):
        return True
    return False

# Draws another player hand.
def draw_hand(player_deck, player_hand):
    if player_deck.player_no == 1:
        try:
            hand_dealt = []
            for counter in xrange(0,6):
                counter
                hand_dealt += [player_deck.deck[0]]
                del player_deck.deck[0]
            player_hand.hand = hand_dealt
            
        except:
            print "There is no more cards to draw."
        
    if player_deck.player_no == 2:
        try:
            hand_dealt = []
            for counter in xrange(0,6):
                counter
                hand_dealt += [player_deck.deck[0]]
                del player_deck.deck[0]
    
            player_hand.hand = hand_dealt
        except:
            print "There is no more cards to draw."

# the main function that puts down a card into the battleground to fight.            
def reinforce(player_hand,card_name,battleground, gui):
    
    if player_hand.player_no == 1:
# When player clicks button one it returns the index of the button.
# the first button 0, the third button 2 etc... Then this function takes that
# index. Then checks which card in the player hand list of that index and puts
# that card forward. As my system uses indexes to work a replacement dummy card
# (N0) is replaced.
        index = player_hand.index
        battleground.card_1 = player_hand.hand[index]
        player_hand.hand[index] = gui.N0
        player_hand.index = None

       
    if player_hand.player_no == 2:
        index = player_hand.index
        battleground.card_2 = player_hand.hand[index]
        player_hand.hand[index] = gui.N0
        player_hand.index = None

# Sometimes a card has to be put down without a fight (when players have uneven
# numbers of cards). This function removes a card from the player hand.                  
def burn_card(player_hand,card_name,battleground, gui):

    if player_hand.player_no == 1:
        index = player_hand.index
        battleground.card_1 = player_hand.hand[index]
        player_hand.hand[index] = gui.N0
        player_hand.index = None

                
    if player_hand.player_no == 2:
        index = player_hand.index
        battleground.card_2 = player_hand.hand[index]
        player_hand.hand[index] = gui.N0
        player_hand.index = None
                                       
# the ai version of reinforcement.
def ai_reinforce(player_hand,battleground, gui):
    
# This function does the reverse. First iterates through the hand calling 
# acceptable card on each element of the player hand list (all cards)
# When it finds an acceptable card it takes its index and calls the 
# corresponding button which in turn does handles the GUI part of the move. 
    for card in player_hand.hand:
        if acceptable_card(card,battleground):
            battleground.card_2 = card
            index = player_hand.hand.index(card)

            if index == 0:
                p2_button_1(battleground, player_hand, gui)
            elif index == 1:
                p2_button_2(battleground, player_hand, gui)
            elif index == 2:
                p2_button_3(battleground, player_hand, gui)
            elif index == 3:
                p2_button_4(battleground, player_hand, gui)
            elif index == 4:
                p2_button_5(battleground, player_hand, gui)
            elif index == 5:
                p2_button_6(battleground, player_hand, gui)
            player_hand.hand[index] = gui.N0
            return True

# AI version of burning a card.
def ai_burn_card(player_hand,battleground, gui):
  
    if player_hand.player_no == 2:
        for x in xrange(0,6):
            if player_hand.hand[x] != gui.N0:
                battleground.card_2 = player_hand.hand[x]
                if x == 0:
                    p2_button_1(battleground, player_hand, gui)
                elif x == 1:
                    p2_button_2(battleground, player_hand, gui)
                elif x == 2:
                    p2_button_3(battleground, player_hand, gui)
                elif x == 3:
                    p2_button_4(battleground, player_hand, gui)
                elif x == 4:
                    p2_button_5(battleground, player_hand, gui)
                elif x == 5:
                    p2_button_6(battleground, player_hand, gui)
                player_hand.hand[x] = gui.N0
                break

# As each card is replaced with N0 when played. The actual length of the 
# player hands is never reduces. This function solves this issue and 
# returns the number of proper cards.          
def hand_lenght(player_hand, gui):
    length = 0 
    try:
        for card in player_hand.hand:
            if card != gui.N0:
                length += 1
    except:
        return 0
    return length 

# The script that runs when playing. It checks whether there is a winner
# in the battleground (designated with the battleground.fight() function.
# and does whatever needs to be done. The losing player has to reinforce
# If a player cant reinforce give him the point and if the cardn numbers
# in player hands is not equal burn a card.    
def ai_script(battleground,player_1_hand, player_2_hand, gui):
    if battleground.card_1 == None and battleground.card_2 == None:
        gui.wait_order()
        player_1_knight = player_1_hand.index
        burn_card(player_1_hand, player_1_knight, battleground, gui)
        console(gui, "Ai is putting down a card.")
        ai_burn_card(player_2_hand, battleground, gui)
        player_2_hand.index = 0
        console(gui, "Ai has put down.")
        battleground.fight()
    
    if battleground.winner_player == 1:
        if player_2_hand.is_reinforceable(battleground):
            console(gui,  "AI needs to reinforce! He chooses" +\
            " a card that can win the battle!  ")
            ai_reinforce(player_2_hand,battleground, gui)
            battleground.fight()
        else:
            if hand_lenght(player_1_hand, gui) != hand_lenght(player_2_hand, gui):
                if hand_lenght(player_1_hand, gui) < hand_lenght(player_2_hand, gui):
                    console(gui, "Player 1 won. AI needs to put a" +\
                                    " a card to equlize!  ")
                    battleground.winner = None
                    ai_burn_card(player_2_hand, battleground, gui)
                    battleground.card_1 = None
                    battleground.card_2 = None
                    refresh_battleground(gui)
                    player_1_point(gui)
                    battleground.player_1_points += 1
                    battleground.winner_player = None

                elif hand_lenght(player_2_hand, gui) < hand_lenght(player_1_hand, gui):
                    console(gui, "Player 1 lost and needs " +\
                                    " a card to equlize the field!  ")

                    battleground.winner = None              
                    gui.wait_order()
                    player_1_knight = player_1_hand.index
                    burn_card(player_1_hand, player_1_knight, battleground,gui)
                    player_2_point(gui)
                    battleground.player_2_points += 1
                    battleground.card_1 = None
                    battleground.card_2 = None
                    battleground.winner_player = None
                    refresh_battleground(gui)
            else:
                console(gui, "The player 2 lost the war. PLayer 1 wins a point.")
                battleground.card_1 = None
                battleground.card_2 = None
                battleground.winner_player = 0
                battleground.winner = None
                battleground.winner_player = None
                battleground.player_1_points += 1
                player_1_point(gui)
                refresh_battleground(gui)
            
    elif battleground.winner_player == 2:
        if player_1_hand.is_reinforceable(battleground):
            
            
            console(gui,  "Player 1 needs to reinforce! Choose" +\
                                    " a card that can win the battle!  ")
            
            player_1_knight = player_1_hand.index  
            gui.wait_order()
            reinforce(player_1_hand, player_1_knight,battleground, gui)
            battleground.fight()

        else:
            if hand_lenght(player_1_hand, gui) != hand_lenght(player_2_hand, gui):
                if hand_lenght(player_1_hand, gui) < hand_lenght(player_2_hand, gui):
                    console(gui,  "AI lost and needs to put a" + \
                                    " a card to equlize!  ")
                    ai_burn_card(player_2_hand, battleground, gui)
                    refresh_battleground(gui)
                    battleground.card_1 = None
                    battleground.card_2 = None
                    player_1_point(gui)
                    battleground.player_1_points += 1
                    battleground.winner_player = None
                    battleground.winner = None
                     
                elif hand_lenght(player_2_hand, gui) < hand_lenght(player_1_hand, gui):
                    
                    console(gui, "Player 1 lost and needs " +\
                                    " a card to equlize the field!  ")
                    
                    battleground.winner = None
                    battleground.winner_player = None
                    battleground.equilize = 1
                    gui.wait_order()
                    player_1_knight = player_1_hand.index
                    burn_card(player_1_hand, player_1_knight, battleground, gui)
                    battleground.equilize = 0
                    battleground.card_1 = None
                    battleground.card_2 = None
                    refresh_battleground(gui)
                    player_2_point(gui)
                    battleground.player_2_points += 1
            else:
                console(gui,  "The player 1 lost the war. PLayer 2 wins a point!")
                battleground.card_1 = None
                battleground.card_2 = None
                battleground.winner_player = None
                battleground.winner = None
                battleground.player_2_points += 1
                player_2_point(gui)
                refresh_battleground(gui)
                battleground.card_1 = None
                battleground.card_2 = None
    else:
        battleground.card_1 = None
        battleground.card_2 = None

# This main_ai makes ai_script run until all the cards in the deck is depleted
# and also designates who the winner is.       
def main_ai(battleground,player_1_hand, player_2_hand,player_1_deck,player_2_deck, gui, number_players):

    count = 0
    while count != 3:
        count += 1
        while hand_lenght(player_1_hand, gui) != 0 :
            ai_script(battleground,player_1_hand,player_2_hand, gui)
        battleground.card_1 = None
        battleground.card_2 = None
        battleground.winner_player = None
        battleground.winner = None
        refresh_battleground(gui)
        player_1_hand = player_1_deck.draw_hand()
        player_2_hand = player_2_deck.draw_hand()
        update_battleground_ai(number_players,player_1_hand, player_2_hand,\
                               battleground,player_1_deck,player_2_deck, gui, )
        
    
    if battleground.player_1_points > battleground.player_2_points:
        console(gui, "Player 1 won!")
    elif battleground.player_1_points == battleground.player_2_points:
        console(gui, "There was a Draw!")
    else:
        console(gui, "Player 2 won!")
# Refreshes the battleground GUI.
def refresh_battleground(gui):
    gui.l2_b1 = tk.Label(gui.f_line_2, image = gui.img_card_back)
    gui.l3_b1 = tk.Label(gui.f_line_3, image = gui.img_card_back)
    
    gui.l2_b1.grid(row=0, column=0)
    gui.l3_b1.grid(row=0, column=0)

# Updates the battleground GUI.
def update_battleground_ai(number_players, player_hand_1, player_hand_2, battleground, \
                           player_1_deck,player_2_deck, gui):


    gui.l2_b1 = tk.Label(gui.f_line_2, image = gui.img_card_back)
    gui.l3_b1 = tk.Label(gui.f_line_3, image = gui.img_card_back)

    try:
        gui.p1_card_1.set(player_hand_1.hand[0].location)
        gui.p1_card_2.set(player_hand_1.hand[1].location)
        gui.p1_card_3.set(player_hand_1.hand[2].location)
        gui.p1_card_4.set(player_hand_1.hand[3].location)
        gui.p1_card_5.set(player_hand_1.hand[4].location)
        gui.p1_card_6.set(player_hand_1.hand[5].location)
    except:
        return
    
    gui.img_l4b1 = tk.PhotoImage(file = gui.p1_card_1.get())
    gui.img_l4b2 = tk.PhotoImage(file = gui.p1_card_2.get())
    gui.img_l4b3 = tk.PhotoImage(file = gui.p1_card_3.get())
    gui.img_l4b4 = tk.PhotoImage(file = gui.p1_card_4.get())
    gui.img_l4b5 = tk.PhotoImage(file = gui.p1_card_5.get())
    gui.img_l4b6 = tk.PhotoImage(file = gui.p1_card_6.get())
    
    
    gui.l4_b1 = tk.Button(gui.f_line_4, image = gui.img_l4b1, highlightbackground = "black", \
                                background ='black', \
                                command = lambda: p1_button_1(battleground, player_hand_1, gui))
    gui.l4_b2 = tk.Button(gui.f_line_4, image = gui.img_l4b2, \
                                background ='black', command = lambda: p1_button_2(battleground, player_hand_1, gui))
    gui.l4_b3 = tk.Button(gui.f_line_4, image = gui.img_l4b3, \
                                background ='black',command = lambda: p1_button_3(battleground, player_hand_1, gui))
    gui.l4_b4 = tk.Button(gui.f_line_4, image = gui.img_l4b4, \
                                background ='black',command = lambda: p1_button_4(battleground, player_hand_1, gui))
    gui.l4_b5 = tk.Button(gui.f_line_4, image = gui.img_l4b5, \
                               background ='black',command = lambda: p1_button_5(battleground, player_hand_1, gui))
    gui.l4_b6 = tk.Button(gui.f_line_4, image = gui.img_l4b6, \
                               background ='black', command = lambda: p1_button_6(battleground, player_hand_1, gui)) 
    
    
    if number_players == 1:
        gui.p2_card_1.set(player_hand_2.hand[0].location)
        gui.p2_card_2.set(player_hand_2.hand[1].location)
        gui.p2_card_3.set(player_hand_2.hand[2].location)
        gui.p2_card_4.set(player_hand_2.hand[3].location)
        gui.p2_card_5.set(player_hand_2.hand[4].location)
        gui.p2_card_6.set(player_hand_2.hand[5].location)
             
        gui.l2_b1.grid(row=0, column=0)
        
        gui.l3_b1.grid(row=0, column=0)
        
        gui.l4_b1.grid(row=0, column=1)
        gui.l4_b2.grid(row=0, column=2)
        gui.l4_b3.grid(row=0, column=3)
        gui.l4_b4.grid(row=0, column=4)
        gui.l4_b5.grid(row=0, column=5)
        gui.l4_b6.grid(row=0, column=6)
        
        if gui.script_counter == 0:
            main_ai(battleground, player_hand_1, player_hand_2, \
                           player_1_deck, player_2_deck, gui, number_players)
            gui.script_counter += 1        
    
    else: 
        
        gui.p2_card_1.set(player_hand_2.hand[0].location)
        gui.p2_card_2.set(player_hand_2.hand[1].location)
        gui.p2_card_3.set(player_hand_2.hand[2].location)
        gui.p2_card_4.set(player_hand_2.hand[3].location)
        gui.p2_card_5.set(player_hand_2.hand[4].location)
        gui.p2_card_6.set(player_hand_2.hand[5].location)
        
        gui.img_l1b1 = tk.PhotoImage(file = gui.p2_card_1.get())
        gui.img_l1b2 = tk.PhotoImage(file = gui.p2_card_2.get())
        gui.img_l1b3 = tk.PhotoImage(file = gui.p2_card_3.get())
        gui.img_l1b4 = tk.PhotoImage(file = gui.p2_card_4.get())
        gui.img_l1b5 = tk.PhotoImage(file = gui.p2_card_5.get())
        gui.img_l1b6 = tk.PhotoImage(file = gui.p2_card_6.get())
        
        gui.l1_b1 = tk.Button(gui.f_line_1, image = gui.img_l1b1, highlightbackground = "black", \
                                    background ='black', \
                                    command = lambda: p2_button_1(battleground, player_hand_2, gui))
        gui.l1_b2 = tk.Button(gui.f_line_1, image = gui.img_l1b2, \
                                    background ='black', command = lambda: p2_button_2(battleground, player_hand_2, gui))
        gui.l1_b3 = tk.Button(gui.f_line_1, image = gui.img_l1b3, \
                                    background ='black',command = lambda: p2_button_3(battleground, player_hand_2, gui))
        gui.l1_b4 = tk.Button(gui.f_line_1, image = gui.img_l1b4, \
                                    background ='black',command = lambda: p2_button_4(battleground, player_hand_2, gui))
        gui.l1_b5 = tk.Button(gui.f_line_1, image = gui.img_l1b5, \
                                   background ='black',command = lambda: p2_button_5(battleground, player_hand_2, gui))
        gui.l1_b6 = tk.Button(gui.f_line_1, image = gui.img_l1b6, \
                                   background ='black', command = lambda: p2_button_6(battleground, player_hand_2, gui)) 
    
  
        gui.l1_b1.grid(row=0, column=1)
        gui.l1_b2.grid(row=0, column=2)
        gui.l1_b3.grid(row=0, column=3)
        gui.l1_b4.grid(row=0, column=4)
        gui.l1_b5.grid(row=0, column=5)
        gui.l1_b6.grid(row=0, column=6)
        
        gui.l2_b1.grid(row=0, column=0)
        
        gui.l3_b1.grid(row=0, column=0)
        
        gui.l4_b1.grid(row=0, column=1)
        gui.l4_b2.grid(row=0, column=2)
        gui.l4_b3.grid(row=0, column=3)
        gui.l4_b4.grid(row=0, column=4)
        gui.l4_b5.grid(row=0, column=5)
        gui.l4_b6.grid(row=0, column=6)
        
        if gui.script_counter == 0:
            main_ai(battleground, player_hand_1, player_hand_2, \
                           player_1_deck, player_2_deck, gui, number_players)
            gui.script_counter += 1
            
    
############################################
############################################
######              GUI               ######
############################################
############################################
# Give player_1 a point.
def player_1_point(gui):
    
    gui.player_1_scorecounter +=1
    gui.score_1.set(gui.player_1_scorecounter)
    
#Gives player_2 a point.
def player_2_point(gui):
    
    gui.player_2_scorecounter +=1
    gui.score_2.set(gui.player_2_scorecounter)

# Writes the necesary command to the GUI.
def console(gui,string):
    gui.text.set(string)

#The rendering of the GUI.
class GUI(tk.Frame):
        def __init__(self, battleground,player_1_hand, player_2_hand,player_1_deck,\
                     player_2_deck):
             
            self.N0 = Cards("None", 1000, ".\Card_back.gif")
            self.script_counter = 0
            self.equilize = 0
            
            self.win = tk.Tk()
            self.win.title("The Four Knights - H -> S -> D -> C")
                
            self.menubar = tk.Menu(self.win)
            self.filemenu = tk.Menu(self.menubar, tearoff = 0)
            self.filemenu.add_command(label = "Single Player", \
                                      command = lambda: update_battleground_ai \
                                                                (1, \
                                                                 player_1_hand, \
                                                                 player_2_hand, \
                                                                 battleground, \
                                                                 player_1_deck, \
                                                                 player_2_deck, \
                                                                 self))
            
            
            self.filemenu.add_command(label = "Victory Table", command = care)
            
            self.filemenu.add_separator()
            
            self.filemenu.add_command(label = "Quit", command = self.win.destroy)
            self.menubar.add_cascade(label = "Game", menu = self.filemenu)
            self.win.config( menu = self.menubar)
            
            
            self.background = tk.PhotoImage(file = ".\cherry-wood.gif")
            self.f_background = tk.Label(image = self.background)
            
            self.card_back = tk.StringVar()
            self.card_back.set(".\Card_back.gif")
            self.img_card_back = tk.PhotoImage(file = self.card_back.get())
            

            
            self.p2_card_1 = tk.StringVar()
            self.p2_card_2 = tk.StringVar()
            self.p2_card_3 = tk.StringVar()
            self.p2_card_4 = tk.StringVar()
            self.p2_card_5 = tk.StringVar()
            self.p2_card_6 = tk.StringVar()
            
            self.battleground_2 = tk.StringVar()
            self.battleground_1 = tk.StringVar()
            
            self.p1_card_1 = tk.StringVar()
            self.p1_card_2 = tk.StringVar()
            self.p1_card_3 = tk.StringVar()
            self.p1_card_4 = tk.StringVar()
            self.p1_card_5 = tk.StringVar()
            self.p1_card_6 = tk.StringVar()
            
            self.p2_card_1.set(".\Card_back.gif")
            self.p2_card_2.set(".\Card_back.gif")
            self.p2_card_3.set(".\Card_back.gif")
            self.p2_card_4.set(".\Card_back.gif")
            self.p2_card_5.set(".\Card_back.gif")
            self.p2_card_6.set(".\Card_back.gif")
           
            
            self.p1_card_1.set(".\Card_back.gif")
            self.p1_card_2.set(".\Card_back.gif")
            self.p1_card_3.set(".\Card_back.gif")
            self.p1_card_4.set(".\Card_back.gif")
            self.p1_card_5.set(".\Card_back.gif")
            self.p1_card_6.set(".\Card_back.gif")
            
            self.b_card_1 = tk.StringVar()
            self.b_card_1.set(".\Card_back.gif")
            
            self.battleground_1.set(".\Card_back.gif")
            self.img_battleground_1 = tk.PhotoImage(file = self.battleground_1.get())
            
            self.battleground_2.set(".\Card_back.gif")
            self.img_battleground_2 = tk.PhotoImage(file = self.battleground_2.get())
            
            self.img_l1b1 = tk.PhotoImage(file = self.p2_card_1.get())
            self.img_l1b2 = tk.PhotoImage(file = self.p2_card_2.get())
            self.img_l1b3 = tk.PhotoImage(file = self.p2_card_3.get())
            self.img_l1b4 = tk.PhotoImage(file = self.p2_card_4.get())
            self.img_l1b5 = tk.PhotoImage(file = self.p2_card_5.get())
            self.img_l1b6 = tk.PhotoImage(file = self.p2_card_6.get())
            
            self.img_l4b1 = tk.PhotoImage(file = self.p1_card_1.get())
            self.img_l4b2 = tk.PhotoImage(file = self.p1_card_2.get())
            self.img_l4b3 = tk.PhotoImage(file = self.p1_card_3.get())
            self.img_l4b4 = tk.PhotoImage(file = self.p1_card_4.get())
            self.img_l4b5 = tk.PhotoImage(file = self.p1_card_5.get())
            self.img_l4b6 = tk.PhotoImage(file = self.p1_card_6.get())
            
            self.f_line_1 = tk.Frame(self.f_background)
            self.l1_b1 = tk.Button(self.f_line_1, image = self.img_l1b1, highlightbackground = "black", \
                                    background ='black', \
                                    command = care)
            self.l1_b2 = tk.Button(self.f_line_1, image = self.img_l1b2, \
                                    background ='black',command = care)
            self.l1_b3 = tk.Button(self.f_line_1, image = self.img_l1b3, \
                                    background ='black',command = care)
            self.l1_b4 = tk.Button(self.f_line_1, image = self.img_l1b4, \
                                    background ='black',command = care)
            self.l1_b5 = tk.Button(self.f_line_1, image = self.img_l1b5, \
                                   background ='black',command = care)
            self.l1_b6 = tk.Button(self.f_line_1, image = self.img_l1b6, \
                                   background ='black', command = care)
            
            self.f_line_2 = tk.Frame(self.f_background)
            self.l2_b1 = tk.Label(self.f_line_2, image = self.img_battleground_2)
            
            
            self.f_line_3 = tk.Frame(self.f_background)
            self.l3_b1 = tk.Label(self.f_line_3, image = self.img_battleground_1)
            
            self.f_line_4 = tk.Frame(self.f_background)
            self.l4_b1 = tk.Button(self.f_line_4, image = self.img_l4b1, \
                                   background ='black', command = care)
            self.l4_b2 = tk.Button(self.f_line_4, image = self.img_l4b2, \
                                   background ='black', command = care)
            self.l4_b3 = tk.Button(self.f_line_4, image = self.img_l4b3, \
                                   background ='black', command = care)
            self.l4_b4 = tk.Button(self.f_line_4, image = self.img_l4b4, \
                                   background ='black', command = care)
            self.l4_b5 = tk.Button(self.f_line_4, image = self.img_l4b5, \
                                   background ='black', command = care)
            self.l4_b6 = tk.Button(self.f_line_4, image = self.img_l4b6, \
                                   background ='black', command = care)
            
            self.f_background.pack()
            
            self.f_line_1.grid(row=1, column=1)
            self.l1_b1.grid(row=0, column=1)
            self.l1_b2.grid(row=0, column=2)
            self.l1_b3.grid(row=0, column=3)
            self.l1_b4.grid(row=0, column=4)
            self.l1_b5.grid(row=0, column=5)
            self.l1_b6.grid(row=0, column=6)
            
            self.f_line_2.grid(row=2, column=1)
            self.l2_b1.grid(row=0, column=0 )
                  
            self.f_line_3.grid(row=4, column=1)
            self.l3_b1.grid(row=0, column=0)
            
            self.f_line_4.grid(row=5, column=1)
            self.l4_b1.grid(row=0, column=1)
            self.l4_b2.grid(row=0, column=2)
            self.l4_b3.grid(row=0, column=3)
            self.l4_b4.grid(row=0, column=4)
            self.l4_b5.grid(row=0, column=5)
            self.l4_b6.grid(row=0, column=6)

            self.order = tk.BooleanVar()

            self.player_1_scorecounter = 0
            self.player_2_scorecounter = 0
            
            self.score_board = tk.Toplevel()
            self.f_line35 = tk.Frame(self.score_board)

            self.f_line35.grid(row = 3, column = 1)
            
            self.text = tk.StringVar()
            self.text_box = tk.Label(self.f_line35 ,textvariable = self.text)   
            self.score_1 = tk.StringVar()
            self.score_1_box = tk.Label(self.f_line35, textvariable = self.score_1)
            self.score_2 = tk.StringVar()
            self.score_2_box = tk.Label(self.f_line35, textvariable = self.score_2)
            
            self.score_1_prompt = tk.StringVar()
            self.score_1_boxside = tk.Label(self.f_line35, textvariable = self.score_1_prompt)
            self.score_2_prompt = tk.StringVar()
            self.score_2_boxside = tk.Label(self.f_line35, textvariable = self.score_2_prompt)

            self.text_box.pack()
            self.score_1_box.pack(side = "left")
            self.score_1_boxside.pack(side = "left")
            self.score_2_boxside.pack(side = "left")
            self.score_2_box.pack(side = "left")
            
            self.text.set("Welcome to four knights!")
            self.score_1_prompt.set(":                        Player 1 --- SCORES ")
            self.score_2_prompt.set("--- Player 2                       :")
            
            self.score_1.set(0)
            self.score_2.set(0)

            self.win.mainloop()
            
        def wait_order(self):
            self.win.wait_variable( name = self.order)
            

# The player button definitions................... All of them!

def p2_button_1(battleground, player_hand, gui):
    
    gui.p2_card_1.set(".\Card_back.gif")
    gui.img_l1b1 = tk.PhotoImage(file = gui.p2_card_1.get())
    
    gui.l1_b1 = tk.Label(gui.f_line_1, image = gui.img_l1b1, highlightbackground = "black", \
                                background ='black')
    
    
    gui.battleground_2.set(player_hand.hand[0].location)
    gui.img_battleground_2 = tk.PhotoImage(file = gui.battleground_2.get())
    
    gui.l1_b1 = tk.Label(gui.f_line_1, image = gui.img_l1b1, highlightbackground = "black", \
                                background ='black')
    
    gui.l2_b1 = tk.Label(gui.f_line_2, image = gui.img_battleground_2, background ='black')
    
  
    gui.l1_b1.grid(row=0, column=1)
    gui.l2_b1.grid(row = 0, column = 0)
    
    player_hand.index = 0

def p2_button_2(battleground, player_hand, gui):

    gui.p2_card_1.set(".\Card_back.gif")
    gui.img_l1b2 = tk.PhotoImage(file = gui.p2_card_1.get())
    
    gui.l1_b2 = tk.Label(gui.f_line_1, image = gui.img_l1b2, highlightbackground = "black", \
                                background ='black')
    
    
    gui.battleground_2.set(player_hand.hand[1].location)
    gui.img_battleground_2 = tk.PhotoImage(file = gui.battleground_2.get())
    
    gui.l1_b2 = tk.Label(gui.f_line_1, image = gui.img_l1b2, highlightbackground = "black", \
                                background ='black')
    
    gui.l2_b1 = tk.Label(gui.f_line_2, image = gui.img_battleground_2, background ='black')
    
    gui.l1_b2.grid(row=0, column=2)
    gui.l2_b1.grid(row = 0, column = 0)
    
    player_hand.index = 1
     
def p2_button_3(battleground, player_hand, gui):
    gui.p2_card_1.set(".\Card_back.gif")
    gui.img_l1b3 = tk.PhotoImage(file = gui.p2_card_1.get())
    
    gui.l1_b3 = tk.Label(gui.f_line_1, image = gui.img_l1b3, highlightbackground = "black", \
                                background ='black')
    
    
    gui.battleground_2.set(player_hand.hand[2].location)
    gui.img_battleground_2 = tk.PhotoImage(file = gui.battleground_2.get())
    
    gui.l1_b3 = tk.Label(gui.f_line_1, image = gui.img_l1b3, highlightbackground = "black", \
                                background ='black')
    
    gui.l2_b1 = tk.Label(gui.f_line_2, image = gui.img_battleground_2, background ='black')
    
    gui.l1_b3.grid(row=0, column=3)
    gui.l2_b1.grid(row = 0, column = 0)
    
    player_hand.index = 2
        
def p2_button_4(battleground, player_hand, gui):
    gui.p2_card_1.set(".\Card_back.gif")
    gui.img_l1b4 = tk.PhotoImage(file = gui.p2_card_1.get())
    
    gui.l1_b4 = tk.Label(gui.f_line_1, image = gui.img_l1b4, highlightbackground = "black", \
                                background ='black')
    
    
    gui.battleground_2.set(player_hand.hand[3].location)
    gui.img_battleground_2 = tk.PhotoImage(file = gui.battleground_2.get())
    
    gui.l1_b4 = tk.Label(gui.f_line_1, image = gui.img_l1b4, highlightbackground = "black", \
                                background ='black')
    
    gui.l2_b1 = tk.Label(gui.f_line_2, image = gui.img_battleground_2, background ='black')
    
    gui.l1_b4.grid(row=0, column=4)
    gui.l2_b1.grid(row = 0, column = 0)
    
    player_hand.index = 3
    
def p2_button_5(battleground, player_hand, gui):
    gui.p2_card_1.set(".\Card_back.gif")
    gui.img_l1b5 = tk.PhotoImage(file = gui.p2_card_1.get())
    
    gui.l1_b5 = tk.Label(gui.f_line_1, image = gui.img_l1b5, highlightbackground = "black", \
                                background ='black')
    
    
    gui.battleground_2.set(player_hand.hand[4].location)
    gui.img_battleground_2 = tk.PhotoImage(file = gui.battleground_2.get())
    
    gui.l1_b5 = tk.Label(gui.f_line_1, image = gui.img_l1b5, highlightbackground = "black", \
                                background ='black')
    
    gui.l2_b1 = tk.Label(gui.f_line_2, image = gui.img_battleground_2, background ='black')
    
    gui.l1_b5.grid(row=0, column=5)
    gui.l2_b1.grid(row = 0, column = 0)
    
    player_hand.index = 4
        
def p2_button_6(battleground, player_hand, gui):
    gui.p2_card_1.set(".\Card_back.gif")
    gui.img_l1b6 = tk.PhotoImage(file = gui.p2_card_1.get())
    
    gui.l1_b6 = tk.Label(gui.f_line_1, image = gui.img_l1b6, highlightbackground = "black", \
                                background ='black')
    
    
    gui.battleground_2.set(player_hand.hand[5].location)
    gui.img_battleground_2 = tk.PhotoImage(file = gui.battleground_2.get())
    
    gui.l1_b6 = tk.Label(gui.f_line_1, image = gui.img_l1b6, highlightbackground = "black", \
                                background ='black')
    
    gui.l2_b1 = tk.Label(gui.f_line_2, image = gui.img_battleground_2, background ='black')
    
    gui.l1_b6.grid(row=0, column=6)
    gui.l2_b1.grid(row = 0, column = 0)
    
    player_hand.index = 5
    
     
def p1_button_1(battleground,player_hand, gui):
    if acceptable_card(player_hand.hand[0], battleground):
        gui.p1_card_1.set(".\Card_back.gif")
        gui.img_l4b1 = tk.PhotoImage(file = gui.p1_card_1.get())
        
        gui.l4_b1 = tk.Label(gui.f_line_4, image = gui.img_l4b1, highlightbackground = "black", \
                                    background ='black')
        
        
        gui.battleground_1.set(player_hand.hand[0].location)
        gui.img_battleground_1 = tk.PhotoImage(file = gui.battleground_1.get())
        
        gui.l4_b1 = tk.Label(gui.f_line_4, image = gui.img_l4b1, highlightbackground = "black", \
                                    background ='black')
        
        gui.l3_b1 = tk.Label(gui.f_line_3, image = gui.img_battleground_1, background ='black')
        
        gui.l4_b1.grid(row=0, column= 1)
        gui.l3_b1.grid(row = 0, column = 0)

        player_hand.index = 0
        gui.order.set(True)

def p1_button_2(battleground,player_hand, gui):
    if acceptable_card(player_hand.hand[1], battleground):
        gui.p1_card_2.set(".\Card_back.gif")
        gui.img_l4b2 = tk.PhotoImage(file = gui.p1_card_2.get())
        
        gui.l4_b2 = tk.Label(gui.f_line_4, image = gui.img_l4b2, highlightbackground = "black", \
                                    background ='black')
        
        
        gui.battleground_1.set(player_hand.hand[1].location)
        gui.img_battleground_1 = tk.PhotoImage(file = gui.battleground_1.get())
        
        gui.l4_b2 = tk.Label(gui.f_line_4, image = gui.img_l4b2, highlightbackground = "black", \
                                    background ='black')
        
        gui.l3_b1 = tk.Label(gui.f_line_3, image = gui.img_battleground_1, background ='black')
        
        gui.l4_b2.grid(row=0, column= 2)
        gui.l3_b1.grid(row = 0, column = 0)
        
        player_hand.index = 1
        
        gui.order.set(True)
         
def p1_button_3(battleground,player_hand, gui):
    if acceptable_card(player_hand.hand[2], battleground):
        gui.p1_card_3.set(".\Card_back.gif")
        gui.img_l4b3 = tk.PhotoImage(file = gui.p1_card_3.get())
        
        gui.l4_b3 = tk.Label(gui.f_line_4, image = gui.img_l4b3, highlightbackground = "black", \
                                    background ='black')
        
        
        gui.battleground_1.set(player_hand.hand[2].location)
        gui.img_battleground_1 = tk.PhotoImage(file = gui.battleground_1.get())
        
        gui.l4_b3 = tk.Label(gui.f_line_4, image = gui.img_l4b3, highlightbackground = "black", \
                                    background ='black')
        
        gui.l3_b1 = tk.Label(gui.f_line_3, image = gui.img_battleground_1, background ='black')
        
        gui.l4_b3.grid(row=0, column= 3)
        gui.l3_b1.grid(row = 0, column = 0)
        
        player_hand.index = 2
        
        gui.order.set(True)
        
def p1_button_4(battleground,player_hand, gui):
    if acceptable_card(player_hand.hand[3], battleground):
        gui.p1_card_4.set(".\Card_back.gif")
        gui.img_l4b4 = tk.PhotoImage(file = gui.p1_card_4.get())
    
        gui.l4_b4 = tk.Label(gui.f_line_4, image = gui.img_l4b4, highlightbackground = "black", \
                                    background ='black')
        
        
        gui.battleground_1.set(player_hand.hand[3].location)
        gui.img_battleground_1 = tk.PhotoImage(file = gui.battleground_1.get())
        
        gui.l4_b4 = tk.Label(gui.f_line_4, image = gui.img_l4b4, highlightbackground = "black", \
                                    background ='black')
        
        gui.l3_b1 = tk.Label(gui.f_line_3, image = gui.img_battleground_1, background ='black')
        
        gui.l4_b4.grid(row=0, column=4)
        gui.l3_b1.grid(row = 0, column = 0)
        
        player_hand.index = 3
        
        gui.order.set(True)
        
def p1_button_5(battleground, player_hand, gui):
    if acceptable_card(player_hand.hand[4], battleground):
        gui.p1_card_5.set(".\Card_back.gif")
        gui.img_l4b5 = tk.PhotoImage(file = gui.p1_card_5.get())
        
        gui.l4_b5 = tk.Label(gui.f_line_4, image = gui.img_l4b5, highlightbackground = "black", \
                                    background ='black')
        
        
        gui.battleground_1.set(player_hand.hand[4].location)
        gui.img_battleground_1 = tk.PhotoImage(file = gui.battleground_1.get())
        
        gui.l4_b5 = tk.Label(gui.f_line_4, image = gui.img_l4b5, highlightbackground = "black", \
                                    background ='black')
        
        gui.l3_b1 = tk.Label(gui.f_line_3, image = gui.img_battleground_1, background ='black')
        
        gui.l4_b5.grid(row=0, column=5)
        gui.l3_b1.grid(row = 0, column = 0)
        
        player_hand.index = 4 
        
        gui.order.set(True)
    
def p1_button_6(battleground, player_hand, gui):
    if acceptable_card(player_hand.hand[5], battleground):
        gui.p1_card_6.set(".\Card_back.gif")
        gui.img_l4b6 = tk.PhotoImage(file = gui.p1_card_6.get())
        
        gui.l4_b6 = tk.Label(gui.f_line_4, image = gui.img_l4b6, highlightbackground = "black", \
                                    background ='black')
        
        
        gui.battleground_1.set(player_hand.hand[5].location)
        gui.img_battleground_1 = tk.PhotoImage(file = gui.battleground_1.get())
        
        gui.l4_b6 = tk.Label(gui.f_line_4, image = gui.img_l4b6, highlightbackground = "black", \
                                    background ='black')
        
        gui.l3_b1 = tk.Label(gui.f_line_3, image = gui.img_battleground_1, background ='black')
        
        
        gui.l3_b1.grid(row = 0, column = 0)
        gui.l4_b6.grid(row=0, column=6)
        
        player_hand.index = 5
        
        gui.order.set(True)

# Place holder function for empty buttons.
def care():
    return

############################################
############################################
####              MAIN                  ####
############################################
############################################
    

# The main function that creates all the deck, cards and starts the program.

def initilization():

    # A list of cards representing the deck.       
    H1 = Cards("hearts", 14, ".\Ace_hearts.gif")
    H2 = Cards("hearts", 2, ".\Two_hearts.gif")
    H3 = Cards("hearts", 3, ".\Three_hearts.gif")
    H4 = Cards("hearts", 4, ".\Four_hearts.gif")
    H5 = Cards("hearts", 5, ".\Five_hearts.gif")
    H6 = Cards("hearts", 6, ".\Six_hearts.gif")
    H7 = Cards("hearts", 7, ".\Seven_hearts.gif")
    H8 = Cards("hearts", 8, ".\Eight_hearts.gif")
    H9 = Cards("hearts", 9, ".\Nine_hearts.gif")
    H10 = Cards("hearts",10, ".\Ten_hearts.gif")
    HJ = Cards("hearts", 11, ".\Jack_hearts.gif")
    HQ = Cards("hearts", 12, ".\Queen_hearts.gif")
    HK = Cards("hearts", 13, ".\King_hearts.gif")
            
    S1 = Cards("spades", 14, ".\Ace_spades.gif")
    S2 = Cards("spades", 2, ".\Two_spades.gif")
    S3 = Cards("spades", 3, ".\Three_spades.gif")
    S4 = Cards("spades", 4, ".\Four_spades.gif")
    S5 = Cards("spades", 5, ".\Five_spades.gif")
    S6 = Cards("spades", 6, ".\Six_spades.gif")
    S7 = Cards("spades", 7, ".\Seven_spades.gif")
    S8 = Cards("spades", 8, ".\Eight_spades.gif")
    S9 = Cards("spades", 9, ".\Nine_spades.gif")
    S10 = Cards("spades",10, ".\Ten_spades.gif")
    SJ = Cards("spades", 11, ".\Jack_spades.gif")
    SQ = Cards("spades", 12, ".\Queen_spades.gif")
    SK = Cards("spades", 13, ".\King_spades.gif")
    
    D1 = Cards("diamonds", 14, ".\Ace_diamonds.gif")
    D2 = Cards("diamonds", 2, ".\Two_diamonds.gif")
    D3 = Cards("diamonds", 3, ".\Three_diamonds.gif")
    D4 = Cards("diamonds", 4, ".\Four_diamonds.gif")
    D5 = Cards("diamonds", 5, ".\Five_diamonds.gif")
    D6 = Cards("diamonds", 6, ".\Six_diamonds.gif")
    D7 = Cards("diamonds", 7, ".\Seven_diamonds.gif")
    D8 = Cards("diamonds", 8, ".\Eight_diamonds.gif")
    D9 = Cards("diamonds", 9, ".\Nine_diamonds.gif")
    D10 = Cards("diamonds",10, ".\Ten_diamonds.gif")
    DJ = Cards("diamonds", 11, ".\Jack_diamonds.gif")
    DQ = Cards("diamonds", 12, ".\Queen_diamonds.gif")
    DK = Cards("diamonds", 13, ".\King_diamonds.gif")
    
    C1 = Cards("clubs", 14, ".\Ace_clubs.gif")
    C2 = Cards("clubs", 2, ".\Two_clubs.gif")
    C3 = Cards("clubs", 3, ".\Three_clubs.gif")
    C4 = Cards("clubs", 4, ".\Four_clubs.gif")
    C5 = Cards("clubs", 5, ".\Five_clubs.gif")
    C6 = Cards("clubs", 6, ".\Six_clubs.gif")
    C7 = Cards("clubs", 7, ".\Seven_clubs.gif")
    C8 = Cards("clubs", 8, ".\Eight_clubs.gif")
    C9 = Cards("clubs", 9, ".\Nine_clubs.gif")
    C10 = Cards("clubs",10, ".\Ten_clubs.gif")
    CJ = Cards("clubs",  11, ".\Jack_clubs.gif")
    CQ = Cards("clubs", 12, ".\Queen_clubs.gif")
    CK = Cards("clubs", 13, ".\King_clubs.gif")
    
    N0 = Cards("", 0, ".\Card_back.gif")
    
    hearts =   [H1,H2,H3,H4,H5,H6,H7,H8,H9,H10,HJ,HQ,HK]
    spades =   [S1,S2,S3,S4,S5,S6,S7,S8,S9,S10,SJ,SQ,SK]
    diamonds = [D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,DJ,DQ,DK]
    clubs =    [C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,CJ,CQ,CK]
    
    deck_list = hearts + spades + diamonds + clubs
    
    main_deck = Deck(deck_list)  
    main_deck.shuffle()
    
    (stockades, player_1_deck, player_2_deck) = main_deck.deal()
    
    battleground = Battleground(None,None)
    
    player_1_hand = player_1_deck.draw_hand()
    player_2_hand = player_2_deck.draw_hand()
    
    index = 0
    
    bigbang = GUI(battleground,player_1_hand,player_2_hand,player_1_deck,\
          player_2_deck)
    

#The magic happens here.

initilization()