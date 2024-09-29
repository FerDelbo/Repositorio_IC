import os

def openAllFiles():
    files = os.listdir('./')
    files.remove('test.py')
    files.remove('test_all.py')
    return files

def testAllFiles():
    files = openAllFiles()   
    for f in files:
        print(F" !█████████████████████████████████████████████ !-!-!-! FILE {f} !-!-!-! █████████████████████████████████████████████! ")
        os.system(f"python3 test.py {f}")


if __name__ == '__main__':
    testAllFiles()
