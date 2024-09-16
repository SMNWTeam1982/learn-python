# simple state machine
import time
class robotIntake:
    intakeStatus: str
    intakeContent: str

    def __init__(self, status, full):
        self.intakeStatus = status
        self.intakeContent = full

    def getIntakeStatus(self):
        print("Current intake status to: " + self.intakeStatus)
        time.sleep(1)
        return self.intakeStatus

    def getIntakeContent(self):
        time.sleep(1)
        print("Current intake content to: " + self.intakeContent)
        return self.intakeContent

    def setIntakeStatus(self, status):
        print("Setting intake status to: " + status)
        self.intakeStatus = status

    def setIntakeContent(self, full):
        print("Setting intake content to: " + full)
        self.intakeContent = full
    
    def runIntake(self):
        self.intakeContent = "full"
    
    def runEject(self):
        self.intakeContent = "empty"
    


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

        time.sleep(1)
main()