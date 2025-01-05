import time
from rd6006 import * 

max_v = 60

# * Ramp Up + Ramp Down
def set_voltage(psu, start, end, t=1, step=1):
	# Do not set voltage implicitly when calling set_voltage 
	if start != psu.voltage or start < 0 or start > max_v:
		print(f"{start} != {psu.voltage}")
		return

	psu.enable = True
	mul = -1 if start > end else 1
	step *= mul
	for v in range(start, (end+mul), step):
		psu.voltage = v
		# DBG
		print(psu.voltage)
		time.sleep(t)
	psu.enable = False 
