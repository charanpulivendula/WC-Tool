import sys
import os.path

if len(sys.argv)<=1:
    print("input the file")
    exit(1)

def parseFile():
    try:
        file = open(sys.argv[1],'r')
        flags = set(sys.argv[2:])
        #Reading file in chunks
        byteCounter = 0
        wordCounter = 0
        charCounter = 0
        lineCounter = 0

        def readFileInChunks(file, fileSize = 1024):
            while chunk:= file.read(fileSize):
                yield chunk

        def ByteCount(data):
            return len(data.encode("utf-8"))

        def WordCount(data):
            return len(data.split())

        def CharCount(data):
            return len(data)
        
        def LineCount(data):
            return len(data.split("\n"))
        
        def InfoPrinter(flags):
            if not flags or '-all' in flags:
                print(f"Bytes: {byteCounter}")
                print(f"Words: {wordCounter}")
                print(f"Characters: {charCounter}")
                print(f"Lines: {lineCounter}")
                
            else:
                if '-b' in flags:
                    print(f"Bytes: {byteCounter}")
                if '-w' in flags:
                    print(f"Words: {wordCounter}")
                if '-c' in flags:
                    print(f"Characters: {charCounter}")
                if "-l" in flags:
                    print(f"Lines: {lineCounter}")

        chunk = readFileInChunks(file)

        for chunk in readFileInChunks(file):
            byteCounter += ByteCount(chunk)
            wordCounter += WordCount(chunk)
            charCounter += CharCount(chunk)
            lineCounter += LineCount(chunk)

        InfoPrinter(flags)
        file.close()
        exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parseFile()
        


    