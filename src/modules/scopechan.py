'''
VDIV
UNIT
TRACE ON
OFST
CPL
SKEW ? 
BWL?
ATTN - Probe attenuation
pg. 40
'''

''' 
Trigger:
TRIG_DELAY
TRIG_LEVEL
TRIG_MODE
TRIG_PATTERN
TRIG_SELECT
TRIG_SLOPE
pg. 190
'''
class ScopeChannel:
    def __init__(self, ch, attn, cpl, vofst, tra, unit, vdiv):
        # 1 or 2
        self._ch = ch
        self._attn = attn 
        self._cpl = cpl
        # - + 
        self._vofst = vofst
        # "on" or "off"
        self._tra = tra
        self._unit = unit
        self._vdiv = vdiv

    def __repr__(self):
        return f"scope C{self.ch} {self.attn} {self.cpl} {self.vofst}\
        {self.tra} {self.unit} {self.vdiv}"

    @property
    def ch(self):
        return self._ch

    @property
    def attn(self):
        return self._attn

    @property
    def cpl(self):
        return self._cpl

    @property
    def vofst(self):
        return self._vofst

    @property
    def tra(self):
        return self._tra

    @property
    def unit(self):
        return self._unit

    @property
    def vdiv(self):
        return self._vdiv

    @ch.setter
    def ch(self, val):
        if not (1 <= val <= 2):
            raise AttributeError(f"Invalid channel {val}")
        self._ch = val

    @attn.setter
    def attn(self, val):
        # TODO
        self._attn = val

    @cpl.setter
    def cpl(self, val):
        # TODO
        self._cpl = val

    @vofst.setter
    def vofst(self, val):
        # TODO
        self._vofst = val

    @tra.setter
    def tra(self, val):
        # TODO
        self._tra = val

    @unit.setter
    def unit(self, val):
        # TODO
        self._unit = val

    @vdiv.setter
    def vdiv(self, val):
        # TODO
        self._vdiv = val

    def scpi_set_chan(self):
        return [f"C{self.ch}:ATTN {self.attn}",
                f"C{self.ch}:CPL {self.cpl}",
                f"C{self.ch}:OFST {self.vofst}",
                f"C{self.ch}:TRA {self.tra}",
                f"C{self.ch}:UNIT {self.unit}",
                f"C{self.ch}:VDIV {self.vdiv}"]
