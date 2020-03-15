#!/usr/bin/env python
# coding: utf-8

# In[13]:


import os
import numpy as np
from os.path import isfile, join
wav=[]
mypath = "..\\data"
for dirname, dirnames, filenames in os.walk(mypath+"\\wav"):
    # print path to all filenames.
    for filename in filenames:
        wav.append(os.path.join(dirname, filename))
  


# In[14]:


#print(wav)
wav[0]


# In[15]:


Path="..\\data\\f_list"
wavlist = os.path.join(Path, "wav_list.txt")  
with open(wavlist, 'w') as filehandle:
    for listitem in wav:
        filehandle.write('%s\n' % listitem)


# In[16]:


lbl=[]
mypath = "..\\data\\lbl"
for dirname, dirnames, filenames in os.walk(mypath):
    # print path to all filenames.
    for filename in filenames:
        lbl.append(os.path.join(dirname, filename))


# In[17]:


#print(lbl)
lbl[0]


# In[18]:


Path="..\\data\\f_list"
lbllist = os.path.join(Path, "lbl_list.txt")  
with open(lbllist, 'w') as filehandle:
    for listitem in lbl:
        filehandle.write('%s\n' % listitem)


# In[ ]:





# In[10]:


mfc=[]
mypath = "..\\data"
for dirname, dirnames, filenames in os.walk(mypath+"\\mfcc"):
    # print path to all filenames.
    for filename in filenames:
        mfc.append(os.path.join(dirname, filename))


# In[13]:


mfc = np.array(mfc)
#print(mfc)
mfc[0]


# In[12]:


Path="..\\data\\f_list"
mfcclist = os.path.join(Path, "mfcc_list.txt")  
with open(mfcclist, 'w') as filehandle:
    for listitem in mfc:
        filehandle.write('%s\n' % listitem)


# In[15]:


seg=[]
mypath = "..\\data"
for dirname, dirnames, filenames in os.walk(mypath+"\\seg"):
    # print path to all filenames.
    for filename in filenames:
        seg.append(os.path.join(dirname, filename))


# In[16]:


seg = np.array(seg)
seg[0]


# In[18]:


Path="..\\data\\f_list"
seglist = os.path.join(Path, "seg_list.txt")  
with open(seglist, 'w') as filehandle:
    for listitem in seg:
        filehandle.write('%s\n' % listitem)


# In[ ]:




