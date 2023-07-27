#!/bin/python3
def bit_error(B):
    file_s = "sent.dat";
    file_r = "received.dat";
    
    if B:
        OFFSET = 49;
    else:
        OFFSET = 49*2;

    SIZE = 27*8;
    bit_errors = 0;
    sent = ""; received = "";
#-----
    read_s = open(file_s,'rb').read(); 
    read_r = open(file_r,'rb').read(); 

    for s in read_s:
        sent += '{0:08b}'.format(s);
    for r in read_r:
        received += '{0:08b}'.format(r);

    for i in range(0, SIZE):
        #print((sent[i], received[i+OFFSET]))
        if(sent[i] != received[i+OFFSET]):
            bit_errors += 1;

    #print("SENT: \n" + sent[:SIZE] + "\n")
    #print("RECEIVED: \n" + received[OFFSET:OFFSET+SIZE])

    #print("Bit errors: " + str(bit_errors));
    return bit_errors
