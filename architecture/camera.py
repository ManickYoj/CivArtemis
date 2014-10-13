from gameobj import GameObj
from terrain import Terrain
from collections import deque
import pygame


class Camera(GameObj):
    _active = None
    _graphics = pygame.display.set_mode((0, 0), Config.get(display_mode))
    _render_list = deque()

    @staticmethod
    def addToRenderQueue(items):
        Camera._render_list.extendleft(items)

    @staticmethod
    def renderFrame():
        if Camera._active.moved:
            Camera._render_list.clear()
            Terrain.getRenderablesInFrame(Camera._active.getViewport())
            Camera._render_list.extend()

    @staticmethod
    def getActive():
        return Camera._active

    def __init__(self, player, name=None, pos=(0, 0)):
        self.moved = False

        # Set active camera
        if not Camera._active:
            Camera._active = self
            name = "Main Camera"

        super(Camera, self).__init__(name, pos, [KeyInputController(player)])

    def setActive(self):
        Camera._active = self

    def onNotify(self, msg):
        if msg.comp == "Controller" and msg.event == "Moved":
            self.moved = True
