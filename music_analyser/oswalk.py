# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 21:18:55 2017

@author: Vlad
"""

import os
import matplotlib.pyplot as plt
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from mutagen.flac import FLAC
music =  "E:\Музыка".replace("\\","/")



def length(music):
    length_mp3 = []
    length_mp4 = []
    length_flac = []
    for root, dirs, files in os.walk(music):
        for fname in files:
            name = root + '/' + fname
            if name[-3:].lower() == "mp3":
                audio = MP3(name)
                length_mp3.append(audio.info.length / 60)
            if name[-3:].lower() == "m4a" or name[-3:].lower() == "m4a" :
                audio = MP4(name)
                length_mp4.append(audio.info.length / 60)
            if name[-4:].lower() == "flac":
                audio = FLAC(name)
                length_flac.append(audio.info.length / 60)
    return (("MP3","MP4","FLAC"),(length_mp3,length_mp4,length_flac))


length = length(music)

def sub_plot(length):
    plt.clf()
    """Take tuple and for each element create figure of different colors"""
    colors = ["blue","red","green","orange"]
    names = length[0]
    count = length[1]
    
    # create list of boolean , where true is empty list 
    not_empty_count = 0
    isempty = []
    for i in range(len(count)):
        if len(count[i]) == 0:
            isempty.append(True)
        else:
            not_empty_count += 1
            isempty.append(False)
    
    #all iterations
    if not_empty_count != 0:
        a = 1
        for i in range(len(count)):
            #counter for beautiful subbplotting
            
            
            if not isempty[i]:
                plt.subplot(not_empty_count*2,1,a*2)
                a += 1
               
                #define range
                if max(count[i]) > 10:
                    rng = (0, 10)
                else:
                    rng = (0,int(max(count[i])+1))
                
                #plot
                
                plt.grid(True)
                plt.title(names[i], size = "small")
                plt.xlabel('Length (in min)')
                plt.ylabel('Number of songs')
                plt.hist(count[i],bins = rng[1]*10, range = rng, color = colors[i], label = str(len(count[i])))
                plt.legend()
            
        plt.savefig('plots.png', dpi = 600)
        plt.show()
        plt.close()


def stacked_plot(length):
    plt.clf()
    colors_set = ["blue","red","green","yellow","orange"]
    names = length[0]
    count = length[1]
    colors = colors_set[:len(names)]
   
    
    #define range
    rng = (0, 10) 
    
    #counts total number of songs
    total = 0
    for i in range(len(length[1])):
        total += len(length[1][i])
        
    #plot
    plt.grid(True)
    plt.xlabel('Length (in min)')
    plt.ylabel('Number of songs.   Total:  ' + str(total))
    
    label = length[0]
    
    plt.hist(count,bins = rng[1]*10, range = rng, color = colors, stacked = True, label = label)
    plt.legend()
    plt.savefig('stacked_plot.png', dpi = 600)
    plt.show() 
    plt.close()



sub_plot(length)
stacked_plot(length)


          


