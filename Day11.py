#blackjack / 21 game
import random
import blackjack


def jack_game():
   
    play=input("if u want to play the game say 'y' if not 'n' :")
    if play=="n":
        return
    print(blackjack.logo)
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    def rand_card():
        card=random.choice(cards)
        return card
    your_choice=[]
    cmp_choice=[]
    for i in range(2):
        your_choice.append(rand_card())
        cmp_choice.append(rand_card())
    first_score=sum(your_choice)
    cmp_score=sum(cmp_choice)
    while cmp_score!=0 and cmp_score<17:
        cmp_choice.append(rand_card())
        cmp_score=sum(cmp_choice)

    if first_score==21 and len(your_choice)==2 or cmp_score==21:
        return 0 #which represents a black jack in our game
    if first_score>21:
        print("you lose")
    
    print(f"your cards:{your_choice}, The sum:{first_score}\ncomputer card:{cmp_choice[0]}")
    again=input("if u want another card say 'y' if u want to pass say 'n' :")
    while again=="y":
        your_choice.append(rand_card())
        first_score=sum(your_choice)
        if 11 in your_choice and first_score>21:
            your_choice.remove(11)
            your_choice.append(1)
            first_score=sum(your_choice)

        print(f"your choice: {your_choice},the sum: {first_score}\n computer card: {cmp_choice[0]}")
        if first_score>21:
            print("you lose!")
            jack_game()
        again=input("if u want another card say 'y' if u want to pass say 'n' :")
  
    print(f"your cards:{your_choice}, the sum:{first_score}\ncomputer card:{cmp_choice} ,the sum:{cmp_score} ")
    def compare(first_score,cmp_score):
       
        if first_score==cmp_score:
            return "it is draw"
        elif cmp_score==0:
            return "lose, opponent has blackjack"
        elif first_score==0:
            return "you win with a blackjack"
        elif first_score>21:
            return "you went over. you lose"
        elif cmp_score>21:
            return "opponent went over. you win"
        elif first_score>cmp_score:
            return "you win"
        else:
            return "you lose"

    print(compare(first_score,cmp_score))
    jack_game()
jack_game()
