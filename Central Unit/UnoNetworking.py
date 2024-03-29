import PyCmdMessenger
import serial.tools.list_ports
import time
from random import randint

class UnoNetworkController(object):
    commands = [["roll_out", "i"],
                ["get_temp", ""],
                ["get_length", ""],
                ["error", "s"],
                ["temp_is", "i"],
                ["rollout_done", "s"],
                ["length_is", "i"],
                ["get_light", ""],
                ["light_is", "i"],
                ["distance_is", "i"],
                ["light_threshold_is", "i"],
                ["temp_threshold_is", "i"],
                ["get_distance", "i"],
                ["set_temp_threshold", "i"],
                ["set_light_threshold", "i"],
                ["get_light_threshold", "i"],
                ["set_max_rollout", "i"],
                ["get_temp_threshold", "i"],
                ["timer_runtime_end", "s"],
                ["is_rolled_out", "s"],
                ["is_rolled_out_is", "s"],
                ["toggle_auto", ""]
                ]

    arduino = 0#PyCmdMessenger.ArduinoBoard("COM3", baud_rate=9600)
    messenger = 0#PyCmdMessenger.CmdMessenger(arduino, commands)
    isConnected = 0

    def UnoNetworkController(self, isConnected):
        self.isConnected = isConnected;

    def connect(self):
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            if("Uno" in str(p)):
                port = str(p).split(" ")[0]
                self.arduino = PyCmdMessenger.ArduinoBoard(port, baud_rate=9600)
                self.messenger = PyCmdMessenger.CmdMessenger(self.arduino, self.commands)
                print("Connected succesfully")
        return True

    def connectWithPort(self, port):
        self.arduino = PyCmdMessenger.ArduinoBoard(port, baud_rate=9600)
        self.messenger = PyCmdMessenger.CmdMessenger(self.arduino, self.commands)
        print("Connected succesfully")
        return True

    def rollOut(self, roll_out):
        self.messenger.send("roll_out", roll_out)
        #time.sleep(3)
        #msg = self.messenger.receive("s")
        return str("")

    def getTemp(self):
        valid = False
        self.messenger.send("get_temp")

        while not valid:
            msg = self.messenger.receive("s")
            if msg != None:
                if str(msg[0]) == "temp_is":
                    return int(str(msg[1][0]).split(".")[0])
                    valid = True


    def getLight(self):
        valid = False
        self.messenger.send("get_light")
        while not valid:
            msg = self.messenger.receive("s")
            if msg != None:
                if str(msg[0]) == "light_is":
                    return int(str(msg[1][0]).split(".")[0])
                    valid = True

    def getDistance(self):
        self.messenger.send("get_distance")
        msg = self.messenger.receive("s")
        if (msg != None):
            return int(str(msg[1][0]).split(".")[0])
        else:
            return 0


    def getLength(self):
        self.messenger.send("get_length")
        msg = self.messenger.receive("s")
        return int(str(msg[1][0]).split(".")[0])

    def getLightThreshold(self):
        self.messenger.send("get_light_threshold")
        msg = self.messenger.receive("s")
        return int(str(msg[1][0]))

    def getTempThreshold(self):
        self.messenger.send("get_temp_threshold")
        msg = self.messenger.receive("s")
        return int(str(msg[1][0]))

    def getRolledOut(self):
        valid = False
        self.messenger.send("is_rolled_out")

        while not valid:
            msg = self.messenger.receive("s")
            if msg != None:
                if str(msg[0]) == "is_rolled_out_is":
                    return int(str(msg[1][0]))
                    valid = True


    def setTempThreshold(self, value):
        self.messenger.send("set_temp_threshold", value)
        msg = self.messenger.receive("s")
        return int(str(msg[1][0]))

    def setLightThreshold(self, value):
        self.messenger.send("set_light_threshold", value)
        msg = self.messenger.receive("s")
        return int(str(msg[1][0]))

    def forceError(self):
        self.messenger.send("force_error")
        msg = self.messenger.receive("s")
        return msg

    def waitForMessage(self):
        msg = self.messenger.receive("s")
        return msg;

    def toggleauto(self):
        self.messenger.send("toggle_auto")