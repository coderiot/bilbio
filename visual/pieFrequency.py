# -*- coding: utf-8 -*-

from pylab import *

freqs = open('../results/freqSubjectRules.txt')

#return list with all lines of the file
freqsLines = freqs.readlines()

#omit first line (title)
freqsLines.pop(0)

#create new list for storing tuples with the information of every line
freqsItems = []
for line in freqsLines:
    freqsItems.append(freqsLines[freqsLines.index(line)].split())


# 1st element of tuple: lable, 2nd element: value, to be plotted!
total = 0
for item in freqsItems:
    total = total + float(item[1])

item0=freqsItems[0]
item1=freqsItems[1]
item2=freqsItems[2]
item3=freqsItems[3]
item4=freqsItems[4]
item5=freqsItems[5]
item6=freqsItems[6]
item7=freqsItems[7]
item8=freqsItems[8]

#make a square figure and axes
figure(1, figsize=(7,7))
ax = axes([0.1, 0.1, 0.8, 0.8])

labels = '1', '2', '3', 'others'
fracs = [int(item0[1])/total,int(item1[1])/total,int(item2[1])/total,(int(item3[1])+int(item4[1])+int(item5[1])+int(item6[1])+int(item7[1])+int(item8[1]))/total]

explode=(0, 0, 0, 0.1)
pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow = False)
title(u'Häufigkeit der Anzahl von Themen im arxiv.org Datensatz')

show()
