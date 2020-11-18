Arcana Seal of Rimsala v2.1 alpha 12
Thank you for playing! OTL  ~Sarah Shinespark


Blurb
-----
This is an improvement-type mod for Arcana (SNES), my first JRPG as a kid. Why? ...Because I can!

-Faster gameplay, redrawn maps, and a coherent story
-Singular level-up screen matching the Japanese version; no more scrolling!
-New status screen with icons
-Undoes 90's Nintendo censorship (Alchemist selling elixir -> Bartender selling beer)
-Introduces unused content: A novelty ring, flavor text in battle, character classes, new animation palettes, and the elusive Mimic!
-Easter eggs and bug fixes!
-Hundreds of tiny tweaks: equipment, items, maps, dialogue, monster stats, treasure chests, Level Select inventory.
 I really like to tweak things :D


Patches
-------
FastROM v1.1b:
 Speeds up gameplay, reduces lag by telling the game to read from faster banks.
Multi-Levelup v1.1:
 Lets EXP roll over when gaining a level.
Dungeon map v1.0:
 Expands the ROM to 2MB and stores the raw dungeon maps in ROM uncompressed for editability and faster access.
SOR title fix v1.0:
 Fixes a display error where the title text used the wrong color.
SOR credit:
 Adds the author to the credit sequence (thank you RetGal!)
Title register reset v2:
 Fixes dirty graphics after failing the final battle and returning to the title screen.


Troubleshooting
---------------
Be sure to use an un-headered rom when patching. Should be "Arcana (U).smc" with a CRC32 of C891B297. (Use SnesRomUtil to remove the header if needed)
And... don't forget to EQUIP your weapons! /BoF2-style advice


Known vanilla bugs present
--------------------------
Some spell or item names are written with a trailing space, like when casting "Lightning 1 ." There's a patch in progress.
During the Darwin cutscene in Ch2, his sprite cuts off some of the text.
Axs is unequipped and level-averaged in the transition from Ch3 to Ch4. (Technically he does leave for the Sarah cutscene)
Switching spirits with Call resets any custom spell ordering.
The end music is very laggy.
The end card animation has graphic tears.
Stat boost items used when at max stats falsely say your stat was increased.
Stat buff spells when already buffed falsely say your stat was buffed.
-Same for stat debuff spells.
The sprite for Goblin-type enemies has an odd green border.
The final boss is missing part of a card background on the top.
Yes the manual is cringe. It's there for posterity. (It would be awesome to make a new one, but that's a special skill.)


Known SOR bugs
--------------
Level select causes graphics bugs like the sky showing on the ground. This can be remedied by saving at the inn and resetting. May be a FastROM bug.
During the 3 Treasures cutscene at the end, the graphics are glitched. This is a bug with the FastROM patch and probably graphics handling.
Large formations introduce a lot of lag that doesn't go away unless you save and reset.
Casting the Call spells/Call Amulet on Bishops (Ch5) makes the game hang. Sometimes. (Need more information to diagnose this)
In Bizance Castle the room before Karl, a phantom wall flickers when walking at full speed on the north side of the room.
The subtitle slightly cuts off the Arcana graphic. (The next row down is compressed, so it's just easier this way)
The purple swirl used for indirect spells can look glitchy depending on emulator or target palette.


Level Select
------------
This is a feature of the original game. To skip later in the story, input the following on the title screen.
Select Down Select Select, XY Select Select, LR Select Select, Left right up...
CH2: A
CH3: B
CH4: X
CH5: Y
(The extra Select input at the start lets the code work even with a save file, where otherwise you'll pick Continue.)


Credits!
--------
Coding
------
rainponcho- (last active August 2017) Decreased encounter rate, Fastrom patch, Multi-levelup patch
torha - (last active April 2020) Fastrom v1.0, Dungeon map editing, SOR title fix, Title Register Reset v1, Spell reader v1 and lots of encouragement
sluffy- Fastrom fixes
rookwield- Fastrom v0.6
justin3009
stratoform - Title Register Reset v2, hoarding code I missed and being awesome in asar
abw- Assisted fixing my ASM status screen code
Raeven0- Valuable input on a prevalent ASM function

Being AMAZING
-------------
KingMike
TheSiege
Apocalypse612

Graphics
--------
RetGal (he/him)

Mechanics
---------
zombero
Reiska
DragonSpirit

Testing
-------
PersianImm0rtal
TheSiege
Phaxuji
Cureless
Sherry Shriner
Apocalypse612

Inspiration
-----------
The RHDN community
BGB and FF6 Brave New World
My family and friends
And... you! :V


To do
=====
LDA [$10]  [$97:8F84]	38 -> 39 (Two Princesses theme for chapter intermissions)
40400: Add version number (Window Color text)


Version history
---------------
2.1a12
 Gameplay: Rebranded anti-Medusa flag as anti-Human, and anti-Dragon as anti-Reptile.
  This will make bonuses more important when picking equipment!
 Printme updated with the following data.
 Enemies:
 -All Medusa no longer have a race.
 -Lizard-type enemies (including dragons) are now Reptile type.
 -Human-type enemies are now Human type.
 Equipment changes:
 -Cursed Sword: Power 100->50, anti-Human, Crit increased to 80%
 -Cursed Shield: Mdef 00->30, resists Giants
 -Cursed Gauntlet: Mdef 00->25, resists Reptile, casts Change Attr to Wind
 -Dragon Blade: renamed Chain Blade to fit description
 -Medusa Axe: reverted to Demon Axe
 -Mage Staff: casts Confuse
 -Memory Wand: casts Defense Impair
 -Mace: anti-Human, price 1000 -> 850
 -Flail: anti-Human, power 90 -> 95
 -Warhammer: anti-Human
 -Chain Whip: now Gaia Whip, Earth elemental
 -Blackthorne Whip: now Blitz Whip, Wind elemental
 -Small Shield: Mdef 00->02 (Large Shield is +5)
 -Spike Shield: now resists Human (it's a very angry spike)
 -Dragon Mail: renamed Bizantine Armor (doesn't protect against dragons tmn)
 -Dragon Shield: renamed Scaly Shield
 -Mirror Shield: renamed Kite Shield
 -Grand Armor: renamed Fanas' Armor
 -Grand Shield: renamed Fanas' Shield
 -Rune Gauntlet: resists Human/Reptile
 -Spirit Gauntlet: resists Undead/Human/Reptile/Giant
 -Lots of equipment descriptions updated.
 Extras:
 -Added a Monster list, Spell list, and Equipment list in PDF.
 -Added vanilla versions of the lists for reference.


2.1a9
 Coding: Elemental equipment can now be viewed in the Status screen!
    As you may know, the four elements are Wind, Fire, Water and Earth.
 Graphics: New elemental icons!
 Script: Spell text rewritten for more flavor.
 Script: Attribute spells now show their element.
 Balance: Reverted barehanded damage to vanilla.

2.1a5
 New ASM: Introducing race bonuses!
 The four races are Undead, Dragons, Medusa and Giants.
 Weapons can increase damage, and armor can decrease damage i.e. anti-undead.
 Fitting that Axs' final equipment is anti-Medusa when he was turned to stone.

 Bugfix: Corrected a display error with Rooks' LV in the status screen
 Bugfix: The Equipment menu in battle no longer pulls up the outdated menu
 Correction: Several armors had inaccurate descriptions
 Correction: Mithril Gauntlet is anti-undead and not Magic Gauntlet, so it
  is the new Holy Gauntlet.
 Correction: Moon Gauntlet is anti giant and not Cursed Gauntlet. Updated description.


2.1a2
 Introducing stat icons!
 Sword = Attack power
 Shield = Defense power
 Sparkly shield = Magic defense
 x2 = Critical hit rate
 % = percentage! (This wasn't a visible character until now!)

 Please note that rings do not affect critical hit rate.

-New ASM hack: Overhauled the status and equipment menus.
 Rearranged the menu for more space and information.
 Displayed Spirit's level (they share Rooks')
-Bugfix: Spirits now have significantly more defense by level.
  This was supposed to scale, but thanks to one byte it didn't.
-Bugfix: Unequipped characters now properly have 0% crit/0 mdef, instead of 20% and 52 mdef
  (This made shields detrimental for most of the game)

2.0g
-Modified the Enchanted Jewel to be grayed out as an item. (It was 'always useable' but dummied to do nothing anyway)

2.0f
-Fixed a 3-digit display error present in all versions' level up screen; when gaining 100+ HP at Lv60, no longer tries displaying 2 digits.
  Was about to give up on this one and fixed it by chance by changing a 1 to a 0. Still don't understand why, but THAT'S CODING!!
-Balnea 1F: Removed a Lizardman encounter that was showing glitched graphics
-Balnea 2F: Fixed the facing direction on the Silver Flask chest
-Jinmenju renamed Man Face
-Doubled boss EXP
-Jotun/Minotaur EXP +256

2.0e
(Base mod + fastrom v1.1 + levelup v0.4 + all the other patches)
General changes:
-ROM expanded to store the maps uncompressed; it speeds up the dungeons and it's easier to make map edits.
  Maps now minimize backtracking and should be more fun to explore. *cough*crimsonvalley*cough*
-Added a new armor in Chapter 3, the Merfolk Mail. Now everyone can take damage as a Water elemental.
-Added a vanity item in Chapter 2, so you can fill in the 4th equipment slot for s&g.
-Overhauled the level select inventories for balance (and possibly... easter eggs)
-Removed all formations with 6+ enemies, for lag reduction
-Several enemies with weak MT spells were given stronger ST spells to reduce waiting in mob battles

Dialogue edits:
-The Priest in Ch1 is no longer called High Priest
-Remorse Tower is no longer called Stavery
-Rooks' "Card" ability is now called "Arcana". Because that's his power.
-Changed some equipment descriptions (the reward for clearing out Ch4 is entertaining)
-Touched up the script

Area and treasure changes:
-The maps in Ch1-3 were redrawn.
-Balnea 1F: Added 1/16 Lizardman, 1/16 Chimera 
-Balnea 1F: Sleeping Bag moved
-Balnea 2F: Reduced an 8 enemy encounter to 5 to reduce lag
-Balnea 2F: Silver Flask moved
-Dwarven Pass: Added 1/16 Flytrap, 1/16 Wolfsbane 
-Dwarven Pass: Reduced a 6 enemy encounter to 5 to reduce lag
-Crimson Valley: Reduced a 6 enemy encounter to 5 to reduce lag
-Crimson Valley: Assassin -> Ogre (left half of the map)
-Crimson Valley: Added 1/16 Flytrap, 1/16 Wolfsbane 
-Forest of Doubt: Added 2/16 Thief, 2/16 Assassin
-Forest of Doubt: Fixed a silly-looking encounter with 3 enemies stacked vertically
-Forest of Doubt: Water Card moved -> Ring Mail
-Ch3 - Ch5: Reduced a 7 enemy encounter to 5 to reduce lag (not listing all 13 by area)
-Ch3 - Ch5: -This made a duplicate encounter, so one was given 2 of a different enemy. (13 instances again)
-Ice Maze: Added 3333 GP and the 3 Cursed equipment for funsies. (Probably not cursed) (btw Cursed Gauntlet uniquely resists Giant)
-Icicle Dungeon: Buffed 2 treasures before the boss. Might be worth checking out.
-Icicle Dungeon: Fixed a vanilla bug preventing 2 treasures from appearing (HP Honey and MP Honey iirc)
-Polar Labyrinth: Buffed the six "angel wing" treasures
-Polar Labyrinth: Moved 2 of the vault treasures to dead ends
-Polar Labyrinth: One dead end has a Morning Star for Axs (btw Morning Star is anti-Giant)
-Polar Labyrinth: Introducing SOR's mascot, the Mimic! :W They will appear in certain areas.
-Remorse 1F/2F (Ch4): Knight 11/16 -> 4/16 (replaced Ghoul)
-Remorse 1F/2F (Ch4): Added Mimic 11/16 (replaced Knight)
-Remorse 1F/2F (Ch4): Added Mage 7/16 (replaced Warlock)
-Remorse 10F (Ch4): Return Ring -> Intelligence Honey
-Remorse 11F (Ch4): Tent after Teefa fight (formerly 7F 500 GP)
-Remorse 2F (Ch5): Tent -> Intelligence Honey

Enemy changes:
-Mandrake reverted to Alraune. There's some... pretty good monster girl art if you google that. >//>
-Galneon 2 renamed *giggle* Zombeon
-Rimsala 2 renamed Empress Rimsala
-Mage: Flame 1 -> Evasion Impair (0A -> 32)
-Warlock: Smash 1 -> Defense Impair (04 -> 34)
-Sorcerer: Flame 2 -> Attribute 4 (0B -> 10)
-Wraith: Attribute 1 -> Attribute 5 (0D -> 11)
-Teefa: Sleep All -> Paralyze (2B -> 2D) 
-Teefa: HP 400 -> 250
-Galneon 1: Confuse All (2C) (come on, it's his thing!)
-Galneon 1: HP 600 -> 400

Weapon shop changes:
Ch2: Adventurer Ring in place of Scale Mail
Ch3-5: Replaced Herbs with Moon Oil (it and Tent heals paralyze)
Ch5: Kaiser Shield price 45k -> 30k
Ch5: Dragon Shield price 2.5k -> 5k (are you kidding me?)
Some equipment description changes (reward for clearing out Ch4)
Some weapon renames:
 Thunderbolt -> Stormbrand
 Stone Mail -> Gaia Gear
 Scale Mail -> Merfolk Mail (get it? fish scales? its defense got buffed too)
 Shiny Sword -> Glittering Sword
 Shiny Armor -> Glittering Armor
 Secret Ring -> Adventurer Ring

Item shop changes:
-Ch3-5 now sells Moon Oil (heals paralysis)
-Updated the descriptions for Moon Oil and Tent
-Shops now have a theme; in Dwarven Town Sleeping Bags and HP/Str Honey are cheaper
 In Elf Village MP recovery and MP/Int/Agi Honey are cheaper

Bug fixes:
-SOR title fix: The “of” in Seal of Rimsala now correctly changes colors when selecting Continue.
-Changed a tile on the subtitle so it covers "Arcana" evenly
-Title register reset: Properly resets RAM after losing the final battle, avoids some graphical bugs on the title screen.

Misc:
Fixed status text for Petrify, Paralyze, Confuse. Went with STONE, PARA, and MAD as there was no C nor U for CONFU
 (Petrify is still inaccessible to monsters)



1.0d
(Changes to 1.0c)
Switched HAL theme to "Crystal Sword" to give the intro text cool music.
Added several more fastrom fixes, should slightly help lag.
Modified unarmed power to use Rooks’ current MP.
Moved the Mage Staff to Balnea 2F, replaced Herbs. Former location switched to 500 GP.
Allowed HP Restore/All out of battle.
(Be my guest if you want to full heal off a treasure chest!)
Flee MP cost reduced 32 -> 10

Rebalanced spell accuracy:
Elementals are now the same where Smash had a clear advantage.
Lightning 1,2,3: 80%/80%/80% -> 80%/90%/98%
Flame 1,2,3:     80%/80%/80% -> 80%/90%/98%
Water 1,2,3:     80%/80%/80% -> 80%/90%/98%
Smash 1,2,3:     98%/98%/98% -> 80%/90%/98%
Attribute 2: 98% -> 97%
Attribute 3: 98% -> 97%
Attribute 5: 85% -> 98%
Attribute 6: 98% -> 94%
Attribute 7: 98% -> 91%
Attribute 9: 98% -> 94%
Paralyze All: 35% -> 43%
Sleep All:    35% -> 47%
Confuse All:  35% -> 50%

Renamed Mantecore -> Manticore
Renamed Stop/All to Silence/All. (They're still dummied but the name matches now)
Attribute spell animations now match their power (greater than lv2: lv2 animation)
Swapped names of Attribute 7 and 9. Former is actually stronger and lower MP.

1.0c
(Base mod + levelup v0.3 + fastrom v0.6)
Fixed the FastROM patch, for real this time!!
Works on actual hardware!

1.0b
(Base mod + levelup v0.3 + fastrom v0.5fix)
Buffed the Bartender's food/drink healing
Buffed the Honey items
Reinoll -> Reynold
Ariel -> Alan (fite me)
Ending dialogue edits

0.99
(Base mod + levelup v0.3 + fastrom v0.5)
New Fastrom fix added; graphics issues fixed on many emulators now.
Item buffs:
Medicine 200->250 HP
Silver Flask 15->20 MP
Gold Flask 40->50 MP

0.98
(Base mod + levelup v0.3 + fastrom v0.4s)
Text changes
Gave Galneon 2 the "undead" property and Hydra the "dragon" property.
Changed Salah to Sarah.

0.97s
(Base mod + levelup v0.3 + fastrom v0.4s)
Fixed a lag issue with FastROM v0.4 thanks to sluffy. Hence the s.
Corrected some text formatting in Ch 5.
Darah +50 HP, spell changed to Lightning 2
Barah -50 HP

0.97 lv3
(Base mod + levelup v0.3)
Dialogue edits for Ch 4 and 5.

0.96 fr4 lv3
(Base mod + levelup v0.3 + fastrom v0.4)
Fixed patch conflict in fastrom v0.3 with levelup v0.3.
Fixed Heal animation crash from invalid animation values (23 and E0).

0.951
(Base mod + levelup v0.3 + fastrom v0.3)
First beta!
Finished Ch 2+3 script and started Ch 4.
Changed SFX during Darwin's Ch 2 event to match the spell actually cast.
Spirit Staff power 160 -> 192, casts Lightning 3 as an item
Assassin changed to Water elemental (he's already blue and casts Water 1)
Several minor name edits
Swapped Attribute 3 and 6's positions on Salah's spell list
BUG: Game crashes when casting a Heal spell in no$sns.

0.95
(Base mod 0.942 + levelup v0.3 + fastrom v0.3)
Fixed fastrom v0.2 by reverting 8 bytes that were causing gfx junk.

0.942 -fastrom
(Base mod + levelup v0.3)
Changed SFX of support spells to "Lufia Buff".
Chimera: Lightning 1 -> Attribute 1
Manticore: Lightning 2 -> Attribute 2

0.941 -fastrom
(Base mod + levelup v0.3)
Added a Broad Sword to the inventory (Ch 2 stage select) to give Darwin something to swing.

0.94 lv3
(Base mod 0.93r1 + levelup v0.3 + fastrom v0.2)
Fixed a RAM initialization bug in levelup v0.2 causing a softlock.
Changed the encounter rate to 1/20.
BUG: fastrom v0.2 is causing graphics glitches in the field (Ch 2)

0.93r1
(Base mod)
Adjusted some EXP and GP values.
Lowered the encounter rate (1/12 -> 1/24).
Changed FINIS status to DEATH. I think it's kinda funny.

0.92
Found the RAM values for the current song and sfx.
Changed the HAL logo music to the unused "Grass Flute", and the saving theme to Rimsala's laugh sfx. BECAUSE I CAN!!!
Rewrote the pre-title intro text and added a dramatic pause and some tabs for readability.
Adjusted the pauses in the intro to better fit the music.
Cleaned up the Inventory text to say "Cards" and "Items" and used a tab so the arrow would still be in the right position.

0.9
Japanese level-up screen implemented! ^____^
The text has been condensed to a single screen and properly formatted. Also, the spell learning text is faster now (the period appears instantly).
This has been a year in the making because of really dumb code. Originally you have 7 messages to click through for a level up, so they made a loop to wait for a button press exactly 7 times. Changing the code to only need 1 button press made the game softlock since it was still waiting, so... I had to find a BYTE (0x090CE) that was literally set to 7 and decremented each time. I changed it to 1 and it worked >.>

0.85
Recolored the title screen and added the subtitle!
Improved the cards you get on Stage Select.

0.8
Blackthorne Whip power 60 -> 108.
Wish Wand price 10000 -> 6500.
Fog Card price 100 -> 30.
Water at the bar is now free (down from 1 GP lol).
Changed an out-of-the-way Balnea Temple chest to a Mage Staff.
Reduced item inventory limit 48 -> 24. Mwa ha ha...

0.7
Found the character names in VRAM. I changed the sprite pointer in Efrite's name to say Ifrite. Unfortunately the trailing "t" shares pixels in neighboring "e" and "i", so removing the "e" to say Ifrit would produce a lopsided "t".

Earlier
Rewrote the intro text. I added a pause that wasn't there too, and I wrote the section in a flavor I'm particularly proud of. Yay, the mod feels a lot more personal now ^_^
Edited many animations. Mid-level Attribute spells now have solid colored balls. (This is the bird attack from Call Amulets)
Transferred #70 Baal's Demon race to #71 Medusa. All the other Demons have Medusa sprites, so this fixes a consistency issue. Changed "Demon Axe" to "Medusa Axe".





...Did you really read this far? Have one internet cookie (^-^)-0
Don't miss Kirby in the opening sequence!