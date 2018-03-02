
# coding: utf-8

# In[77]:

pwd


# In[26]:

cd Desktop


# In[64]:

file = open("Modified_Data.txt")


# In[70]:

for i in range(1):
    s = file.readline()
print (7+9)

print(s)


# In[76]:

for line in range(1):
    words = s.split("|")
    s1 = words(1)
    print (s1)
    print (words)


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



