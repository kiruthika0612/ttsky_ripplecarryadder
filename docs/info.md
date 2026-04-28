<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

This project implements a 4-bit ripple carry adder that adds two 4-bit binary inputs (A[3:0] and B[3:0]) along with a carry input (Cin) and produces a 4-bit sum output (Sum[3:0]) and a carry output (Cout) using cascaded full-adder logic.

## How to test

Apply 4-bit inputs on ui[3:0] and uio[3:0], set the carry input on ui[4], and verify that the outputs uo[3:0] and uo[4] match the expected binary sum and carry output.
## External hardware

No external hardware is required.
