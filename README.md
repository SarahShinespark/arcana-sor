# arcana-sor
Project page for Arcana - Seal of Rimsala, a Super Nintendo game mod.

### Python
- Contains extract-and-display tools to read specific data from the game ROM.

### Arcana SOR v2.1a12
- Contains the patch file and game readme bundled with the current release on [RHDN](http://www.romhacking.net).
- Transcription excerpt follows.


## Blurb
This is an improvement-type mod for Arcana (SNES), my first JRPG as a kid. Why? ...Because I can!

- Faster gameplay, redrawn maps, and a coherent story
- Singular level-up screen matching the Japanese version; no more scrolling!
- New status screen with icons
- Undoes 90's Nintendo censorship (Alchemist selling elixir -> Bartender selling beer)
- Introduces unused content: A novelty ring, flavor text in battle, character classes, new animation palettes, and the elusive Mimic!
- Easter eggs and bug fixes!
- Hundreds of tiny tweaks: equipment, items, maps, dialogue, monster stats, treasure chests, Level Select inventory.
 I really like to tweak things :D

## Troubleshooting
Be sure to use an un-headered rom when patching. Should be "Arcana (U).smc" with a CRC32 of C891B297.</br>
(Use SnesRomUtil to remove the header if needed).</br>
And... don't forget to EQUIP your weapons! /BoF2-style advice

## Known bugs
- Level select causes graphics bugs like the sky showing on the ground. This can be remedied by saving at the inn and resetting. May be a FastROM bug.
- During the 3 Treasures cutscene at the end, the graphics are glitched. This is a bug with the FastROM patch and probably graphics handling.
- Large formations introduce a lot of lag that doesn't go away unless you save and reset.
- Casting the Call spells/Call Amulet on Bishops (Ch5) makes the game hang. Sometimes. (Need more information to diagnose this)
- In Bizance Castle the room before Karl, a phantom wall flickers when walking at full speed on the north side of the room.
- The subtitle slightly cuts off the Arcana graphic. (The next row down is compressed, so it's just easier this way)
- The purple swirl used for indirect spells can look glitchy depending on emulator or target palette.

## Known vanilla bugs
- Some spell or item names are written with a trailing space, like when casting "Lightning 1 ." There's a patch in progress.
- During the Darwin cutscene in Ch2, his sprite cuts off some of the text.
- Axs is unequipped and level-averaged in the transition from Ch3 to Ch4. (Technically he does leave for the Sarah cutscene)
- Switching spirits with Call resets any custom spell ordering.
- The end music is very laggy.
- The end card animation has graphic tears.
- Stat boost items used when at max stats falsely say your stat was increased.
- Stat buff spells when already buffed falsely say your stat was buffed.
  - Same for stat debuff spells.
- The sprite for Goblin-type enemies has an odd green border.
- The final boss is missing part of a card background on the top.
- Yes the manual is cringe. It's there for posterity. (It would be awesome to make a new one, but that's a special skill.)

## Level Select
This is a feature of the original game. To skip later in the story, input the following on the title screen.</br>
Select Down Select Select, XY Select Select, LR Select Select, Left right up...</br>
CH2: A</br>
CH3: B</br>
CH4: X</br>
CH5: Y</br>

## Version history
2.1a12</br>
 Gameplay: Rebranded anti-Medusa flag as anti-Human, and anti-Dragon as anti-Reptile.</br>
  This will make bonuses more important when picking equipment!</br>
 Printme updated with the following data.</br>
 Enemies:</br>
 -All Medusa no longer have a race.</br>
 -Lizard-type enemies (including dragons) are now Reptile type.</br>
 -Human-type enemies are now Human type.</br>
 Equipment changes:</br>
 -Cursed Sword: Power 100->50, anti-Human, Crit increased to 80%</br>
 -Cursed Shield: Mdef 00->30, resists Giants</br>
 -Cursed Gauntlet: Mdef 00->25, resists Reptile, casts Change Attr to Wind</br>
 -Dragon Blade: renamed Chain Blade to fit description</br>
 -Medusa Axe: reverted to Demon Axe</br>
 -Mage Staff: casts Confuse</br>
 -Memory Wand: casts Defense Impair</br>
 -Mace: anti-Human, price 1000 -> 850</br>
 -Flail: anti-Human, power 90 -> 95</br>
 -Warhammer: anti-Human</br>
 -Chain Whip: now Gaia Whip, Earth elemental</br>
 -Blackthorne Whip: now Blitz Whip, Wind elemental</br>
 -Small Shield: Mdef 00->02 (Large Shield is +5)</br>
 -Spike Shield: now resists Human (it's a very angry spike)</br>
 -Dragon Mail: renamed Bizantine Armor (doesn't protect against dragons tmn)</br>
 -Dragon Shield: renamed Scaly Shield</br>
 -Mirror Shield: renamed Kite Shield</br>
 -Grand Armor: renamed Fanas' Armor</br>
 -Grand Shield: renamed Fanas' Shield</br>
 -Rune Gauntlet: resists Human/Reptile</br>
 -Spirit Gauntlet: resists Undead/Human/Reptile/Giant</br>
 -Lots of equipment descriptions updated.</br>
 Extras:</br>
 -Added a Monster list, Spell list, and Equipment list in PDF.</br>
 -Added vanilla versions of the lists for reference.</br>


## Credits!
#### Coding
rainponcho- (last active August 2017) Decreased encounter rate, Fastrom patch, Multi-levelup patch</br>
torha - (last active April 2020) Fastrom v1.0, Dungeon map editing, SOR title fix, Title Register Reset v1, Spell reader v1 and lots of encouragement</br>
sluffy- Fastrom fixes</br>
rookwield- Fastrom v0.6</br>
justin3009</br>
stratoform - Title Register Reset v2, hoarding code I missed and being awesome in asar</br>
abw- Assisted fixing my ASM status screen code</br>
Raeven0- Valuable input on a prevalent ASM function</br>

#### Being AMAZING
KingMike</br>
TheSiege</br>
Apocalypse612</br>

#### Graphics
RetGal (he/him)

#### Mechanics
zombero</br>
Reiska</br>
DragonSpirit</br>

#### Testing
PersianImm0rtal</br>
TheSiege</br>
Phaxuji</br>
Cureless</br>
Sherry Shriner</br>
Apocalypse612</br>

#### Inspiration
The RHDN community</br>
BGB and FF6 Brave New World</br>
My family and friends</br>
And... you! :V</br>
