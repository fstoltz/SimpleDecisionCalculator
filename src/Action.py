

class Action:
    #Constructor
    def __init__(self, definedAction):
        self.actionName = definedAction
        self.pros = {}
        self.cons = {}


    #Helpers
    def addPro(self, pro, value):
        self.pros[pro] = value

    def addCon(self, con, value):
        self.cons[con] = value


    #Getters
    def getProSum(self):
        proSum = 0
        for value in self.pros.values():
            proSum += value
        return proSum

    def getConSum(self):
        conSum = 0
        for value in self.cons.values():
            conSum += value
        return conSum


    def getSummary(self):
        #Retrieve values from the pro / con dicts
        #return self.getProSum() + " | "
        return "+"+str(self.getProSum()) + " | " + str(self.getConSum())
