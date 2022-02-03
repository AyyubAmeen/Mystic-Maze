spriteSize = 32

playerStats = {"maxHp" : 100,
               "hp" : 100,
               "maxMp" : 100,
               "mp" : 100,
               "mpRegen" : 0.5,
               "atk" : 1,
               "def" : 1,
               "spd" : 1}

straightSpell = {"type" : "straight",
              "dmg" : 1,
              "numShots" : 1,
              "limit" : 10,
              "spd" : 7.5,
              "size" : 5,
              "mpCost" : 10,
              "cooldown" : 300}

shotgunSpell = {"type" : "straight",
              "dmg" : 1,
              "numShots" : 5,
              "limit" : 10,
              "spd" : 7.5,
              "size" : 5,
              "mpCost" : 10,
              "cooldown" : 300}

opSpell = {"type" : "straight",
           "dmg" : 1000,
           "numShots" : 10,
           "limit" : 1000000,
           "spd" : 25,
           "size" : 15,
           "mpCost" : 0,
           "cooldown" : 1}

colour = {"white" : (255, 255, 255),
         "black" : (0, 0, 0),
         "grey" : (128, 128, 128),
         "brown" : (102, 51, 0),
         "light brown" : (153, 102, 0),
         "red" : (255, 0, 0),
         "green" : (0, 255, 0),
         "blue" : (0, 0, 255),
         "yellow" : (255, 255, 0),
         "cream" : (255, 204, 102),
         "gold" : (204, 153, 0),
         "orange" : (255, 102, 0),
         "purple" : (102, 0, 102)} 

baseMap = ["BBBBBBBFFBBBBBBB",
           "BFFFFFFFFFFFFFFB",
           "BFFFFFFFFFFFFFFB",
           "FFFFFFFFFFFFFFFF",  
           "FFFFFFFFFFFFFFFF",
           "FFFFFFFFFFFFFFFF",
           "BFFFFFFFFFFFFFFB",  
           "BFFFFFFFFFFFFFFB",
           "BBBBBBBFFBBBBBBB"]