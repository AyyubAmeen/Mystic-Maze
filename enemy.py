import pygame
import math
import os
import sys
from player import *
from item import *
from UI import *
from maps import *
from sprites import *
from constants import *

class enemy:
    def __init__(self, hp, atk, defe, spd, projLife, baseDmg, size):
        self.hp = hp
        self.currentHp = hp
        self.atk = atk
        self.defe = defe
        self.spd = spd
        self.projLife = projLife
        self.baseDmg = baseDmg
        self.numShots =  0
        self.size = size