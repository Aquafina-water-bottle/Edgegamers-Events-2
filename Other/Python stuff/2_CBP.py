#   Converts PCBP_name to proper CBP_name files
#   Features:
#       |0||1| --> |0|1|
#       //= and \\= are comment blocks
#       At a line end, if ; exists, goes into the next line
#       Team organization via $T$ <name> [display name]: -- NOT DONE YET
#       color blue,
#       friendlyfire false

import textwrap

fileNameOriginal = '2O_CBP.txt'
fileNameTemp = '2T_CBP.txt'
fileNameFinal = '2F_CBP.txt'

def copy_file(a, b):
    '''Copies file a to b'''
    readFile1 = open(a, 'r')
    readFile2 = open(b, 'w')
    fileMessage = readFile1.read()
    readFile2.write(fileMessage)
    readFile1.close()
    readFile2.close()

def replace_function(fileName,replace1,replace2):
    readTempFileRepeat = open(fileName, 'r+')
    fileTempEdit = readTempFileRepeat.read()
    open(fileName, 'w').close()
    fileEdit = fileTempEdit.replace(replace1, replace2)
    open(fileName, 'w').write(fileEdit)
    readTempFileRepeat.close()

copy_file(fileNameOriginal, fileNameTemp)
replace_function(fileNameTemp,'||','|')

#   Prepping files for ; with skipping lines
readNewFile = open(fileNameFinal, 'w')
readTempFile = open(fileNameTemp, 'r+')
fileSplit = readTempFile.read().split('\n')

skipLine = 0
rewriteLine = ''

for s in fileSplit:
    if skipLine == 1:
        if s[-1:] == ';':
            readNewFile.write(textwrap.dedent(s[:-1]))
        else:
            readNewFile.write(textwrap.dedent(s))
            readNewFile.write('\n')
            skipLine = 0
    else:
        if s[-1:] == ';':
            readNewFile.write(s[:-1])
            skipLine = 1
        else:
            readNewFile.write(s)
            readNewFile.write('\n')

readTempFile.close()
readNewFile.close()

#   Prepping files for comment blocks via //= and \\=
copy_file(fileNameFinal, fileNameTemp)
readNewFile = open(fileNameFinal, 'w')
readTempFile = open(fileNameTemp, 'r+')
fileSplit = readTempFile.read().split('\n')

commentBlock = 0

for s in fileSplit:
    if s[:3] == '//=':
        commentBlock = 1
    if commentBlock == 1:
        readNewFile.write('/// ')
        if s[:3] == '\\\\=':
            commentBlock = 0
    readNewFile.write(s)
    readNewFile.write('\n')

readTempFile.close()
readNewFile.close()
