# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 21:18:55 2017

@author: Vlad
"""
import music_analyser as ma

def main():
    music =  "E:\Музыка".replace("\\","/")
    
    #useng length() to create tuple with lists of length files of different formats
    length = ma.length(music)
    
    #some histograms
    ma.sub_plot(length)
    
    #stacked histogram
    ma.stacked_plot(length)


if __name__ == "__main__":
    main()
          


