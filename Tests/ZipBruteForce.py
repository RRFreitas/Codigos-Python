import zipfile

zFile = zipfile.ZipFile('test.zip')
passFile = open('dictionary.txt')
for line in passFile.readlines():
    password = line.strip('\n')
    try:
        print(password)
        zFile.extractall(pwd=password)
        print("[*] Password = " + password + '\n')
        exit(0)
    except Exception:
        print("erro")