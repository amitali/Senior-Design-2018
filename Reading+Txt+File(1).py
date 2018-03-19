
# coding: utf-8

# In[134]:

cd Desktop


# In[135]:

file = open("Modified_Data.txt")


# In[136]:

for i in range(1):
    s = file.readline()

print(s)


# In[14]:

for line in range(1):
    words = s.split("|")
    for i in range(len(words)):
        print(words[i])
print("Done!")        


# In[27]:

import os


# In[28]:

import urllib.request


# In[30]:

pwd


# In[32]:

url = 'https://hnevtimg.blob.core.windows.net/vehicle/1ea515ca-1c86-483c-94bf-9eac77b54a38.jpg'
file = os.path.join(C:/Users/manas/Desktop, "tested image.jpeg")
urllib.request.urlretrieve(url,file)


# In[143]:

import webbrowser
webbrowser.open_new(words[3])


# In[ ]:


r = requests.get(url, allow_redirects=True)
open('tested image', 'w').write(r.content)


# In[ ]:





# In[ ]:




# In[60]:

s = file.read(6)
print(s)

new = open("write.txt", "w+")




# In[ ]:




# In[61]:

new.write(s)
#new.close()


# In[62]:

new = open("write.txt", "r")
print(new.read(5))


# In[ ]:



