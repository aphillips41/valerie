import os

class valTest:

    def __init__(self, test_name, service_name, network_name):
        self.Name = test_name
        self.Service_name = service_name
        self.Network_name = network_name

    def Run(val_test):
        cmdStr = "docker run -d --rm --network " + val_test.Network_name + " " + val_test.Service_name
        out = os.system(cmdStr)
        return out

