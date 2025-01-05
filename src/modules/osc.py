from modules.instr import Instrument
from modules.scopechan import ScopeChannel 
import time

class Scope(Instrument):
    def __init__(self, vid, Ch1: ScopeChannel, Ch2: ScopeChannel):
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

    def set_trigger(ch,):
        pass

    # TODO toggle relative & normal time (?)
    def save_csv(ch):
        self.self.instr.write(f'CHDR OFF')
        vdiv = float(self.instr.query(f'C{ch}:VDIV?'))
        ofst = float(self.instr.query(f'C{ch}:OFST?'))
        tdiv = float(self.instr.query(f'TDIV?'))
        trdl = (-1) * float(self.instr.query(f'TRDL?'))
        sara = float(self.instr.query(f'SARA?'))

        dflt_chsz = self.instr.chunk_size

        #TODO self.instr.timeout
        # N*1kByte
        # USB2 60MB/s
        # 1 MByte
        self.instr.chunk_size = 1024*1024

        npts = 0
        self.instr.write(f'WFSU SP,0,NP,{npts},FP,0')

#    self.instr.write(f'SYST:INFO?')

        # ask for trace data
        # TODO for each channel
        self.instr.write(f'C{ch}:WF? DAT2')

        # retrieve trace data
        rec = list(self.instr.read_raw())
        hdr = rec[:15]
        
        print(f"hdr information: {hdr}")

        wvfm = rec[15:]

        # Remove last 2 stop bytes 0x0A 0x0A
        wvfm.pop()
        wvfm.pop()

        # TODO change filename
        fname = "TEST.csv"
        f = open(fname, 'w')
        # TODO
        # ... Header Ctrl info . . . 

        conversion_constant = float(vdiv/25)
        # sampling window
        Ts = float(1/sara)
        total_time = tdiv * 14
        # relative to trdl 0
        t_left = -(total_time / 2)
        #t_right = total_time

        # fit trigger delay to window
        t_trigger = ((7*tdiv) - trdl)

        # sample idx
        i = 0
        for s in wvfm:
            if s > 127:
                s -= 255
            s = ((s*conversion_constant) - ofst)

            current_time = t_left + i*Ts
            tr = current_time - t_trigger
            i+=1
            line = f"{tr}, {s}"
            # write sample+time info to file
            f.write(line+'\n')

        f.flush()
        f.close()

        # restore default chunk_size
        self.instr.chink_size = dflt_chsz 

# in hepler f()s TODO
# this f() may be useless 
    def read_exponent(string_num):
        sstr = string_num.split('E') 
        return (float(sstr[0]) * (10**int(sstr[1])))
