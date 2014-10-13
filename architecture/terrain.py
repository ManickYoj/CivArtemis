from gameobj import GameObj
from assetloader import AssetLoader
from components import RenderableCmpt
from config import Config


class Tile(GameObj):
    def __init__(self, location, biome_type):
        self.biome_type = biome_type
        name = ''.join([str(biome_type), " Tile @ " + str(location)])
        r = RenderableCmpt(AssetLoader.getImage(biome_type))
        super(Tile, self).__init__(name, location, [r])


def generateTerrain(size):
        """ Generates a new terrain """
        # TODO: Come up with an algorithm for tile generation
        # TODO: Figure out the axial ranges needed to generate a
        #       rectangular world (its not (0-size, 0-size))
        return [[Tile((i, j), "Ocean") for i in xrange(size[0])] for j in xrange(size[1])]


class Terrain:
    _t = generateTerrain(Config.get('game settings', 'world_size'))

    @staticmethod
    def getTile(location):
        return Terrain._t[location[0], location[1]]
