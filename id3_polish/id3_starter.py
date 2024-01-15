'''
    [mst] id3_batcher.py
    mp3 tag moddyfication with regex

    gain:
    -mutagen tag and header lib usage
    -folder/file iteration and operation
    -using tinytag was unconventional

    [wip]:
    -gui?
    -usage with an argument (filename or dir path)


    log:
    -2024.01.15:    -added folder iteration
    -2021.07.12:    -initial draft
                    -used tinytag but it is a read only package so mutagen was selected instead

@author: mst
'''


from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
# import mutagen.id3
# from mutagen.id3 import ID3, TIT2, TIT3, TALB, TPE1, TRCK, TYER

import re   # renaming using regex
import os   # iterating files in folder


# compile\define manipulation patterns: here is what we actually modifying
def clean_composers (composers_str):
    clean_up = re.sub(r'\s+(?=[,;\/])',r'', composers_str)  # remove trailing spaces
    clean_up = re.sub(r'\*',r'', clean_up)                  # remove illegal characters

    clean_up = re.sub(r'([,;\/])',r';', clean_up)           # handle separators

    print(f'modifying: {composers_str=} to {clean_up=}')
    return clean_up




################## DRIVER
def main():

    # intro
    print ("[mst] mp3 tag batch script")

    # run on all .mp3 files in current dir
    # [wip] alternatively, run on a given argument as a path
    directory = '.'

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file and an mp3 one
        if os.path.isfile(f):
            if f.endswith('.mp3'):
                print(f)
                mp3file = MP3(f, ID3=EasyID3)   # load the mp3 tag object
                composer = mp3file['composer']  # composer field as a string in an array
                clean_up = clean_composers(composer[0])
                mp3file['composer'] = clean_up
                # mp3file.filename = os.path.join('modified', os.path.basename(mp3file.filename)) # to be saved in separate folder
                mp3file.save() # save modifications. this will write in-file


# insicate a running script
if __name__ == ("__main__"):
    main()
