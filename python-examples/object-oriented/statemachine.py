# simple state machine
import time
class robotIntake:
    intakeStatus: str
    intakeContent: str

    def __init__(self, status, full):
        self.intakeStatus = status
        self.intakeContent = full

    def getIntakeStatus(self):
        print(self.intakeStatus)
        time.sleep(5)
        return self.intakeStatus

    def getIntakeContent(self):
        time.sleep(5)
        print(self.intakeContent)
        return self.intakeContent

    def setIntakeStatus(self, status):
        self.intakeStatus = status

    def setIntakeContent(self, full):
        self.intakeContent = full
    
    def runIntake(self):
        self.intakeContent = True
    
    def runEject(self):
        self.intakeContent = False
    


def main():
    currentIntake = robotIntake("up", "empty")
    while True:
        if (currentIntake.getIntakeContent() == "empty"):
            currentIntake.setIntakeStatus("down")
            if (currentIntake.getIntakeStatus() == "down"):
                currentIntake.runIntake()
            else:
                currentIntake.setIntakeStatus("down")
        else:
            currentIntake.setIntakeStatus("up")
            if (currentIntake.getIntakeStatus() == "up"):
                currentIntake.runEject()
            else:
                currentIntake.setIntakeStatus("up")
                
            


main()
