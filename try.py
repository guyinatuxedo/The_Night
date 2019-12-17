import night
from pwn import *

target = process("./try")

puts = target.recvline().strip("puts: ").strip("\n")
printf = target.recvline().strip("printf: ").strip("\n")

puts = int(puts, 16)
printf = int(printf, 16)

print "puts address: " + hex(puts)
print "printf address: " + hex(printf)

night.findLibcVersion("puts", puts, "printf", printf)

target.interactive()

