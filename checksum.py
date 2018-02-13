import hashlib, os

ubuntuDict = {'560df9005d3bc355bf3239cd8a18f744': 'Ubuntu 17.10', '0d9fe8e1ea408a5895cbbe3431989295': 'Ubuntu 16.10'}
kaliDict = {'545adb675c5982de2bb69a04d1663342b534164e': 'Kali Light 2017', 'ed88466834ceeba65f426235ec191fb3580f71d50364ac5131daec1bf976b317': 'Kali 64 Bit', 'b541a78a063b6385365ac00248631c4a18c92b8c4e3618db0b1bf751b495149f': 'Kali 32 Bit'}

for root, dirs, files in os.walk('/home/stephen/Downloads/'):
    for isoFile in files:
        if isoFile is None:
            print("There are no isos in your current directory")
        elif isoFile.endswith('.iso'):
            print(isoFile)

print("Enter path of iso: ")

file = input()

if 'ubuntu'.lower() in file:
    def md5Checksum(filePath):
        with open(filePath, 'rb') as fh:
            md5 = hashlib.md5()
            while True:
                data = fh.read(8192)
                if not data:
                    break
                md5.update(data)
            return md5.hexdigest()

    print('The MD5 checksum of your file is', md5Checksum(file))


    if md5Checksum(file) in ubuntuDict:
        print("Your " + ubuntuDict[md5Checksum(file)] + " iso is valid!")
    else:
        print("Warning: this checksum is not in our database!")

if 'kali'.lower() in file:
    def shaChecksum(filePath):
        with open(filePath, 'rb') as fh:
            sha = hashlib.sha1()
            while True:
                data = fh.read(8192)
                if not data:
                    break
                sha.update(data)
            return sha.hexdigest()
    print('The sha256 checksum of your iso is', shaChecksum(file))

    if shaChecksum(file) in kaliDict:
        print("Your " + kaliDict[shaChecksum(file)] + " iso is valid!")
    else:
        print("Warning: this checksum is not in our database!")