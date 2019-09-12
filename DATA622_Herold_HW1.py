# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 20:37:50 2019
CUNY DATA 622
@author: Zachary Herold
"""

import numpy as np

#Q1 - Extracting ordered number from list, removing redundancies
def unique_index(l1, idx = 1):
    l1_sorted = sorted(np.unique(l1))
    print('The number requested is {0}'.format(l1_sorted[idx]))

#test
unique_index([2,2,2,2,3,1,1])
# gives 2

#Q2 - Anagram Check
def anagram_check(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    s1_list = [ch for ch in s1]
    s1_sorted = sorted(s1_list)
    s2_list = [ch for ch in s2]
    s2_sorted = sorted(s2_list)
    is_anagram = (s1_sorted == s2_sorted)
    print('The strings \'{0}\' and \'{1}\' are anagrams: {2}'.format(s1, s2, is_anagram))

anagram_check("cautioned", "education") #yields True
anagram_check("Cautioned", "Education") #yields True
anagram_check("caution", "educate") #yields False

