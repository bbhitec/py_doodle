'''
 [mst] id3_starter.py 
 doodling mp3 tag reading functionality

 log:
 -2021.07.12:   -initial draft
                -used tinytag but it is a read only package so mutagen was selected instead

@author: mst
'''

#import os
#from tinytag import TinyTag, TinyTagException   # used package


from mutagen.mp3 import MP3  
from mutagen.easyid3 import EasyID3  
import mutagen.id3  
from mutagen.id3 import ID3, TIT2, TIT3, TALB, TPE1, TRCK, TYER  

#import sys
import re

################## DRIVER
def main():

    # intro
    print ("[mst] mp3 tag batch script")
   
    # build a file list from a given path and run through it
    # [wip]

    # load the mp3 tag object
    mp3file = MP3("Agnes - Release Me (Cahill Club Mix).mp3", ID3=EasyID3) 

    # extract the working fields
    composer = mp3file['composer']  # composer field as a string
    
    print(mp3file['composer'])
    #print(f'{composer=}')
    ##print(len(composer))

    # [here][wip] make this a callable
    # compile\define manipulation patterns: here is what we actually modifyung
    for each_composer in composer:

        clean_up = re.sub(r'\s+(?=[,;\/])',r'', each_composer)  # remove trailing spaces
        clean_up = re.sub(r'\*',r'', clean_up)                  # remove illegal characters

        # handle separators
        clean_up = re.sub(r'([,;\/])',r';', clean_up)           

        print(f'modifying:\n{each_composer=} to {clean_up=}')

    # substitution  
    mp3file['composer'] = [clean_up]
    mp3file.save() # save modifications. this will write in-file


# insicate a running script
if __name__ == ("__main__"):
    main() 
