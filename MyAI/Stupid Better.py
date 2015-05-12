# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from constants import HIT, MISS, OPEN_WATER


class AIPlayer(object):
    def __init__(self):
        ROWS = 9
        COLS = 10
        self.all_coords = []
        for r in xrange(ROWS):
            for c in xrange(COLS):
                letter = chr(ord('A') + r)
                number = c + 1
                self.all_coords.append('%s%d' % (letter, number))

    def config_fleet(self, fleet):
        coords = []
        for x in xrange(fleet['Carrier'].length):
            coords.append('A%d' % (x + 1,))
        fleet['Carrier'].coords = coords
        fleet['Battleship'].coords = ['B1', 'B2', 'B3', 'B4']
        fleet['Submarine'].coords = ['C1', 'C2', 'C3']
        fleet['Destroyer'].coords = ['D1', 'D2', 'D3']
        fleet['PatrolBoat'].coords = ['F1', 'F2']
        return fleet

    def get_coords_for_shot(self, api):
        """
        api.is_enemy_boat_sunk(boat_name)
        api.get_current_contents(coord_pair)
        api.get_enemy_contents(coord_pair)
        """

        for coord in self.all_coords:
            if api.get_enemy_contents(coord) == OPEN_WATER:
                return coord
