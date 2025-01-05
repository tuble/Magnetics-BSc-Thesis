from enum import Enum

class WaveShape(Enum):
    SQUARE = 1
    SINE = 2
    # etc.

'''
typ
freq
amp_pp
offst
duty
phase
hlvl
llvl
'''
# errror checking for valid data ranges
class WaveParams:
    def __init__(self, ch, shape, freq, amp, duty=50, offst=0, phase=0):
        # 1 or 2
        self.ch = ch
        # SQUARE, SINE, ETC
        self.shape = shape 
        # 1 - 1 Meg ?
        self.freq = freq
        # 1 - 20 pp
        self.amp = amp
        # 0-100
        self.duty = duty
        # ?? Volts
        self.offst = offst
        # 0-360 
        self.phase = phase

    def __repr__(self):
        return f"on C{self.ch} {self.shape} wave f:{self.freq}Hz amp:{self.amp} D:{self.duty} p:{self.phase}"

    @property
    def ch(self):
        return self._ch

    @property
    def shape(self):
        return self._shape.name

    @property
    def freq(self):
        return self._freq

    @property
    def amp(self):
        return self._amp

    @property
    def duty(self):
        return self._duty

    @property
    def offst(self):
        return self._offst

    @property
    def phase(self):
        return self._phase

    @ch.setter
    def ch(self, val):
        if not (1 <= val <= 2):
            raise AttributeError(f"Invalid channel {val}")
        self._ch = val

    @shape.setter
    def shape(self, val):
        if not isinstance(val, WaveShape):
            raise TypeError(f"Value must be a WaveShape Enum type")
# TODO
        if not val in WaveShape:
            raise AttributeError(f"Invalid shape {val}") 
        self._shape = val

    @freq.setter
    def freq(self, val):
        if not isinstance(val, int):
            raise TypeError(f"Value must be an integer")
        if not (1 <= val <= 30000000):
            raise AttributeError(f"frequency out of range: {val}") 

        self._freq = val 

    @amp.setter
    def amp(self, val):
        if not isinstance(val, int):
            raise TypeError(f"Value must be an integer")
        if not (1 <= val <= 20):
            raise AttributeError(f"Amplitude out of range: {val}") 

        self._amp = val 

    @duty.setter
    def duty(self, val):
        if not isinstance(val, int):
            raise TypeError(f"Value must be an integer")
        if not (0 <= val <= 100):
            raise AttributeError(f"Duty Cycle out of range: {val}") 

        self._duty = val 

    @offst.setter
    def offst(self, val):
# Value does not need to be an integer
# 3 point precision double
        if not (0 <= val <= 100):
            raise AttributeError(f"offst out of range: {val}") 

        self._offst = val 

    @phase.setter
    def phase(self, val):
        if not isinstance(val, int):
            raise TypeError(f"Value must be an integer")
        if not (0 <= val <= 360):
            raise AttributeError(f"phase out of range: {val}") 

        self._phase = val 
