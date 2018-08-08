__author__ = 'niketanrane'

class LogicGate:

    def __init__(self, label):
        self.label = label
        self.output = None

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

    def getLabel(self):
        return self.label

class BinayGate(LogicGate):

    def __init__(self, label):
        # Always call the parent class so that all the data items are first inherited into the child class
        super(BinayGate, self).__init__(label)
        #LogicGate.__init__(self, label)
        self.A = None
        self.B = None

    def getA(self):
        if self.A == None:
            return int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))
        else:
            return self.A.getFrom().getOutput()

    def getB(self):
        if self.B == None:
            return int(input("Enter Pin B input for gate " + self.getLabel() + "-->"))
        else:
            return self.B.getFrom().getOutput()

class UnaryGate(LogicGate):

    def __init__(self, label):
        super(UnaryGate, self).__init__(label)
        self.A = None

    def getA(self):
        if self.A == None:
            return int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))
        else:
            return self.A.getFrom().getOutput()

class AndGate(BinayGate):

    def __int__(self, label):
        super(AndGate, self).__init__(label)

    def performGateLogic(self):
        self.A = self.getA()
        self.B = self.getB()
        #print("a = ", a, "b = ", b)
        if self.A == 1 and self.B == 1:
            return 1
        else:
            return 0

    def setNextPin(self, source):
        if self.A is None:
            self.A = source
        elif self.B is None:
            self.B = source
        else:
            RuntimeError("No input pins available")

class OrGate(BinayGate):
    def __init__(self, label):
        super(OrGate, self).__init__(label)

    def performGateLogic(self):
        self.A = self.getA()
        self.B = self.getB()
        if self.A == 0 and self.B == 0:
            return 0
        else:
            return 1

    def setNextPin(self, source):
        if self.A is None:
            self.A = source
        elif self.B is None:
            self.B = source
        else:
            RuntimeError("No input pins available")

class NotGate(UnaryGate):
    def __init__(self, label):
        super(NotGate, self).__init__(label)

    def performGateLogic(self):
        self.A = self.getA()

        if self.A == 0:
            return 1
        else:
            return 0
    def setNextPin(self, source):
        if self.A is None:
            self.A = source
        else:
            RuntimeError("No input pins available")

class NandGate(AndGate):
    def __init__(self, label):
        super(NandGate, self).__init__(label)

    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1


class NorGate(OrGate):
    def __init__(self, label):
        super(NorGate, self).__init__(label)

    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1

class Connector:

    def __init__(self, fromgate, togate):
        self.fromgate = fromgate
        self.togate = togate

        self.togate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate
'''
g1 = AndGate("G1")
print(g1.getOutput())

g2 = OrGate("G2")
print(g2.getOutput())

g3 = NotGate("G3")
print(g3.getOutput())
'''

def main():
   g1 = AndGate("G1")
   g2 = AndGate("G2")
   g3 = OrGate("G3")
   g4 = NotGate("G4")
   c1 = Connector(g1,g3)
   c2 = Connector(g2,g3)
   c3 = Connector(g3,g4)
   print(g4.getOutput())
   g5 = NandGate("G5")
   g6 = NorGate("G6")
   print(g6.getOutput())

main()
