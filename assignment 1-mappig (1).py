#!/usr/bin/env python
# coding: utf-8

# In[9]:





# In[ ]:



    


# In[30]:


#Starting point
s_x=1
print("x-coordinate of starting point is:",s_x)
s_y=1
print("y-coordinate of starting point is:",s_y)
f_x=7
f_y=7



for x in range (s_x,f_x+1):
     
    
    for y in range (s_y, f_y+1):
        
        if x==3 and y==2:
            print("(",x, ",",y,") =","turn left")
        elif x==3 and y==4:
            print("(",x, ",",y,") =","turn right")
        elif x==5 and y==4:
            print ("(",x, ",",y,") =","turn left")
        elif x==5 and y==5:
            print("(",x, ",",y,") =","turn right")
        elif x==6 and y==5:
            print("(",x, ",",y,") =","turn left")
        elif x==6 and y==6:
            print("(",x, ",",y,") =","turn right")
        elif x==7 and y==6:
            print("(",x, ",",y,") =","STOP")
            break
        else:
            print("(",x, ",",y,") =","go straight")
        y+=1
    x+=1
    


# In[ ]:




