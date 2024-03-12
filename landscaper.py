tools = [
    {"name": 'teeth' , "generates": 1, 'price': 0 },
    {"name": 'scissors', "generates": 5, 'price': 5 },
    {"name": 'old lawnmower', 'generates': 10, 'price': 10 },
    {"name": 'new lawnmower', 'generates': 20, 'price': 20 },
    {"name": 'students', 'generates': 50, 'price': 50 }
]

player = {
    'money': 0,
    'tool': 0,
    'winning': False
}

def mowlawn():
    global player
    tool = tools[player["tool"]]
    print(f"You cut a lawn with {tool['name']} and make {tool['generates']} dollars")
    player['money'] += tool['generates']

def upgrade():
    global player

    if player['tool'] + 1 < len(tools):
        next_tool = tools[player["tool"]+1]

        if next_tool['price'] <= player['money']:
            player['money'] -= next_tool["price"]
            player['tool'] += 1

        else:
            print('Money is not enough for this upgrade.')
    else:
        print("You've hired the students and this is the most you can upgrade to.")

def win_game():
    global player
    if player ['money'] >= 100 & player['tool'] == len(tools) - 1:
       print('"Congrats!!! You won the game')
       player["winning"] = True


print("Welcome to the landscaper simulation!!")

while not player['winning']:
    response = input(f"You currently have {player['money']} dollars [m]ow lawns or [u]pgrade? ")
    if response == 'm':
        mowlawn()
    elif response == 'u':
        upgrade()
    else:
        print("Slayyy!! But this is not a valid option. You gotta bills to pay. Type [m] or [u].")
    win_game()