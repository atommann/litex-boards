# This file is Copyright (c) 2020 Hu XinLing <hxl_led@163.com>
# This file is Copyright (c) 2020 Long Li <atommann@gmail.com>
# License: BSD

from litex.build.generic_platform import *
from litex.build.xilinx import XilinxPlatform
from litex.build.openocd import OpenOCD

# IOs ----------------------------------------------------------------------------------------------

_io = [
    ("user_led", 0, Pins("A17"), IOStandard("LVCMOS25")),
    ("cpu_reset", 0, Pins("A10"), IOStandard("LVCMOS25")),
    ("clk200", 0,
        Subsignal("p", Pins("AB11"), IOStandard("LVDS")),
        Subsignal("n", Pins("AC11"), IOStandard("LVDS"))
    ),


    ("serial", 0,
        Subsignal("tx", Pins("C16")),
        Subsignal("rx", Pins("K15")),
        IOStandard("LVCMOS25")
    ),


    ("spiflash", 0,
        Subsignal("clk", Pins("B16")),
        Subsignal("cs_n", Pins("A18")),
        Subsignal("mosi", Pins("A19")),
        Subsignal("miso", Pins("B17")),
        IOStandard("LVCMOS25"),
    ),

    ("ddram", 0,
        Subsignal("a", Pins(
            "AD8 AC8 AA7 AA8 AF7 AE7 W8 V9",
            "Y10 Y11 Y7 Y8 V7 V8 W11 V11"),
            IOStandard("SSTL15")),
        Subsignal("ba", Pins("AA9 AC7 AB7"), IOStandard("SSTL15")),
        Subsignal("ras_n", Pins("AB9"), IOStandard("SSTL15")),
        Subsignal("cas_n", Pins("AC9"), IOStandard("SSTL15")),
        Subsignal("we_n", Pins("AD9"), IOStandard("SSTL15")),
        Subsignal("cs_n", Pins("AB12"), IOStandard("SSTL15")),
        Subsignal("dm", Pins("U6 Y3 AB6 AD4 AE17 AA14 AA19 Y17"),
            IOStandard("SSTL15")),
        Subsignal("dq", Pins(
            "U5 U2 U1 V3 W3 U7 V6 V4", 
            "Y2 V2 V1 W1 Y1 AB2 AC2 AA3",
            "AA4 AB4 AC4 AC3 AC6 Y6 Y5 AD6",
            "AD1 AE1 AE3 AE2 AE6 AE5 AF3 AF2",
            "AF17 AF14 AF15 AD15 AE15 AF19 AF20 AD16",
            "AA15 AC14 AD14 AB14 AB15 AA17 AA18 AB16",
            "AC18 AD18 AB17 AC17 AA20 AC19 AD19 AB19",
            "V16 V17 W15 W16 V18 V19 V14 W14"),
            IOStandard("SSTL15_T_DCI")),
        Subsignal("dqs_p", Pins("W6 AB1 AA5 AF5 AE18 Y15 AD20 W18"),
            IOStandard("DIFF_SSTL15")),
        Subsignal("dqs_n", Pins("W5 AC1 AB5 AF4 AF18 Y16 AE20 W19"),
            IOStandard("DIFF_SSTL15")),
        Subsignal("clk_p", Pins("W10"), IOStandard("DIFF_SSTL15")),
        Subsignal("clk_n", Pins("W9"), IOStandard("DIFF_SSTL15")),
        Subsignal("cke", Pins("AC12"), IOStandard("SSTL15")),
        Subsignal("odt", Pins("AA13"), IOStandard("SSTL15")),
        Subsignal("reset_n", Pins("AA2"), IOStandard("LVCMOS15")),
        Misc("SLEW=FAST"),
        Misc("VCCAUX_IO=HIGH")
    ),

    ("ddram_dual_rank", 0,
        Subsignal("a", Pins(
            "AD8 AC8 AA7 AA8 AF7 AE7 W8 V9",
            "Y10 Y11 Y7 Y8 V7 V8 W11 V11"),
            IOStandard("SSTL15")),
        Subsignal("ba", Pins("AA9 AC7 AB7"), IOStandard("SSTL15")),
        Subsignal("ras_n", Pins("AB9"), IOStandard("SSTL15")),
        Subsignal("cas_n", Pins("AC9"), IOStandard("SSTL15")),
        Subsignal("we_n", Pins("AD9"), IOStandard("SSTL15")),
        Subsignal("cs_n", Pins("AB12 Y12"), IOStandard("SSTL15")),
        Subsignal("dm", Pins("U6 Y3 AB6 AD4 AE17 AA14 AA19 Y17"),
            IOStandard("SSTL15")),
        Subsignal("dq", Pins(
            "U5 U2 U1 V3 W3 U7 V6 V4", 
            "Y2 V2 V1 W1 Y1 AB2 AC2 AA3",
            "AA4 AB4 AC4 AC3 AC6 Y6 Y5 AD6",
            "AD1 AE1 AE3 AE2 AE6 AE5 AF3 AF2",
            "AF17 AF14 AF15 AD15 AE15 AF19 AF20 AD16",
            "AA15 AC14 AD14 AB14 AB15 AA17 AA18 AB16",
            "AC18 AD18 AB17 AC17 AA20 AC19 AD19 AB19",
            "V16 V17 W15 W16 V18 V19 V14 W14"),
            IOStandard("SSTL15_T_DCI")),
        Subsignal("dqs_p", Pins("W6 AB1 AA5 AF5 AE18 Y15 AD20 W18"),
            IOStandard("DIFF_SSTL15")),
        Subsignal("dqs_n", Pins("W5 AC1 AB5 AF4 AF18 Y16 AE20 W19"),
            IOStandard("DIFF_SSTL15")),
        Subsignal("clk_p", Pins("W10 AC13"), IOStandard("DIFF_SSTL15")),
        Subsignal("clk_n", Pins("W9  AD13"), IOStandard("DIFF_SSTL15")),
        Subsignal("cke", Pins("AC12 AA12"), IOStandard("SSTL15")),
        Subsignal("odt", Pins("AA13 Y13"), IOStandard("SSTL15")),
        Subsignal("reset_n", Pins("AA2"), IOStandard("LVCMOS15")),
        Misc("SLEW=FAST"),
        Misc("VCCAUX_IO=HIGH")
    ),

    ("eth_clocks", 0,
        Subsignal("tx", Pins("R21")),
        Subsignal("gtx", Pins("N21")),
        Subsignal("rx", Pins("R22")),
        IOStandard("LVCMOS25")
    ),
    ("eth", 0,
        Subsignal("rst_n", Pins("U16")),
        Subsignal("int_n", Pins("P18")),
        Subsignal("mdio", Pins("R18")),
        Subsignal("mdc", Pins("T17")),
        Subsignal("rx_dv", Pins("U17")),
        Subsignal("rx_er", Pins("M19")),
        Subsignal("rx_data", Pins("N18 R17 R16 N17 P16 T19 T18 U20")),
        Subsignal("tx_en", Pins("U19")),
        Subsignal("tx_er", Pins("T23")),
        Subsignal("tx_data", Pins("M22 M21 P20 P19 L24 M24 M20 N19")),
        Subsignal("col", Pins("T22")),
        Subsignal("crs", Pins("R20")),
        IOStandard("LVCMOS25")
    ),

]

# Connectors ---------------------------------------------------------------------------------------

_connectors = [
    ("HPC", {
        "DP1_M2C_P": "P25",
        }
    ),
    ("LPC", {
        "GBTCLK0_M2C_P": "R25",
        }
    ),
  
]

# Platform -----------------------------------------------------------------------------------------

class Platform(XilinxPlatform):
    default_clk_name = "clk200"
    default_clk_period = 1e9/200e6

    def __init__(self):
        XilinxPlatform.__init__(self, "xc7k325t-ffg676-2", _io, _connectors, toolchain="vivado")
        self.add_platform_command("""
set_property CFGBVS VCCO [current_design]
set_property CONFIG_VOLTAGE 2.5 [current_design]
""")
        self.toolchain.bitstream_commands = ["set_property BITSTREAM.CONFIG.SPI_BUSWIDTH 4 [current_design]"]
        self.toolchain.additional_commands = ["write_cfgmem -force -format bin -interface spix4 -size 16 -loadbit \"up 0x0 {build_name}.bit\" -file {build_name}.bin"]

    def create_programmer(self):
        return OpenOCD("openocd_xc7_ft232.cfg", "bscan_spi_xc7a325t.bit")

    def do_finalize(self, fragment):
        XilinxPlatform.do_finalize(self, fragment)
        self.add_period_constraint(self.lookup_request("clk200",        loose=True), 1e9/200e6)
        self.add_period_constraint(self.lookup_request("eth_clocks:rx", loose=True), 1e9/125e6)
        self.add_period_constraint(self.lookup_request("eth_clocks:tx", loose=True), 1e9/125e6)
        self.add_platform_command("set_property DCI_CASCADE {{32 34}} [get_iobanks 33]")
