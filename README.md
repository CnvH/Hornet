# Hornet
This is a set of routines for running a TF03 Lidar range finder and a pair of wifi stepper motors for a pan tilt platform 
to steer the TF03 as it tracks a flying insect.  As much as possible these routines will be run on an ESP32 microcontroller
in micropython with overall master control being vested with high level code running on a Raspberry Pi.

The routines will be collected in a module with appropriate classes (to be documented here)

class Ring implements a Fifo/Lifo buffer: 
