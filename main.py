
from turtle import Turtle, Screen
from tkinter import messagebox
import random


def race_game():
    """Starts the game"""
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    all_turtle = []
    y_cord = -100
    screen = Screen()
    screen.setup(width=500, height=400)
    screen.title("Welcome to the Turtle racing game !")
    available_color = ', '.join(colors)
    messagebox.showinfo("Available turtle color", f"{available_color}")
    user_bet = screen.textinput(title='Make a bet', prompt='which turtle color will win the race? Enter a color: ')
    screen.clear()
    if user_bet:
        # Creates instances
        for x in range(len(colors)):
            new_turtle = Turtle(shape='turtle')
            new_turtle.penup()
            new_turtle.goto(x=-230, y=y_cord)
            new_turtle.color(colors[x])
            y_cord += 40
            all_turtle.append(new_turtle)

        game_on = True
        while game_on:

            # Starts the race
            for turtle in all_turtle:
                random_move = random.randint(0, 10)
                turtle.forward(random_move)

                # Checks if the turtle has reached the finish line
                if turtle.xcor() > 230:
                    game_on = False
                    winner = turtle.pencolor()
                    if winner == user_bet:
                        messagebox.showinfo("You've won!", f"The {winner} turtle is the winner!")
                        return True
                    else:
                        messagebox.showinfo("You've lost!", f"The {winner} turtle is the winner!")
                        return False
    else:
        messagebox.showinfo('No choice made', 'In-other to play you must pick a color ')

    screen.exitonclick()


def scores(win):
    """Adds up the Scores."""
    score = 0
    if win:
        score += 1
        return score
    else:
        return score


game_start = True
while game_start:
    won = race_game()
    user_score = scores(won)
    proceed = messagebox.askyesno('Do you want to continue')
    if not proceed:
        game_start = False
        messagebox.showinfo('Your Score', f"You scored: {user_score}")

