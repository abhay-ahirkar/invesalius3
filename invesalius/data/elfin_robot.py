import invesalius.data.elfin as elfin
import time
import numpy as np


class elfin_server():
    def __init__(self, server_ip, port_number):
        self.server_ip = server_ip
        self.port_number = port_number
        #print(cobot.ReadPcsActualPos())

    def Initialize(self):
        SIZE = 1024
        rbtID = 0
        self.cobot = elfin.elfin()
        self.cobot.connect(self.server_ip, self.port_number, SIZE, rbtID)
        print("conected!")

    def Run(self):
        #target = [540.0, -30.0, 850.0, 140.0, -81.0, -150.0]
        #print("starting move")
        return self.cobot.ReadPcsActualPos()

    def SendCoordinates(self, target):
        coord = self.cobot.ReadPcsActualPos()
        print(coord)
        print(target)
        #target_keep_angle = np.hstack([target[:3],coord[3:]])
        #print(target_keep_angle)
        print(self.cobot.MoveL(target))
        status = self.cobot.ReadMoveState()
        while status == 1009:
            time.sleep(5)
            print("moving...")
            #print(self.cobot.ReadPcsActualPos())
            status = self.cobot.ReadMoveState()
            print(status)
        print("end move")
        #print(self.cobot.ReadPcsActualPos())

    def Close(self):
        self.cobot.close()