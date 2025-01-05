from enum import Enum

class WaveShape(Enum):
    SQUARE = 1
    SINE = 2

class GenChannel:
    # TODO HL & LL
    def __init__(self, ch, shape, freq, amp, duty=50, offst=0, phase=0):
        # 1 or 2
        self._ch = ch
        # SQUARE, SINE, ETC
        self._shape = shape 
        # 1 - 1 Meg ?
        self._freq = freq
        # 1 - 20 pp
        self._amp = amp
        # 0-100
        self._duty = duty
        # ?? Volts
        self._offst = offst
        # 0-360 
        self._phase = phase

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

    def scpi_set_chan(self):
        return [f"C{self.ch}:BSWV WVTP,{self.shape}",
                f"C{self.ch}:BSWV FQR,{self.freq}",
                f"C{self.ch}:BSWV AMP,{self.amp}",
                f"C{self.ch}:BSWV duty,{self.duty}",
                f"C{self.ch}:BSWV OFST,{self.offst}",
                f"C{self.ch}:BSWV PHSE,{self.phase}"]

    def scpi_en_chan(self):
        return f"C{self.ch}:OUTPUT ON"

    def scpi_dis_chan(self):
        return f"C{self.ch}:OUTPUT OFF"

