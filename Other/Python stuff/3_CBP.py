#   Converts CBP_name_commands to minecart command block chunks
fileNameOriginal = '3O_CBP.txt'
fileNameTemp = '3T_CBP.txt'
fileNameFinal = '3F_CBP.txt'

lenNumber = 24000
server = 1

if server == 1:
    serverText = 'minecraft:'
else:
    serverText = ''

lenBeg = 'summon FallingSand ~ ~1 ~ {Block:stone,Time:1,Passengers:[{id:FallingSand,Block:redstone_block,Time:1,Passengers:[{id:FallingSand,Block:activator_rail,Time:1,Passengers:[{id:MinecartCommandBlock,Command:'
lenMid = '},{id:MinecartCommandBlock,Command:'
lenEnd = '},{id:MinecartCommandBlock,Command:setblock ~ ~1 ~ chain_command_block 0 replace {Command:fill ~ ~-4 ~ ~ ~2 ~ air,auto:1b}},{id:MinecartCommandBlock,Command:setblock ~ ~2 ~ command_block 0 replace {Command:minecraft:kill @e[type=MinecartCommandBlock,r=10]}},{id:MinecartCommandBlock,Command:setblock ~ ~3 ~ redstone_block},{id:MinecartCommandBlock,Command:summon FallingSand ~ ~-2 ~ {Block:command_block,Time:1s,TileEntityData:{TrackOutput:0b}}},{id:MinecartCommandBlock,Command:' + serverText + 'kill @e[type=MinecartCommandBlock,r=3]}]}]}]}'

def copy_file(a, b):
    readFile1 = open(a, 'r')
    readFile2 = open(b, 'w')
    fileMessage = readFile1.read()
    readFile2.write(fileMessage)
    readFile1.close()
    readFile2.close()

copy_file(fileNameOriginal, fileNameTemp)

def replace_function(a,b):
    readTempFileRepeat = open(fileNameTemp, 'r+')
    fileTempEdit = readTempFileRepeat.read()
    open(fileNameTemp, 'w').close()
    fileEdit = fileTempEdit.replace(a, b)
    open(fileNameTemp, 'w').write(fileEdit)
    readTempFileRepeat.close()

#   print(replace_function.__doc__)
replace_function(',CustomName:"CBP",LastOutput:"{\\"text\\":\\"Made with CBP\\"}"', '')
replace_function('\\', '\\\\')
replace_function('\\"', '\\\\"')

#   Removes all empty lines, puts it into fileName3
readTempFile = open(fileNameTemp, 'r')
readNewFile = open(fileNameFinal, 'w')

for line in readTempFile:
    if not line.isspace():
        readNewFile.write(line)

readTempFile.close()
readNewFile.close()

copy_file(fileNameFinal, fileNameTemp)

readNewFile = open(fileNameFinal, 'w')
readTempFile = open(fileNameTemp, 'r+')
fileSplit = readTempFile.read().split('\n')

fileLenEdit = lenBeg
for s in fileSplit:
    if not s:
        lenWrite = fileLenEdit + 'say PCBP end' + lenEnd + '\n' + '\n'
        readNewFile.write(lenWrite)
        fileLenEdit = lenBeg
        break
    fileLenEdit += s
    if len(fileLenEdit + lenEnd) >= lenNumber:
        lenWrite = fileLenEdit + lenEnd + '\n' + '\n'
        readNewFile.write(lenWrite)
        fileLenEdit = lenBeg
    else:
        fileLenEdit += lenMid
