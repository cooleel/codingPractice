# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 10:16:18 2018

@author: Shanshan
"""
import sys
import time
from collections import deque 

fancy_loading = deque('>----------------------------')

while True:
    print('\r%s' % ''.join(fancy_loading))
    print(fancy_loading.rotate(1))
    sys.stdout.flush()
    time.sleep(0.08)