Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=================== RESTART: /Users/agil/Desktop/blackjack.py ==================
Blackjack, by Al Sweigart al@inventwithpython.com

Rules:
Try to get as close to 21 without going over.
Kings, Queens, and Jacks are worth 10 points.
Aces are worth 1 or 11 points.
Cards 2 through 10 are worth their face value.
(H)it to take another card.
(S)tand to stop taking cards.
On your first play, you can (D)ouble down to increase your bet
but must hit exactly one more time before standing.
In case of a tie, the bet is returned to the player.
The dealer stops hitting at 17.
Money: 5000
How much do you bet? (1-5000, or QUIT)
> 3
Bet: 3

DEALER: ???
 ___  ___ 
|## | |K  | 
|###| | ♥ | 
|_##| |__K| 

PLAYER: 20
 ___  ___ 
|J  | |Q  | 
| ♥ | | ♥ | 
|__J| |__Q| 


(H)it, (S)tand, (D)ouble down> h
You drew a 4 of ♣.

DEALER: ???
 ___  ___ 
|## | |K  | 
|###| | ♥ | 
|_##| |__K| 

PLAYER: 24
 ___  ___  ___ 
|J  | |Q  | |4  | 
| ♥ | | ♥ | | ♣ | 
|__J| |__Q| |__4| 






DEALER: 20
 ___  ___ 
|10 | |K  | 
| ♦ | | ♥ | 
|_10| |__K| 

PLAYER: 24
 ___  ___  ___ 
|J  | |Q  | |4  | 
| ♥ | | ♥ | | ♣ | 
|__J| |__Q| |__4| 

You lost!
Press Enter to continue...



Money: 4997
How much do you bet? (1-4997, or QUIT)
> 7
Bet: 7

DEALER: ???
 ___  ___ 
|## | |10 | 
|###| | ♠ | 
|_##| |_10| 

PLAYER: 16
 ___  ___ 
|5  | |A  | 
| ♣ | | ♣ | 
|__5| |__A| 


(H)it, (S)tand, (D)ouble down> s




DEALER: 20
 ___  ___ 
|10 | |10 | 
| ♣ | | ♠ | 
|_10| |_10| 

PLAYER: 16
 ___  ___ 
|5  | |A  | 
| ♣ | | ♣ | 
|__5| |__A| 

You lost!
Press Enter to continue...



Money: 4990
How much do you bet? (1-4990, or QUIT)
> 0
How much do you bet? (1-4990, or QUIT)
> 9
Bet: 9

DEALER: ???
 ___  ___ 
|## | |K  | 
|###| | ♠ | 
|_##| |__K| 

PLAYER: 16
 ___  ___ 
|5  | |A  | 
| ♣ | | ♣ | 
|__5| |__A| 


(H)it, (S)tand, (D)ouble down> d
How much do you bet? (1-9, or QUIT)
> 9
Bet increased to 18.
Bet: 18
You drew a 7 of ♠.
Dealer hits...

DEALER: ???
 ___  ___  ___ 
|## | |K  | |A  | 
|###| | ♠ | | ♦ | 
|_##| |__K| |__A| 

PLAYER: 13
 ___  ___  ___ 
|5  | |A  | |7  | 
| ♣ | | ♣ | | ♠ | 
|__5| |__A| |__7| 

Press Enter to continue...
Dealer hits...

DEALER: ???
 ___  ___  ___  ___ 
|## | |K  | |A  | |10 | 
|###| | ♠ | | ♦ | | ♥ | 
|_##| |__K| |__A| |_10| 

PLAYER: 13
 ___  ___  ___ 
|5  | |A  | |7  | 
| ♣ | | ♣ | | ♠ | 
|__5| |__A| |__7| 





DEALER: 23
 ___  ___  ___  ___ 
|2  | |K  | |A  | |10 | 
| ♣ | | ♠ | | ♦ | | ♥ | 
|__2| |__K| |__A| |_10| 

PLAYER: 13
 ___  ___  ___ 
|5  | |A  | |7  | 
| ♣ | | ♣ | | ♠ | 
|__5| |__A| |__7| 

Dealer busts! You win $18!
