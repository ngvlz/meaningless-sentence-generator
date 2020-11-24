import random
import urllib.request
import urllib.error
import os


# prompt for the user input, and try again until the user put in the correct URL
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
        # recursion
        getPath()


def generateStrFileFolder(path, x, extension, length):
    # create a list of words from a specific word file
    # you can also use RandomWords() from the random_words library
    # source: https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain
    txtFile = urllib.request.urlopen(
        'https://raw.githubusercontent.com/ngvlz/folder_file_sentence_generator/main/words.txt')
    txtData = txtFile.read().decode()
    words = txtData.splitlines()
    # change the working directory to *path*
    os.chdir(path)
    # set variables' names for folder_x and file_x
    folder = f'folder_{x}'
    file = f'file_{x}'
    # generate the path of the folder
    folderPath = os.path.join(path, folder)
    # if the folder path doesn't exist, create a new folder
    if not os.path.exists(folderPath):
        os.mkdir(folder)
    # open file_x in folder_x to append and read
    # LINUX file tree format uses /
    # WINDOWS file tree format uses \
    with open(f'{folder}/{file}.{extension}', 'a+') as fileData:
        counter = 0
        while True:
            # generate random meaningless sentence with a specified *length*
            result_str = ' '.join(random.choice(words)
                                  for i in range(length))
            # This defines how many lines you want to generate within a file
            # Change *11* to the number of your choice
            if counter < 11:
                fileData.write(result_str + '\n')
                counter = counter + 1
            else:
                break
    print(f'{folder}, {file}.{extension}, and string generated')


# execute getPath()
path = getPath()

# define the range of *x*
# which is how many *folder_x* (and *file_x* in them) you want to generate
# change to the range of your choice
for x in range(1, 10):
    # generate the specified *length* of your meaniless sentence
    # change to the range of your choice
    length = random.randint(1, 20)
    # execute the main function with
    # *path* from getPath()
    # randomized *x*
    # a specific *extension* of file_x / change to whatever you like
    # randomized *length*
    generateStrFileFolder(path, x, 'txt', length)
