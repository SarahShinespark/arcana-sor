#file="Arcana SOR v2.1 a9.smc"
#file="Arcana (u).smc"
#file="Arcana SOR v2.1 a9 - Cursed changes 2.smc"
file ="t.smc"
f = open(file,'rb')

weaponNames = []
armorNames = []
accessNames= []
ringNames  = []
weaponPrices = []
armorPrices = []
accessPrices = []
ringPrices = []
weaponFlags = []
armorFlags = []
accessFlags = []
ringFlags = []
weaponAtk = []
armorDef = []
accessDef = []
weaponRace = []
accessRace = []
weaponElement = []
armorElement = []
weaponCrit = []
accessMdef = []
weaponPenalty = []
weaponSpell = []
armorSpell = []
accessSpell = []
ringSpell = []

f.seek(185981)
# Get names
for x in range(40):
    testme = f.read(16).decode('ascii')
    f.read(1)
    weaponNames.append(testme)
for x in range(40):
    testme = f.read(16).decode('ascii')
    f.read(1)
    armorNames.append(testme)
for x in range(20):
    testme = f.read(16).decode('ascii')
    f.read(1)
    accessNames.append(testme)
for x in range(20):
    testme = f.read(16).decode('ascii')
    f.read(1)
    ringNames.append(testme)

f.seek(188038)
#Get prices
for x in range(40):
    testme = f.read(2)
    weaponPrices.append( int.from_bytes(testme, byteorder='little'))
for x in range(40):
    testme = f.read(2)
    armorPrices.append( int.from_bytes(testme, byteorder='little'))
for x in range(20):
    testme = f.read(2)
    accessPrices.append( int.from_bytes(testme, byteorder='little'))
for x in range(20):
    testme = f.read(2)
    ringPrices.append( int.from_bytes(testme, byteorder='little'))

f.seek(188280)
#Get equip flags
def getEquipFlags(x):
    flags = ""
    if(x[0] & 1 != 0): flags += "R"
    if(x[0] & 8 != 0): flags += "D"
    if(x[0] & 16!= 0): flags += "A"
    if(x[0] & 4 != 0): flags += "S"
    if(x[0] & 2 != 0): flags += "T"
    return flags
for x in range(40):
    testme = f.read(1)
    weaponFlags.append( getEquipFlags(testme))
for x in range(40):
    testme = f.read(1)
    armorFlags.append( getEquipFlags(testme))
for x in range(20):
    testme = f.read(1)
    accessFlags.append( getEquipFlags(testme))
for x in range(20):
    testme = f.read(1)
    ringFlags.append( getEquipFlags(testme))

f.seek(188401)
#Get power/defense
for x in range(40):
    testme = f.read(2)
    weaponAtk.append( int.from_bytes(testme, byteorder='little'))
for x in range(40):
    testme = f.read(2)
    armorDef.append( int.from_bytes(testme, byteorder='little'))
for x in range(20):
    testme = f.read(2)
    accessDef.append( int.from_bytes(testme, byteorder='little'))

f.seek(188643)
#Get race/element
def getRaceFlags(x):
    x = x[0]
    if x == 0: return "      "
    if x == 1: return "Zombie"
    if x == 2: return "Dragon"
    if x == 3: return "ZD"
    if x == 4: return "Medusa"
    if x == 5: return "ZM"
    if x == 6: return "DM"
    if x == 7: return "ZDM"
    if x == 8: return "Giant"
    if x == 9: return "ZG"
    if x ==10: return "DG"
    if x ==11: return "ZDG"
    if x ==12: return "MG"
    if x ==13: return "MG"
    if x ==14: return "DMG"
    if x ==15: return "ZDMG"
    return "Undef"
    return int.from_bytes(race, byteorder='little')
def getElementFlags(x):
    x = int.from_bytes(x, byteorder='little')>>4
    if x == 0: return "      "
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
    return "Undef"
for x in range(40):
    race = f.read(1)
    element = f.read(1)
    weaponRace.append(getRaceFlags(race))
    weaponElement.append( getElementFlags(element))
for x in range(40):
    f.read(1)
    element = f.read(1)
    armorElement.append( getElementFlags(element))
for x in range(20):
    race = f.read(1)
    f.read(1)
    accessRace.append(getRaceFlags(race))

f.seek(188885)    
#Get crit/mdef
for x in range(40):
    testme = f.read(1)
    crit = int.from_bytes(testme, byteorder='little')
    crit = crit * 100 / 256
    crit = "{:.2f}".format(crit) + "%"
    weaponCrit.append(crit)
for x in range(40):
    f.read(1)
for x in range(20):
    testme = f.read(1)
    accessMdef.append(int.from_bytes(testme, byteorder='little'))
    
f.seek(189006)
#Get Eq?2 "Penalty"
for x in range(40):
    testme = f.read(1)
    weaponPenalty.append(int.from_bytes(testme, byteorder='little'))

f.seek(189127)
#Get Spell cast
for x in range(40):
    testme = f.read(1)
    value = int.from_bytes(testme, byteorder='little')
    if( value < 1 | value > 81): weaponSpell.append("Undef")
    elif(value == 0): weaponSpell.append("")
    else:
        temp = f.tell()
        f.seek(189248 + value*22)
        weaponSpell.append(f.read(21).decode('ascii'))
        f.seek(temp)
for x in range(40):
    testme = f.read(1)
    value = int.from_bytes(testme, byteorder='little')
    if( value < 1 | value > 81): armorSpell.append("Undef")
    elif(value == 0): armorSpell.append("")
    else:
        temp = f.tell()
        f.seek(189248 + value*22)
        armorSpell.append(f.read(21).decode('ascii'))
        f.seek(temp)
for x in range(40):
    testme = f.read(1)
    value = int.from_bytes(testme, byteorder='little')
    if( value < 1 | value > 81): accessSpell.append("Undef")
    elif(value == 0): accessSpell.append("")
    else:
        temp = f.tell()
        f.seek(189248 + value*22)
        accessSpell.append(f.read(21).decode('ascii'))
        f.seek(temp)
#for x in range(40):
#    testme = f.read(1)
#    value = int.from_bytes(testme, byteorder='little')
#    if( value < 1 | value > 81): ringSpell.append("Undef")
#    elif(value == 0): ringSpell.append("")
#    else:
#        temp = f.tell()
#        f.seek(189270 + value*22)
#        ringSpell.append(f.read(21).decode('ascii'))
#        f.seek(temp)
    

#Print the crap
print ("Race: Z=Zombie, D=Dragon, M=Medusa, G=Giant")
print("Spells: [=Wind, \=Fire, ]=Water, ^=Earth")
print ("Name\t\t\tPrice\tEquip\tPWR\tRace\t  Element\tCrit\tPenalty\t  Spell")

for x in range(40):
    print (weaponNames[x], end= '')
    print ('\t', end = '')
    print (weaponPrices[x], end= '')
    print ('\t', end = '')
    print (weaponFlags[x], end= '')
    print ('\t', end = '')
    print (weaponAtk[x], end = '')
    print ('\t', end = '')
    print (weaponRace[x], end='')
    print ('\t  ', end = '')
    print (weaponElement[x], end = '')
    print ('\t', end = '')
    print (weaponCrit[x], end = '')
    print ('\t', end = '')
    print (weaponPenalty[x], end = '')
    print ('\t  ', end = '')
    print (weaponSpell[x])
print ("\nName\t\t\tPrice\tEquip\tDEF\tElement\t  Spell")
for x in range(40):
    print (armorNames[x], end= '')
    print ('\t', end = '')
    print (armorPrices[x], end= '')
    print ('\t', end = '')
    print (armorFlags[x], end= '')
    print ('\t', end = '')
    print (armorDef[x], end= '')
    print ('\t', end = '')
    print (armorElement[x], end= '')
    print ('\t', end = '')
    print (armorSpell[x])
print ("\nName\t\t\tPrice\tEquip\tDEF\tRace\tMdef\tSpell")
for x in range(20):
    print (accessNames[x], end= '')
    print ('\t', end = '')
    print (accessPrices[x], end= '')
    print ('\t', end = '')
    print (accessFlags[x], end= '')
    print ('\t', end = '')
    print (accessDef[x], end= '')
    print ('\t', end = '')
    print (accessRace[x], end = '')
    print ('\t', end = '')
    print (accessMdef[x], end = '')
    print ('\t', end = '')
    print (accessSpell[x])
print ("\nName\t\t\tPrice\tEquip")
for x in range(20):
    print (ringNames[x], end= '')
    print ('\t', end = '')
    print (ringPrices[x], end= '')
    print ('\t', end = '')
    print (ringFlags[x])

f.close()
