#!/usr/bin/python
# -*- coding: utf-8 -*-
from struct import pack, unpack
import sys
import math

if __name__ == "__main__":
    for x in sys.argv[1:]:
        x = float(x)

        # Encode the value as bytes and then interpret
        # it as uint64.
        x_bytes = pack(">d", x)
        x_uint64, = unpack(">Q", x_bytes)

        # Rewrite the appropriate fields to the new
        # variables. Extra note: ((1 << N) - 1) creates
        # a bit pattern of N 1's.
        x_sign = (x_uint64 >> 63) & 1
        x_exponent = (x_uint64 >> 52) & ((1 << 11) - 1)
        x_fraction = x_uint64 & ((1 << 52) - 1)

        x_fraction_str = bin(x_fraction)[2:].ljust(52, "0")
        print "--- Double Precision Number:", x
        print "Hex : %.16x" % x_uint64
        print "Sign: %s" % "+-"[x_sign]
        print "Exp : %u (dec) " % (x_exponent - 1023)
        print "Frac: 1.%s (bin)\n" % x_fraction_str