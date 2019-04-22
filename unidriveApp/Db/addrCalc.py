
class paramProps(object):
   paramDict = {}
   def __init__(self, idx, bits, dp):
      self.bits = bits
      self.dp = dp
      paramProps.paramDict[idx] = self

#
# All entries in the dictionary are 32 bit integers. The value is the number
# of decimal places
#
for idx in range(101, 108):
   paramProps(idx, 32, 1)

for idx in [117, 118]:
   paramProps(idx, 32, 1)

for idx in range(121, 129):
   paramProps(idx, 32, 1)

for idx in range(129, 135):
   paramProps(idx, 16, 1)

for idx in range(136, 138):
   paramProps(idx, 32, 1)

paramProps(138, 32, 2)
paramProps(139, 32, 1)




keys = paramProps.paramDict.keys()
keys.sort()

for item in keys:
   print item, paramProps.paramDict[item].bits, paramProps.paramDict[item].dp
