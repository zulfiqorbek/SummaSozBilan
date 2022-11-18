# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 05:26:48 2022

@author: Zulfiqor
"""

def onlik_yuzlik(summa):
  raqamSozga = {  
    0: "",  
    1: " bir",  
    2: " ikki",
    3: " uch",
    4: " to'rt",
    5: " besh",
    6: " olti",
    7: " yetti",
    8: " sakkiz",
    9: " to'qqiz",
    10: "o'n",
    20: "yigirma",
    30: "o'ttiz",
    40: "qirq",
    50: "ellik",
    60: "oltmish",
    70: "yetmish",
    80: "sakson",
    90: "to'qson",
    100: "yuz"
  }
  natija = ""
  sanoqchi = 1
  while summa > 0:
    n = summa % 10 
    if sanoqchi < 100:
      natija = raqamSozga[n * sanoqchi] + "" + natija
    else:
      natija = raqamSozga[n] + " " + raqamSozga[sanoqchi] + " " + natija
    summa //= 10
    sanoqchi *= 10
  return natija
  
def SummaSozBilan(summa):
  ming_mln_lion = ["", " ming", " million ", " milliard ", " trillion ", " kvadrilon "]
  natija = ""
  index = 0
  
  while summa > 0:
    qoldiq = summa % 1000
    if qoldiq != 0:
        natija = onlik_yuzlik(qoldiq) + ming_mln_lion[index] + natija
    summa //= 1000
    index += 1
  
  return natija

summa = int(input("Raqamingizni kiriting: "))

print(SummaSozBilan(summa))