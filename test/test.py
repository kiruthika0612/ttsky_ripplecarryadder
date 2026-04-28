# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start Ripple Carry Adder Test")

    # Clock generation
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1

    # -------------------------
    # Test Case 1: 3 + 5 = 8
    # -------------------------
    # A = 0011, B = 0101, Cin = 0
    dut.ui_in.value = 0b00000011
    dut.uio_in.value = 0b00000101
    await ClockCycles(dut.clk, 1)

    expected = 0b00001000   # Cout=0, Sum=1000
    assert dut.uo_out.value == expected, f"Test1 Failed: got {dut.uo_out.value}, expected {expected}"

    # -------------------------
    # Test Case 2: 15 + 1 = 16
    # -------------------------
    # A = 1111, B = 0001, Cin = 0
    dut.ui_in.value = 0b00001111
    dut.uio_in.value = 0b00000001
    await ClockCycles(dut.clk, 1)

    expected = 0b00010000   # Cout=1, Sum=0000
    assert dut.uo_out.value == expected, f"Test2 Failed: got {dut.uo_out.value}, expected {expected}"

    # -------------------------
    # Test Case 3: 7 + 8 = 15
    # -------------------------
    # A = 0111, B = 1000, Cin = 0
    dut.ui_in.value = 0b00000111
    dut.uio_in.value = 0b00001000
    await ClockCycles(dut.clk, 1)

    expected = 0b00001111   # Cout=0, Sum=1111
    assert dut.uo_out.value == expected, f"Test3 Failed: got {dut.uo_out.value}, expected {expected}"

    # -------------------------
    # Test Case 4: 15 + 15 + Cin(1) = 31
    # -------------------------
    # A = 1111, Cin = 1 => ui_in = 00011111
    # B = 1111
    dut.ui_in.value = 0b00011111
    dut.uio_in.value = 0b00001111
    await ClockCycles(dut.clk, 1)

    expected = 0b00011111   # Cout=1, Sum=1111
    assert dut.uo_out.value == expected, f"Test4 Failed: got {dut.uo_out.value}, expected {expected}"

    dut._log.info("All Ripple Carry Adder tests passed!")
