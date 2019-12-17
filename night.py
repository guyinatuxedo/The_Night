from pwn import *
import os



def lookupLibcs():
    libcVersions = []
    for libc in os.listdir("libc_versions/"):
        libcVersions.append(libc)
    return libcVersions

def lookOffset(symbol0, symbol1, libc):
    print "look"
    libc = ELF("libc_versions/" + libc)
    offset = libc.symbols[symbol0] - libc.symbols[symbol1]
    return offset

def findLibcVersion(symbol0, address0, symbol1, address1):
    offset = address0 - address1

    print "Offset:   " + hex(offset)
    print "Symbol0:  " + symbol0
    print "Symbol1:  " + symbol1
    print "Address0: " + hex(address0)
    print "Address1: " + hex(address1)

    libcVersions = lookupLibcs()
    for libc in libcVersions:
        libcOffset = lookOffset(symbol0, symbol1, libc)
        if libcOffset == offset:
            print "Potential Libc: " + libc

