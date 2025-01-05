import pyvisa as visa

class Instrument:
    def __init__(self, vid):
        self.rm = visa.ResourceManager()
        self.instr = self.rm.open_resource(vid)

    def close(self):
        self.instr.close()

    def __del__(self):
        self.close()
        self.rm.close()
