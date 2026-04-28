/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_ripplecarry (
    input  wire [7:0] ui_in,    
    output wire [7:0] uo_out,   
    input  wire [7:0] uio_in,   
    output wire [7:0] uio_out,  
    output wire [7:0] uio_oe,   
    input  wire       ena,      
    input  wire       clk,      
    input  wire       rst_n     
);

    wire [3:0] A, B;
    wire Cin;
    wire [3:0] Sum;
    wire Cout;
    wire c1, c2, c3;

    assign A   = ui_in[3:0];
    assign B   = uio_in[3:0];
    assign Cin = ui_in[4];

    // Ripple Carry Adder Logic
    assign Sum[0] = A[0] ^ B[0] ^ Cin;
    assign c1     = (A[0] & B[0]) | (Cin & (A[0] ^ B[0]));

    assign Sum[1] = A[1] ^ B[1] ^ c1;
    assign c2     = (A[1] & B[1]) | (c1 & (A[1] ^ B[1]));

    assign Sum[2] = A[2] ^ B[2] ^ c2;
    assign c3     = (A[2] & B[2]) | (c2 & (A[2] ^ B[2]));

    assign Sum[3] = A[3] ^ B[3] ^ c3;
    assign Cout   = (A[3] & B[3]) | (c3 & (A[3] ^ B[3]));

    // Output mapping
    assign uo_out[3:0] = Sum;
    assign uo_out[4]   = Cout;
    assign uo_out[7:5] = 3'b000;

    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

    // Unused signals
    wire _unused = &{ena, clk, rst_n, ui_in[7:5], uio_in[7:4], 1'b0};

endmodule
