;TYPE:CUSTOM
;added code by post processing
;script: PauseAtHeight.py
;current z: 0.900000
;current height: 0.600000
M83 ;Set extruder to relative mode
G1 Z1.900000 F300
G1 X190.000000 Y190.000000 F9000
G1 Z15 F300
M84 E0
M104 S0; standby temperature
M0 ;Do the actual pause
M109 S0; resume temperature
G1 Z1.900000 F300
G1 X75.600000 Y75.600000 F9000
G1 F9000
M82
G92 E750.775880 ;Set Position
