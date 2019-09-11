step_commands = {}

step_0 = ["", ""]
step_0[0] = "./home/maps/git/misc_software/usbserial_testbeam/open_terminals.sh"
step_0[1] = "Open power supply terminals"
step_commands["Step 0: open steminals"] = step_0


step_1 = ["", ""]
step_1[0] = "source ~/software/Xilinx/Vivado/2017.4/settings64.sh; vivado -mode batch -source /home/maps/git/RUv1_Test_sync2018-08/bitstreams/program_3plus1.tcl"
step_1[1] = "Program RU FPGA"
step_commands["Step 1: program FPGA"] = step_1


step_2 = ["", ""]
step_2[0] = "source ~/git/RUv1_Test_sync2018-08/software/py/scl_source enable rh-python36"
step_2[1] = "Config python"
step_commands["Step 2: Config python"] = step_2















"""
step_commands["step_0"] = ["print 'abc'", " use to print abc"]
step_commands["step_1"] = ["print '123'", "use to print 123"]
step_commands["step_2"] = ["print 'fgh'", "use to print fgh"]
"""

