import threading
import time 

from modules.psu import * 
from modules.awg import AWG 
from modules.osc import Scope 

# globals 
psu_comport = 'COM2'
osc_vid = 'USB0::0xF4EC::0xEE38::SDSMMGKX7R3585::INSTR'
awg_vid = 'USB0::0xF4EC::0x1103::SDG1XDDQ7R4187::INSTR'

def main():
#    psu2 = RD6006(psu_comport)
    
    # Save .csv test start
    osc = Scope(osc_vid, ScopeChannel(1, 1, 0, 0, "on", "V", 2), None)

    osc.instr.write("TDIV 500US")
    osc.instr.write("MSIZ 7K")
    # -> SARA = MSIZ * (TDIV*14) = 1 MHz
    print("DBG: send_csv start")
    osc.send_csv(1)
    print("DBG: send_csv end")
    time.sleep(5)

    return
    # Save .csv test end

#   Temp VISA test start
    awg = AWG(awg_vid, GenChannel(1, WaveShape.SQUARE, 100, 6, 25, 50, 0), None) 
    osc = Scope(osc_vid, ScopeChannel(1, 1, 0, 0, "on", "V", 2), None)

    #awg.Ch1 = GenChannel(2, WaveShape.SQUARE, 200, 3, 25, 50, 0)
    awg.enable_channel(2)
    awg.set_channel(1)
    time.sleep(3)
    osc.set_channel(1)

    time.sleep(0.5)
    # osc save to csv test

    osc.close()
    awg.close()

    return
#   Temp VISA test end

if __name__ == "__main__":
    main()
