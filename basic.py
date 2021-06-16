#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Hello World')


# In[3]:


the_world_is_flat = True
if the_world_is_flat :
    
    print ("Hello World")


# In[4]:


x = 5  #number


# In[5]:


print (x)


# In[6]:


y = "Arwy" #string


# In[7]:


print(y)


# In[8]:


x,y,z = "Orange","Apple", "Cherry"
print(y)


# In[9]:


x=y=z ="Data"
print(y)


# In[12]:


#Function
x = 12
def myfunc():
    
    print(x+ "this is the Value Of X")
    myfunc()


# In[13]:


print(x)


# In[24]:


## Multiply Function
def multiplyFunc(x):
    print(x)
    
    


# In[28]:


def passing_data(x):
    print("x"+x)


# In[29]:


passing_data('x')


# In[30]:


# Numbers 

x = 35e3
y = 12E4
z=-8726.7e12
print(type(x))
print(type(y))
print(type(z))


# In[31]:


#Casting
x = int(1) #should Be 1
y=int(2.8)#should be 2
z=int("3") #should Be 3
print(x,y,z,"Print")


# In[32]:


#String Array

a = "Hello, World"
print(a[0])


# In[34]:


print (a)


# In[44]:


for i in "Banana":
    print (i)


# In[45]:


for i in a :
    print (i)


# In[47]:


#modify String
a = "Hello World"
print(a.upper())
print (a.lower())
print(a.strip())
print(a.replace("H","J"))
print(a.split(","))


# In[48]:


a = "Hello"
b = "World"
c = a + " " + b
print(c)

age = 36
txt = "My Name Is John, and I am {}"  #Insert Numbers into Strings
print(txt.format(age))


# In[49]:


quantity = 3
item_no = 567
price = 49.95
myOrder = "I want to pay {2} dollars for {0} places of item {1}"
print (myOrder.format(quantity,item_no,price))


# In[50]:


txt = "We are the so-called \"Viking\" from north."
print(txt)


# In[53]:


x = "Hello World"
print(len(x))


# In[54]:


print(10<9)


# In[55]:


this_list = ["apple","banana","cherry"]
print(this_list)


# In[ ]:


newTupple = ("DataA","DataB","Data C")

