playerStats = {
    "maxHp" : 100,
    "hp" : 100,
    "maxMp" : 100,
    "mp" : 100,
    "mpRegen" : 0.5,
    "atk" : 1,
    "def" : 1,
    "spd" : 1,
    "activeItems" : ["rFire Bolt", "rFire Spray", 0, 0, 0],
    "passiveItems" : []}

#Range Spells
rangeWeapons = [
    {
    "name" : "Fire Bolt",
    "type" : "straight",
    "dmg" : 15,
    "numShots" : 1,
    "lifetime" : 10,
    "spd" : 10,
    "size" : 25,
    "mpCost" : 5,
    "cooldown" : 0.2
    },

    {
    "name" : "Fire Spray",
    "type" : "shotgun",
    "dmg" : 10,
    "numShots" : 5,
    "lifetime" : 10,
    "spd" : 10,
    "size" : 25,
    "mpCost" : 20,
    "cooldown" : 0.5
    },

    {
    "name" : "Dragon's Breath",
    "type" : "straight",
    "dmg" : 1000,
    "numShots" : 10,
    "lifetime" : 1,
    "spd" : 25,
    "size" : 60,
    "mpCost" : 0.3,
    "cooldown" : 0
    }
]

meleeWeapons = [
    {
    "name" : "Fire Floor",
    "type" : "rectangle",
    "dmg" : 10,
    "lifetime" : 1,
    "distance" : 0,
    "size" : [100,100],
    "cooldown" : 1.5
    },

    {
    "name" : "Fire Pool",
    "type" : "circle",
    "dmg" : 2,
    "lifetime" : 5,
    "distance" : 0,
    "size" : 100,
    "cooldown" : 5
    }
]

colour = {
    "white" : (255, 255, 255),
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

baseMap = [
    ["B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B"],
    ["B","F","F","F","F","F","F","F","F","F","F","F","F","F","F","B"],
    ["B","F","F","F","F","F","F","F","F","F","F","F","F","F","F","B"],
    ["B","F","F","F","F","F","F","F","F","F","F","F","F","F","F","B"],
    ["B","F","F","F","F","F","F","F","F","F","F","F","F","F","F","B"],
    ["B","F","F","F","F","F","F","F","F","F","F","F","F","F","F","B"],
    ["B","F","F","F","F","F","F","F","F","F","F","F","F","F","F","B"],  
    ["B","F","F","F","F","F","F","F","F","F","F","F","F","F","F","B"],
    ["B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B"],
    ]