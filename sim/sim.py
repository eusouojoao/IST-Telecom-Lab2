#!/bin/python3
import signal
from bit_error import bit_error 

B=False;
BW = 0.0; N = 0.0;

if B:
    from mdBPSK_copy import mdBPSK as top_block_cls
else:
    from mdQPSK_copy import mdQPSK as top_block_cls

#-----
def sim():
    N0 = [x/2 for x in range(9)];
    loop_BW = [round(6/100 * x/10, 3) for x in range(1,43)];
    #---
    f1 = open("data.txt", "w"); f1.write("Loop BW/Noise");
    for N in N0:
        f1.write(" & " + str(N));
    f1.write(" \\\\\n");
    f2 = open("data.csv", "w"); f2.write("N,BW,bit_errors\n")
    #--- 'TeX
    for BW in loop_BW:
        b_error = [];
        for N in N0:
            #print("\nLoop bandwidth: " + str(BW) + " Noise voltage: " + str(N))
            tb = top_block_cls(BW,N); #simulação
            tb.start();
            tb.wait();
            b = bit_error(B);
            b_error.append(b);

        f1.write(str(BW));
        for i in b_error:
            f1.write(" & " + str(round(i/216*100,1)) + "%");
        f1.write(" \\\\\n")
    #--- .csv
    for N in N0:
        for BW in loop_BW:
            tb = top_block_cls(BW,N); #simulação
            tb.start();
            #tb.show();
            tb.wait();
            b = bit_error(B);
            f2.write(str(N) + "," + str(BW) + "," + str(b) + "\n");

    tb.show();
    #---
    f1.close();
    f2.close();
    #---
    def sig_handler(sig=None, frame=None):
        tb.stop();
        tb.wait();
    #---
    signal.signal(signal.SIGINT, sig_handler);
    signal.signal(signal.SIGTERM, sig_handler);
