dict=""" 
!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~‪‫"""
rawfile=""
output=""
sub="‪"
split="‫"
import sys
with open(sys.argv[1],'r') as raw:
  rawfile=raw.read()
for char in rawfile:
  print(char)
  output+=sub*dict.index(char)
  output+=split
with open("output.nc","w") as nc:
  nc.write(output[:-1])