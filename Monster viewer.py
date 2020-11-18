#file="Arcana SOR v2.1 a9.smc"
file="Arcana (u).smc"
f = open(file,'rb')

monsterNames = []
monsterRace = []
monsterElement = []
monsterHP = []
monsterEXP = []
monsterGP = []
monsterSpell = []
monsterLV = []
monsterSTR = []
monsterINT = []
monsterEND = []
monsterALT = []

f.seek(172009)
# Get names
for x in range(80):
    testme = f.read(16).decode('ascii')
    f.read(1)
    monsterNames.append(testme)

f.seek(182573)
#Get race/element
def getRaceFlags(x):
    x = x[0]
    bossFlag = ""
    if x & 16:
        bossFlag = "Boss"
        x -= 16
    if x == 0: return bossFlag + ""
    if x == 1: return bossFlag + "Z"
    if x == 2: return bossFlag + "D"
    if x == 3: return bossFlag + "ZD"
    if x == 4: return bossFlag + "M"
    if x == 5: return bossFlag + "ZM"
    if x == 6: return bossFlag + "DM"
    if x == 7: return bossFlag + "ZDM"
    if x == 8: return bossFlag + "G"
    if x == 9: return bossFlag + "ZG"
    if x ==10: return bossFlag + "DG"
    if x ==11: return bossFlag + "ZDG"
    if x ==12: return bossFlag + "MG"
    if x ==13: return bossFlag + "MG"
    if x ==14: return bossFlag + "DMG"
    if x ==15: return bossFlag + "ZDMG"
    return "Undef"
def getElementFlags(x):
    x = int.from_bytes(x, byteorder='little')
    if x == 0: return "       "
    if x == 1: return "Wind   "
    if x == 2: return "Earth  "
    if x == 3: return "WiEa   "
    if x == 4: return "Water  "
    if x == 5: return "WiEa   "
    if x == 6: return "EaWa   "
    if x == 7: return "WiEaWa "
    if x == 8: return "Fire   "
    if x == 9: return "WiFi   "
    if x ==10: return "EaFi   "
    if x ==11: return "WiEaFi "
    if x ==12: return "WaFi   "
    if x ==13: return "WiWaFi "
    if x ==14: return "EaWaFi "
    if x ==15: return "WEWF   "
    return "Undef  "
for x in range(80):
    race = f.read(1)
    element = f.read(1)
    monsterRace.append(getRaceFlags(race))
    monsterElement.append( getElementFlags(element))

f.seek(183893)
#Get HP
for x in range(80):
    testme = f.read(2)
    monsterHP.append( int.from_bytes(testme, byteorder='little'))
    
f.seek(184053)
#Get EXP
for x in range(80):
    testme = f.read(2)
    monsterEXP.append( int.from_bytes(testme, byteorder='little'))
    
f.seek(184213)
#Get GP
for x in range(80):
    testme = f.read(2)
    monsterGP.append( int.from_bytes(testme, byteorder='little'))

f.seek(184885)
#Get Spell
for x in range(80):
    testme = f.read(1)
    value = int.from_bytes(testme, byteorder='little')
    if( value < 1 | value > 81): monsterSpell.append("Undef")
    elif(value == 0): monsterSpell.append("")
    else:
        #Read spell name
        temp = f.tell()
        f.seek(189248 + value*22)
        monsterSpell.append(f.read(21).decode('ascii'))
        f.seek(temp)

    
f.seek(184373)
#Get LV
for x in range(80):
    testme = f.read(2)
    monsterLV.append( int.from_bytes(testme, byteorder='little'))
    
f.seek(182733)
#Get STR
for x in range(80):
    testme = f.read(2)
    monsterSTR.append( int.from_bytes(testme, byteorder='little'))
    
f.seek(182933)
#Get INT
for x in range(80):
    testme = f.read(2)
    monsterINT.append( int.from_bytes(testme, byteorder='little'))
    
f.seek(183093)
#Get END
for x in range(80):
    testme = f.read(2)
    monsterEND.append( int.from_bytes(testme, byteorder='little'))
    
f.seek(183253)
#Get ALT
for x in range(80):
    testme = f.read(2)
    monsterALT.append( int.from_bytes(testme, byteorder='little'))
    


#Print the crap
print ("Race: B=Boss, Z=Zombie, D=Dragon, M=Medusa, G=Giant")
print("Spells: [=Wind, \=Fire, ]=Water, ^=Earth")
print ("Name\t\tRace\t  Element  HP\tEXP\tGP\tSpell\t\t\tLV\tSTR\tINT\tEND\tALT")

for x in range(80):
    print ('{0: <16}'.format(monsterNames[x]), end = "")
    print (' ', end = '')
    print ('{0: <7}'.format(monsterRace[x]), end = '')
    print ('  ', end = '')
    print (monsterElement[x], end = '')
    print ('  ', end = '')
    print (monsterHP[x], end = '')
    print ('\t', end = '')
    print (monsterEXP[x], end = '')
    print ('\t', end = '')
    print (monsterGP[x], end = '')
    print ('\t', end = '')
    print ('{0: <21}'.format(monsterSpell[x]), end = '')
    print ('\t', end = '')
    print (monsterLV[x], end = '')
    print ('\t', end = '')
    print (monsterSTR[x], end = '')
    print ('\t', end = '')
    print (monsterINT[x], end = '')
    print ('\t', end = '')
    print (monsterEND[x], end = '')
    print ('\t', end = '')
    print (monsterALT[x])

