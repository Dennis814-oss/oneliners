import random

banner = r"""
 _     _              _   _               _ 
| |   (_)            | | | |             | |
| |    _ _ __   ___  | |_| | __ _ _ __ __| |
| |   | | '_ \ / _ \ |  _  |/ _` | '__/ _` |
| |___| | | | |  __/ | | | | (_| | | | (_| |
\_____/_|_| |_|\___| \_| |_/\__,_|_|  \__,_|
"""

print(banner)
print("My favourite oneliners :)")
print("Press any key to continue....")
input()

oneliners = [
    "I'll be back.",  # The Terminator (1984)
    "Yippee-ki-yay, mother****er!",  # Die Hard (1988)
    "Hasta la vista, baby.",  # Terminator 2: Judgment Day (1991)
    "Get to the chopper!",  # Predator (1987)
    "Say hello to my little friend!",  # Scarface (1983)
    "Go ahead, make my day.",  # Sudden Impact (1983)
    "I live my life a quarter mile at a time.",  # The Fast and the Furious (2001)
    "Why so serious?",  # The Dark Knight (2008)
    "You can't handle the truth!",  # A Few Good Men (1992)
    "Welcome to the party, pal!",  # Die Hard (1988)
    "I am the law!",  # Judge Dredd (1995)
    "This is Sparta!",  # 300 (2006)
    "Consider that a divorce.",  # Total Recall (1990)
    "You're a disease, and I'm the cure.",  # Cobra (1986)
    "I have come here to chew bubblegum and kick ass, and I'm all out of bubblegum.",  # They Live (1988)
    "You know my name.",  # Casino Royale (2006)
    "Let off some steam, Bennett.",  # Commando (1985)
    "It's not a tumor!",  # Kindergarten Cop (1990)
    "Prepare to be terminated.",  # Terminator 3: Rise of the Machines (2003)
    "Looks like I picked the wrong week to quit sniffing glue.",  # Airplane! (1980)
    "Welcome to Earth!",  # Independence Day (1996)
    "I'm too old for this s***.",  # Lethal Weapon (1987)
    "Remember, Sully, when I promised to kill you last? I lied.",  # Commando (1985)
    "Hail to the king, baby.",  # Army of Darkness (1992)
    "You’re terminated.",  # The Terminator (1984)
    "Say... what again!",  # Pulp Fiction (1994)
    "I’m Batman.",  # Batman (1989)
    "Sweep the leg.",  # The Karate Kid (1984)
    "Frankly, my dear, I don't give a damn.",  # Gone with the Wind (1939)
    "Game over, man! Game over!",  # Aliens (1986)
    "You're gonna need a bigger boat.",  # Jaws (1975)
    "Keep the change, ya filthy animal.",  # Home Alone (1990)
    "Do you feel lucky? Well, do ya, punk?",  # Dirty Harry (1971)
    "I know what you're thinking. Did he fire six shots or only five?",  # Dirty Harry (1971)
    "If it bleeds, we can kill it.",  # Predator (1987)
    "I’ll have what she’s having.",  # When Harry Met Sally (1989)
    "There's no place like home.",  # The Wizard of Oz (1939)
    "What we've got here is failure to communicate.",  # Cool Hand Luke (1967)
    "Bond. James Bond.",  # Dr. No (1962)
    "Leave the gun. Take the cannoli.",  # The Godfather (1972)
    "Say my name.",  # Breaking Bad (2013, TV series, but iconic!)
    "To infinity and beyond!",  # Toy Story (1995)
    "You’re tearing me apart, Lisa!",  # The Room (2003)
    "Im inevitable,ironman"# end game(2019)
    "Avengers! Assemble", # Avengers: Endgame (2019)
]
print(random.choice(oneliners))
