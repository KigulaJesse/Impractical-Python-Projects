"""This file is used to generate random names for the Psych show."""
import sys
import random

def main():
    """Choose two names from list and print out the combination"""
    print("Welcome to the Pysch 'Sidekick Name Picker.' \n")
    print("A name Sean would pick for Gus \n")

    first = ('Bob','Butterbean','Bad News','Big Burps',
            'Bill','Boxelder',"Bud",'Buttermilk','Buttocks','Chad',
            'Chesterfield','Chewy','Crapps','Fancypants','Chigger','Dark Skies',
            'Cinnabuns','Cleet','Cornbread','Crab Meat','Dicman',
            'Figgs','Foncy','Gootsy','Elphonso','Huckleberry','Huggy',
            'Ignatious','Jimbo','Joe','Johnny','Lemongrass','Lil Debil',
            'Longbranch','Lunch Money','Mergatroid','Mr Peabody','Oinks',
            'Ovaltine','Pennywhistle','Pitchfork Ben','Potato Bug',
            'Pushmeet','Schlomo','Scratchensniff','Scut',"Sid ",
            'Skidmark' , 'Slaps','Snakes','Snoobs','Snorki','Spitzitout',
            'Squids','Stinky','Storyboard','Sweet Tea','TeeTee','Winston',
            'Worms'
        )

    middle = ('Stinkbug','Beenie­Weenie','The Squirts','Jazz Hands','Pottin Soil','Lite',
            'Oil­ Can','Old Scratch','Soupcan Sam','Greasy Jim','Dennis Clawhammer',
            'Bowel Noises','Baby Oil','Wheezy Joe','Rock Candy','The Big News',
            'Grunts','Tinkie Winkie','Lala','Po',
        )

    last = ('Appleyard','Breedslovetrout','Cocktoasten','Bigmeat','Bloominshine','Butterbaugh',
            'Clovenhoof','Endicott','Fewhairs','Boogerbottom','Clutterbuck','Goodpasture',
            'Hootkins','Guster','Henderson','Jefferson','Jenkins','Kingfish','Noseworthy',
            'Oxhandler','Listenbee',"M'Bembo",'Gooberdapple','Hooperbag','Jingley­Schmidt',
            'McFadden','Goodensmith','Hoosenater','Johnson','Moonshine','Nettles','Olivetti',
            'Pealike','Pinkerton','Porkins','Rosenthal','Rubbins','Stevens','Stroganoff',
            'Turnipseed','Weiners','Vinaigrette','Whipkey','Woolysocks','Outerbridge',
            'Pennywhistle','Overpeck','Peterson','Overturf','Putney','Quakenbush','Pieplow',
            'Rainwater','Sackrider','Snuggleshine','Splern','Sugar­Gold','Swackhamer',
            'Tippins','Walkingstick','Wallbanger','Weewax','Wigglesworth','Wimplesnatch',
            'Winterkorn'
        )


    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)
        middle_name = None
        if random.random() < 0.33333:
            middle_name = random.choice(middle)
        if middle_name:
            print(f'{first_name} {middle_name} {last_name}', file=sys.stderr)
        else:
            print(f'{first_name} {last_name}', file=sys.stderr)
        try_again = input("\nTry Again? (Press enter else n to quit)\n")
        if try_again.lower() == "n":
            break

    input("\nPress enter to exit.")

if __name__ == "__main__":
    main()
