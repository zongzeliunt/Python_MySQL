#!/usr/bin/env python
import serial
import sys, time
from curses import wrapper

WAIT = 0.2

# works with dual-channel supplies with overvoltage protection: E3646A

def main(stdscr):
    stdscr.clear()
    stdscr.nodelay(True)
    initwindow = stdscr.subwin(3,80,0,0)
    monitorwindow = stdscr.subwin(2,80,3,0)

    ser = serial.Serial(sys.argv[1], 9600, timeout=1, dsrdtr=True)
    ser.flush()
    ser.write("SYST:REM\r\n".encode())
    time.sleep(WAIT)

    redraw_settings(ser,initwindow)

    while True:
        c = stdscr.getch()
        if c == ord('q'):
            break
        elif c == ord('R'):
            recall_settings(ser)
            monitorwindow.erase()
            initwindow.erase()
            redraw_settings(ser,initwindow)
        elif c == ord('N'):
            power_on(ser)
            monitorwindow.erase()
        elif c == ord('F'):
            power_off(ser)
            monitorwindow.erase()
        ser.write("INST:NSEL 1\r\n".encode())
        time.sleep(WAIT)
        monitorwindow.addstr(0,0,print_status(ser))
        monitorwindow.refresh()
        ser.write("INST:NSEL 2\r\n".encode())
        time.sleep(WAIT)
        monitorwindow.addstr(1,0,print_status(ser))
        monitorwindow.refresh()

def redraw_settings(ser,initwindow):
    ser.write("*IDN?\r\n".encode()); response = ser.readline()
    initwindow.addstr(0,0,response.decode().strip())
    initwindow.refresh()
    time.sleep(WAIT)
    ser.write("INST:NSEL 1\r\n".encode())
    time.sleep(WAIT)
    initwindow.addstr(1,0,print_settings(ser))
    initwindow.refresh()
    ser.write("INST:NSEL 2\r\n".encode())
    time.sleep(WAIT)
    initwindow.addstr(2,0,print_settings(ser))
    initwindow.refresh()

def power_on(ser):
    ser.write("OUTPUT ON\r\n".encode())
    time.sleep(WAIT)
        
def power_off(ser):
    ser.write("OUTPUT OFF\r\n".encode())
    time.sleep(WAIT)

def recall_settings(ser):
    ser.write("*RCL 1\r\n".encode())
    time.sleep(5*WAIT)

def print_settings(ser,end="\n"):
    outstr = ""
    ser.write("INST:SEL?\r\n".encode()); response = ser.readline()
    channel = response.decode().strip()
    outstr += "channel {0}: ".format(channel)

    #ser.write("OUTPUT?\r\n".encode()); response = ser.readline()
    #output_enabled = "ON" if int(response)==1 else "OFF"
    #outstr += "output {0}, ".format(output_enabled)

    ser.write("VOLT?\r\n".encode()); response = ser.readline()
    volt_set = float(response)
    ser.write("CURR?\r\n".encode()); response = ser.readline()
    curr_set = float(response)
    outstr += "setpoints {0:.3f} V {1:.3f} A, ".format(volt_set, curr_set)

    ser.write("VOLT:PROT:STATE?\r\n".encode()); response = ser.readline()
    ovp_enabled = "ENABLED" if int(response)==1 else "DISABLED"
    ser.write("VOLT:PROT:LEVEL?\r\n".encode()); response = ser.readline()
    ovp_setpoint = float(response)
    outstr += "OVP {0} @ {1} V".format(ovp_enabled, ovp_setpoint)

    #not supported by E3646A?
    #ser.write("CURR:PROT:STATE?\r\n".encode()); response = ser.readline()
    #ocp_enabled = "ENABLED" if int(response)==1 else "DISABLED"
    #ser.write("CURR:PROT:LEVEL?\r\n".encode()); response = ser.readline()
    #ocp_setpoint = float(response)
    #print("OCP {0} @ {1} A".format(ocp_enabled, ocp_setpoint),end="")

    return outstr

def print_status(ser,end="\n"):
    outstr = ""
    ser.write("INST:SEL?\r\n".encode()); response = ser.readline()
    channel = response.decode().strip()
    outstr += "channel {0}: ".format(channel)

    #ser.write("APPLY?\r\n".encode()); response = ser.readline()
    #print(response.decode().strip())

    ser.write("OUTPUT?\r\n".encode()); response = ser.readline()
    output_enabled = "ON" if int(response)==1 else "OFF"
    outstr += "output {0}, ".format(output_enabled)

    ser.write("MEAS:VOLT?\r\n".encode()); response = ser.readline()
    volt_readback = float(response)
    ser.write("MEAS:CURR?\r\n".encode()); response = ser.readline()
    curr_readback = float(response)
    outstr += "readbacks {0:.6f} V {1:.6f} A, ".format(volt_readback, curr_readback)

    ser.write("VOLT:PROT:TRIP?\r\n".encode()); response = ser.readline()
    ovp_tripped = "TRIPPED" if int(response)==1 else "OK"
    outstr += "OVP {0}".format(ovp_tripped)

    #not supported by E3646A?
    #ser.write("CURR:PROT:TRIP?\r\n".encode()); response = ser.readline()
    #ocp_tripped = "TRIPPED" if int(response)==1 else "OK"
    #print("OCP {0}".format(ocp_tripped),end="")

    return outstr

wrapper(main)
