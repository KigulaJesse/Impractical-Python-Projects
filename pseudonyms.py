"""This file is used to generate random names for the Psych show."""
import sys
import random

print("Welcome to the Pysch 'Sidekick Name Picker.' \n")
print("A name Sean would pick for Gus \n")

first = ('Baby Oil' , "Bob 'Stinkbug'" , 'Butterbean' , 'Bad News' , 'Big Burps' , 'Bowel Noises',
        "Bill 'Beenie­Weenie'" , 'Boxelder' , "Bud 'Lite' " , 'Buttermilk' , 'Buttocks' , 'Chad' ,
        'Chesterfield' , 'Chewy' , 'Crapps' , 'Fancypants' , 'Chigger' , 'Dark Skies' , 
        "Cinnabuns" ,'Cleet' , 'Cornbread' , 'Crab Meat' , 'Dennis Clawhammer' , 'Dicman' , 
        'Figgs' , 'Foncy' , 'Gootsy' , 'Greasy Jim' , 'Elphonso' , 'Huckleberry' , 'Huggy' ,
        'Ignatious' , 'Jimbo' ,  "Joe 'Pottin Soil'" , 'Johnny' , 'Lemongrass' , 'Lil Debil' ,
        'Longbranch' , '"Lunch Money"' , 'Mergatroid' , '"Mr Peabody"' , 'Oil­Can'  , 'Oinks' ,
        'Old Scratch' ,  'Ovaltine' , 'Pennywhistle' ,  'Pitchfork Ben' ,  'Potato Bug' ,
        'Pushmeet' , 'Rock Candy' ,  'Schlomo'  , 'Scratchensniff'  , 'Scut' ,  "Sid 'The Squirts'",
        'Skidmark' , 'Slaps', 'Snakes' , 'Snoobs' , 'Snorki' , 'Soupcan Sam' , 'Spitzitout' ,
        'Squids' ,'Stinky' , 'Storyboard', 'Sweet Tea', 'TeeTee' , 'Wheezy Joe' ,
        "Winston 'Jazz Hands'" , 'Worms')

last = ('Appleyard','Breedslovetrout','Cocktoasten','Bigmeat','Bloominshine','Butterbaugh',
        'Clovenhoof','Endicott','Fewhairs','Boogerbottom','Clutterbuck','Goodpasture','Hootkins',
        'Guster','Henderson','Jefferson','Jenkins','Kingfish','Noseworthy','Oxhandler','Listenbee',
        "M'Bembo",'Gooberdapple','Hooperbag','Jingley­Schmidt','McFadden','Goodensmith',
        'Hoosenater','Johnson','Moonshine','Nettles','Olivetti','Pealike','Pinkerton','Porkins',
        'Rosenthal','Rubbins','Stevens','Stroganoff','Turnipseed','Weiners','Vinaigrette','Whipkey',
        'Woolysocks','Outerbridge','Pennywhistle','Overpeck','Peterson','Overturf',
        'Putney','Quakenbush','Pieplow','Rainwater','Sackrider','Snuggleshine','Splern',
        'Sugar­Gold','Swackhamer','Tippins','Walkingstick','Wallbanger','Weewax','Wigglesworth',
        'Wimplesnatch','Winterkorn')


while True:
    firstName = random.choice(first)
    lastName = random.choice(last)
    print(f'{firstName} {lastName}', file=sys.stderr)

    try_again = input("\nTry Again? (Press enter else n to quit)\n")
    if try_again.lower() == "n":
        break

input("\nPress enter to exit.")
