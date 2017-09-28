# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 2017

@author: Kighn

################################
#Transliterate User Input
#-- Manjot Virdee
#
#1. Take input
#2. Convert to Upper case
#3. Change numbers to words
#4. Ignore non-alpha characters
#5. write to new_string
#
################################
"""

#in_string = 'hello Manjot! You are Number 1.'


in_string = input('Input: ')

#Initializing variables
i = 0
str = out_string = '' 
while i < len(in_string):

#    print(in_string[i])
#   print(in_string[i].upper())
    

    a_string = in_string[i].upper()

    if in_string[i] == '0':
       a_string = 'ZERO'
    elif in_string[i] == '1':
       a_string = 'ONE'
    elif in_string[i] == '2':
       a_string = 'TWO'
    elif in_string[i] == '3':
       a_string = 'THREE'
    elif in_string[i] == '4':
       a_string = 'FOUR'
    elif in_string[i] == '5':
       a_string = 'FIVE'
    elif in_string[i] == '6':
       a_string = 'SIX'
    elif in_string[i] == '7':
       a_string = 'SEVEN'
    elif in_string[i] == '8':
       a_string = 'EIGHT'
    elif in_string[i] == '9':
       a_string = 'NINE'
       

#  print(a_string)
    

    if a_string.isalnum() == True:
        out_string = out_string + a_string

   
    print(out_string)

    i+=1   
    print(i)
