class Child:
    def __init__(self, parent=None):
        self.setParent(parent)

    def setParent(self, parent):
        self.parent = parent

    def parentTo(self, parent):
        self.parent.addChild(self)

    def orphan(self):
        self.parent.removeChild(self)


class Parent(Child):
    def __init__(self, childlist=[]):
        self.children = []
        self.addChildren(childlist)

    def addChildren(self, children, childlist=None):
        if not childlist: childlist = self.children
        childlist.extend(children)
        for child in children:
            child.setParent(self)

    def removeChildren(self, children, childlist=None):
        if not childlist: childlist = self.children
        for child in children:
            child.setParent(None)
            childlist.remove(child)

    def addChild(self, child): self.addChildren([child])
    def removeChild(self, child): self.removeChildren([child])


class GameObj(Parent):
    @staticmethod
    def addPositions(pos1, pos2):
        return (pos1[0]+pos2[0], pos2[1]+pos2[1])

    def __init__(self, name, position, cmpts=[]):
        super(GameObj, self).__init__()
        self.name = name
        self.local_position = position
        self.position = position
        self.components = []

        self.addComponents(cmpts)

    def getPosition(self):
        return self.position

    def setParent(self, parent):
        self.parent = parent
        if isinstance(parent, GameObj):
            self.position = GameObj.addPositions(self.local_position, parent.getPosition())
        else:
            self.position = self.local_position

    def broadcast(self, msg):
        for cmpt in self.components:
            cmpt.onNotify(msg)

    def update(self, t, dt):
        for cmpt in self.components:
            cmpt.update(t, dt)

        for child in self.children:
            self.update(t, dt)

    def addComponent(self, cmpt): self.addChild(cmpt, self.components)
    def addComponents(self, cmpts): self.addChildren(cmpts, self.components)


class Component(Child):
    def awake(self):
        pass

    def update(t, dt):
        pass

    def broadcast(self, msg):
        self.parent.broadcast(msg)

    def onNotify(self, msg):
        pass

if __name__ == "__main__":
    GameObj("G", (0, 0))
