import requests
from bs4 import BeautifulSoup
from random import randint, choice

def get_random_player(player_type):
    url = 'https://www.baseball-reference.com/players/' + get_random_initials()[0].lower() + '/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    players = [a.text for a in soup.find_all('a') if a.text]
    return choice(players)

def get_random_initials():
    first_initial = chr(randint(65, 90))  # Get a random uppercase letter
    second_initial = chr(randint(65, 90))  # Get a random uppercase letter
    return first_initial + second_initial

def verify_player(player_name):
    url = 'https://www.baseball-reference.com/players/' + player_name[0].lower() + '/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    players = [a.text for a in soup.find_all('a') if a.text]
    return player_name in players