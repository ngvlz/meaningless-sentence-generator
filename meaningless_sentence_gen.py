import random
import urllib.request
import urllib.error
import os


def getPath():
    try:
        while True:
            path = input('Enter the specific path to the desired directory: ')
            if os.path.isdir(path):
                return path
            else:
                print('Please enter a valid path')
    except Exception as exc:
        print(f'{exc} error has occured, try again!')
        getPath()


def generateStrFileFolder(path, num, extension, length):
    # random string
    # source: https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain
    txtFile = urllib.request.urlopen(
        'https://raw.githubusercontent.com/ngvlz/folder_file_sentence_generator/main/words.txt')
    txtData = txtFile.read().decode()
    words = txtData.splitlines()
    # write output
    os.chdir(path)
    folder = f'folder_{num}'
    file = f'file_{num}'
    folderPath = os.path.join(path, folder)
    if not os.path.exists(folderPath):
        os.mkdir(folder)
    with open(f'{folder}\{file}.{extension}', 'a+') as fileData:
        counter = 0
        while True:
            result_str = ' '.join(random.choice(words)
                                  for i in range(length))
            if counter < 11:
                fileData.write(result_str + '\n')
                counter = counter + 1
            else:
                break
    print(f'{folder}, {file}.{extension}, and string generated')


path = getPath()
for num in range(1, 10):
    length = random.randint(1, 20)
    generateStrFileFolder(path, num, 'txt', length)
