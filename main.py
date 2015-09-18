import civilization, pickle, sys, jsonpickle, os, random

SAVEFILE = 'savegame.json'
game_state = dict()
turn_count = 0

def newGame():
    check = False
    save = input('New Game?')
    if save == 'y' or save == 'yes':
        check = True
    return check

def saveCiv():
    global game_state
    with open(SAVEFILE, 'w') as savegame:
        savegame.write(jsonpickle.encode(game_state))

def loadCiv():
    with open(SAVEFILE, 'r') as savegame:
        state = jsonpickle.decode(savegame.read())
    return state

def createCiv():
    global civ
    leader = input('Enter your name: ')
    nation = input('Enter your nation\'s name: ')
    seed = random.seed()
    civ = civilization.Civilization(nation, leader, seed)
    state = dict()
    state['playerciv'] = [civ]
    return state

def passTurn():
    global turn_count
    turn_count+=1
    civ.increasePop()

def gamePrompt():
    
    action = input('What would you like to do, great leader? ')
    if action == 'new':
        createCiv()
    if action == 'save':
        saveCiv()
    if action == 'load':
        loadCiv()
    if action == 'end':
        passTurn()
    if action == 'exit':
        sys.exit()

def getStatus():
    global game_state
    global civ
    civ = game_state['playerciv'][0]
    status = ['Population', civ.population, 'Growth Rate', civ.growthRate, 'Happiness', civ.happiness]
    return status
    

def gameloop():
    global game_state
    global civ
    global turn_count
    civ = game_state['playerciv'][0]
    while True:                   
        
        currentCivState = getStatus()
        print(currentCivState)
        gamePrompt()
        

def main():
    global game_state

    if not os.path.isfile(SAVEFILE):
        game_state = createCiv()
        saveCiv()
        print("Hello, " + civ.leaderName + ", great leader of " + civ.nationName + ". Your people need you.")
    else:
        game_state = loadCiv()
        print("Hello, " + civ.leaderName + ", great leader of " + civ.nationName + ". Your people need you.")
    gameloop()
    sys.exit()
    
    
                   
if __name__ == '__main__':
    main()
