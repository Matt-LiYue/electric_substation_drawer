import collections
VerticalBusPair = {}
HorizontalBusPair = {}
AllTrans = {}
adjDict = {}
BusCNID = set()
BusDict = {}
nodeSize = {"daozha": (48, 58), "daozhakai": (48, 58), "kaiguan": (24, 64), "singlearrow": (24, 64),
            "kaiguankai": (24, 64), "CN": (0, 0), "transformer2": (48, 60), "transformer3": (85, 66),
            "generator": (40, 40)}
daozhastat = {}
kaiguanstat = {}
sideBusFP = ['Disconnector', 'Disconnector', 'Breaker', 'Disconnector']
busPairFP = ['Disconnector', 'Disconnector']
transBus = collections.defaultdict(list)
globOffset = 200
colorMap = {}

class BusSkeleton:
    def __init__(self, cnID, x, y, w, dir):
        self.id = cnID
        self.x = x
        self.y = y
        self.w = w
        self.dir = dir
        self.reverseC = False

    def reverseConnector(self):
        self.reverseC = True

    def GetLength(self):
        BNumber = max(adjDict[self.id]-1, 1)
        return BNumber * 120

def isPairEnd(n, ID):
    if (n in VerticalBusPair and n == VerticalBusPair[ID]):
        return True
    if (n in HorizontalBusPair and n == HorizontalBusPair[ID]):
        return True
    return False

def reset():
    global BusDict
    global BusCNID
    global VerticalBusPair
    global adjDict
    global AllTrans
    global daozhastat
    global HorizontalBusPair
    global transBus
    global globOffset
    global kaiguanstat
    global colorMap

    colorMap = {}
    kaiguanstat = {}
    globOffset = 400
    HorizontalBusPair = {}
    VerticalBusPair = {}
    AllTrans = {}
    adjDict = {}
    BusCNID = set()
    BusDict = {}
    daozhastat = {}
    transBus = collections.defaultdict(list)

def placeBus(id, x, y, w, dir):
    BusDict[id] = BusSkeleton(id, x,y,w, dir)

def AddVerticalBusPair(b1, b2):
    VerticalBusPair[b1] = b2
    VerticalBusPair[b2] = b1

def AddHorizontalBusPair(b1, b2):
    HorizontalBusPair[b1] = b2
    HorizontalBusPair[b2] = b1

def fillRelation(adj, BusCNs):
    global adjDict
    global BusCNID
    adjDict = adj
    BusCNID = BusCNs


visitedBusCN = set()