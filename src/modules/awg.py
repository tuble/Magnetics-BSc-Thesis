from modules.genchan import *
from modules.instr import *

class AWG(Instrument):
    '''
    Ch1: GenChannel 
    Ch2: GenChannel 
    '''

    def __init__(self, vid, Ch1: GenChannel, Ch2: GenChannel):
        self.vid = vid
        super().__init__(self.vid)
        self.Ch1 = Ch1
        self.Ch2 = Ch2

    
    def set_channel(self, chnum):
        if chnum == 1:
            C = self.Ch1
        elif chnum == 2:
            C = self.Ch2
        else:
            raise ValueError(f"Invalid channel number {chnum}")

        cmds = C.scpi_set_chan()
        for c in cmds:
            self.instr.write(c)
#           time.sleep(self.timeout)

    def enable_channel(self, chnum):
        if chnum == 1:
            C = self.Ch1
        elif chnum == 2:
            C = self.Ch2
        else:
            raise ValueError(f"Invalid channel number {chnum}")
        self.instr.write(C.scpi_en_chan())

    def disable_channel(self, chnum):
        if chnum == 1:
            C = self.Ch1
        elif chnum == 2:
            C = self.Ch2
        else:
            raise ValueError(f"Invalid channel number {chnum}")

        self.instr.write(C.scpi_dis_chan())
