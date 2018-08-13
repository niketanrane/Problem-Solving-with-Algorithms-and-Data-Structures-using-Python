__author__= "niketanrane"

def moveTower(height, fromPole, toPole, usingPole):
    if height >= 1 :
        moveTower(height - 1, fromPole, usingPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height - 1, usingPole, toPole, fromPole)

def moveDisk(fromPole, toPole):
    print("Move disk from ", fromPole, "to", toPole)

moveTower(3,"A","B","C")