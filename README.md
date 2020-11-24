# Meaningless Sentence Generator

Meaningless Sentence Generator is a tool allowing you to:

* Create **x** folders with a file_**x**.txt in each folder respectively.

* In each file, randome words will be generated and added together to create meaningless sentences.

This works great when you want to create a bunch of randoms files with random text in them and make them a testing environment for your code!

**Current Version:** v.1.0.0

**Author**: Louis Nguyen

## Requirements

Python 3.8 and above

## Install

```bash
apt-get -y install git
git clone https://github.com/ngvlz/meaningless-sentence-generator.git
cd ./meaningless-sentence-generator
```

## Use

**Command**: `python3 meaningless-sentence-generator.py`

### Example

```bash
Enter the specific path to the desired directory: /home/ngvlz/test_environment
```

### Result

```bash
folder_1, file_1.txt, and string generated
folder_2, file_2.txt, and string generated
folder_3, file_3.txt, and string generated
folder_4, file_4.txt, and string generated
folder_5, file_5.txt, and string generated
folder_6, file_6.txt, and string generated
folder_7, file_7.txt, and string generated
folder_8, file_8.txt, and string generated
folder_9, file_9.txt, and string generated
```

## Note for Users

On line **43** in the meaningless-sentence-generator.py, change the syntax to the following:

* If you are using a LINUX machine use `f'{folder}/{file}.{extension}'`

* If you are using a WINDOWS machine use `f'{folder}\{file}.{extension}'`
