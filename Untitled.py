#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True:
    n = int(input()) 
    if 1900<=n<=3000:
        if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
            print("Високосный")
        else:
            print("Обычный")   
    else:
        print("Введите год с 1900 по 3000")


# In[ ]:




