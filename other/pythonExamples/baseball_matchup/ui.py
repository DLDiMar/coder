import tkinter as tk
from tkinter import ttk
from data_layer import store_matchup, get_previous_matchup
from web_scraper import get_random_player, verify_player

def simulate_matchup():
    pitcher = pitcher_entry.get()
    batter = batter_entry.get()
    if verify_player(pitcher) and verify_player(batter):
        outs = outs_var.get()
        home_pitcher = home_pitcher_var.get()
        home_batter = home_batter_var.get()
        score = score_var.get()
        inning = inning_var.get()
        outcome = get_matchup(pitcher, batter, outs, home_pitcher, home_batter, score, inning)
        store_matchup(pitcher, batter, outcome)
        outcome_label.config(text='Outcome: ' + outcome)
    else:
        outcome_label.config(text='Invalid pitcher or batter')

def random_pitcher():
    pitcher_entry.delete(0, 'end')
    pitcher_entry.insert(0, get_random_player('pitcher'))

def random_batter():
    batter_entry.delete(0, 'end')
    batter_entry.insert(0, get_random_player('batter'))

root = tk.Tk()
root.title('Baseball Matchup Simulator')

pitcher_label = tk.Label(root, text='Pitcher:')
pitcher_label.grid(row=0, column=0)

pitcher_entry = tk.Entry(root)
pitcher_entry.grid(row=0, column=1)

batter_label = tk.Label(root, text='Batter:')
batter_label.grid(row=1, column=0)

batter_entry = tk.Entry(root)
batter_entry.grid(row=1, column=1)

outs_label = tk.Label(root, text='Outs:')
outs_label.grid(row=2, column=0)

outs_var = tk.StringVar(root)
outs_var.set('0')  # default value
outs_menu = tk.OptionMenu(root, outs_var, '0', '1', '2')
outs_menu.grid(row=2, column=1)

home_pitcher_label = tk.Label(root, text='Home Pitcher:')
home_pitcher_label.grid(row=3, column=0)

home_pitcher_var = tk.StringVar(root)
home_pitcher_var.set('Yes')  # default value
home_pitcher_menu = tk.OptionMenu(root, home_pitcher_var, 'Yes', 'No')
home_pitcher_menu.grid(row=3, column=1)

home_batter_label = tk.Label(root, text='Home Batter:')
home_batter_label.grid(row=4, column=0)

home_batter_var = tk.StringVar(root)
home_batter_var.set('Yes')  # default value
home_batter_menu = tk.OptionMenu(root, home_batter_var, 'Yes', 'No')
home_batter_menu.grid(row=4, column=1)

score_label = tk.Label(root, text='Score:')
score_label.grid(row=5, column=0)

score_var = tk.StringVar(root)
score_var.set('Tied')  # default value
score_menu = tk.OptionMenu(root, score_var, 'Tied', 'Ahead', 'Behind')
score_menu.grid(row=5, column=1)

inning_label = tk.Label(root, text='Inning:')
inning_label.grid(row=6, column=0)

inning_var = tk.StringVar(root)
inning_var.set('1')  # default value
inning_menu = tk.OptionMenu(root, inning_var, '1', '2', '3', '4', '5', '6', '7', '8', '9')
inning_menu.grid(row=6, column=1)

simulate_button = tk.Button(root, text='Simulate Matchup', command=simulate_matchup)
simulate_button.grid(row=7, column=0, columnspan=2)

random_pitcher_button = tk.Button(root, text='Random Pitcher', command=random_pitcher)
random_pitcher_button.grid(row=0, column=2)

random_batter_button = tk.Button(root, text='Random Batter', command=random_batter)
random_batter_button.grid(row=1, column=2)

outcome_label = tk.Label(root, text='')
outcome_label.grid(row=8, column=0, columnspan=3)

root.mainloop()