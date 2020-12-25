file="Arcana SOR v2.1 a13.smc"
#file ="Arcana (u).smc"
f = open(file,'rb')

nameList = []
accuracyList = []
powerList = []
elementList = []
MPcostList = []
PaletteList = []
SFXList = []

f.seek(189270)
#Get names
for x in range(81):
    testme = f.read(21).decode('ascii')
    f.read(1)
    nameList.append(testme)

f.seek(191217)
#Get accuracy
for x in range(81):
    testme = f.read(1)
    acc = int.from_bytes(testme, byteorder='little')
    acc = acc * 100 / 256
    acc = "{:.2f}".format(acc) + "%"
    accuracyList.append(acc)

f.seek(191309)
#Get power (POWAHR!)
for x in range(81):
    testme = f.read(2)
    #Display hex for the hardcoded spells
    if((x >= 39 and x <= 74) and int.from_bytes(testme, byteorder='little') != 0): powerList.append(hex(int.from_bytes(testme, byteorder='little')))
    else: powerList.append( int.from_bytes(testme, byteorder='little'))


f.seek(191491)
#Get element
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
for x in range(81):
    f.read(1)
    element = f.read(1)
    elementList.append( getElementFlags(element))

f.seek(191654)
#Get MP cost
for x in range(81):
    testme = f.read(1)
    MPcostList.append( int.from_bytes(testme, byteorder='little'))

f.seek(191736)
#Get palette
for x in range(81):
    testme = f.read(1)
    PaletteList.append( int.from_bytes(testme, byteorder='little'))

f.seek(191831)
#Get SFX
for x in range(81):
    testme = f.read(1)
    SFXList.append( int.from_bytes(testme, byteorder='little'))

    
#Print the crap
print ("Race: Z=Zombie, D=Dragon, M=Medusa, G=Giant")
print("Spells: [=Wind, \=Fire, ]=Water, ^=Earth")
print("Name\t\t\tAcc\tPower\tElement\tMP\tPalette\tSFX")

for x in range(81):
    print (nameList[x], end='')
    print('\t', end='')
    print (accuracyList[x], end='')
    print('\t', end='')
    print (powerList[x], end='')
    print('\t', end='')
    print (elementList[x], end='')
    print('\t', end='')
    print (MPcostList[x], end='')
    print('\t', end='')
    print(PaletteList[x], end='')
    print('\t', end='')
    print(SFXList[x])
