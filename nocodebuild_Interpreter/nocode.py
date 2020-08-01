import sys
ncfile=sys.argv[1]
realcode=""
rawcode=""
sub="‪"
split="‫"
dict=""" 
!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~‪‫"""
with open(ncfile,'r')as file:
  rawcode=file.read()
for line in rawcode.split(split):
  realcode+=dict[line.count(sub)]
#print(realcode)
exec(realcode)
