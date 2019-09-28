#What parts of combat do we have???

#Most important pieces!
#Alexander vs enemy
#Code for Alexander: Hit Points, weapon, it does some amount of damage

#Code for the enemy: hit points, weapon, it does some amount of damage

#Code for fight: taking turns to attack, update numbers based on what happens

#Code for results: What happened? Is there another turn? Is the fight over? Has someone died?

profile = {'Name':'Alexander The Mediocre','Weapon':'spork','HP':20}
enemy = "ninja"

def combat(profile, enemy):
    #Alexander vs enemy
    #Code for Alexander: Hit Points, weapon, it does some amount of damage
    #profile = {'Name':'Alexander The Mediocre','Weapon':'spork','HP':20}
    AlexHP = profile['HP']
    print("Alex's HP is: " + str(AlexHP))
    AlexWep = profile['Weapon']
    sdmg = 1
    #Code for the enemy: hit points, weapon, it does some amount of damage
    enm = enemy
    enmHP = 38
    #no specific weapon, be vague
    enmdmg = 1
    #Code for fight: taking turns to attack, update numbers based on what happens
    while AlexHP > 0 and enmHP > 0:
        #Alex gets a turn
        enmHP = enmHP - sdmg
        print("Enemy's HP is: " + str(enmHP))
        #Enemy gets a turn
        AlexHP = AlexHP - enmdmg
        print("Alex's HP is: " + str(AlexHP))
    return print(enmHP)

    #Code for results: What happened? Is there anoher turn? Is the fight over? Has someone died?

combat(profile, enemy)

#People in the fight

#Alexander

#enemy


#Actions

#Alexander's gotta do something
#Alex has choices...fight? heal? run? observe? negotiate?

#enemy has choices...fight? run? taunt? monologue?

#weapons or something to do damage and how many points?

#swings are taken! by both parties

#Consequences

#How many hit points do we have? 

#Getting hurt by getting hit

#attack skills go down because you are weaker or tired

#dying

#alliances

#healing items and how much they heal?