import struct

osc_address = "/python"

#converts a string into OSC data.
def pad_string(s):
    return s.encode() + b'\x00' * (4 - (len(s) % 4))

#converts a list of floats into a list of OSC data. 
def pack_floats(l):
    format = "!" + ("f" * len(l))
    packed = struct.pack(format, *l)
    
    return packed

#creates a full OSC message ready to be sent over UDP.
def create_message(l):
    osc_type = "," + ("f" * len(l) )

    floats = pack_floats(l)
    message = pad_string(osc_address) + pad_string(osc_type) + floats
    return message

