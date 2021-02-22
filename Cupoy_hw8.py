
# coding: utf-8

# $題目：$
# 
# 
# 
# $name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']$
# 
# $sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']$
# 
# $weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]$
# 
# $rank_list = [8,1,5,4,7,6,2,3]$
# 
# $myopia_list = [True,True,False,False,True,True,False,False]$
# 
# 

# 
# $ 1.將上列 list 依照['name', 'sex', 'weight', 'rank', 'myopia']順序擺入 array，並且資料型態順序擺入[Unicode,Unicode,float,int,boolean]$
# 

# In[34]:


import numpy as np

name_list = np.array(['小明','小華','小菁','小美','小張','John','Mark','Tom'])
sex_list = np.array(['boy','boy','girl','girl','boy','boy','boy','boy'])
weight_list = np.array([67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7])
rank_list = np.array([8,1,5,4,7,6,2,3])
myopia_list = np.array([True,True,False,False,True,True,False,False])


# In[31]:


# 使用字母代表的資料型別
dt = np.dtype({'names':('name', 'sex', 'weight', 'rank', 'myopia'), 
               'formats':('U5','U5','f8', int, bool)})


# In[32]:


D = np.zeros(8, dtype=dt)
D


# In[37]:


D['name'] = name_list
D['sex'] = sex_list
D['weight'] = weight_list
D['rank'] = rank_list
D['myopia'] = myopia_list


# In[38]:


print(D)


# $2.呈上題，將 array 中體重(weight)數據集取出算出全部平均體重$

# In[39]:


D_rec = D.view(np.recarray)
D_rec


# In[41]:


print("全部平均體重為:", np.mean(D_rec.weight))


# $3.呈上題，進一步算出男生(sex 欄位是 boy)平均體重、女生(sex 欄位是 girl)平均體重$

# In[44]:


b = np.where(D['sex']=='boy')
Bweight=np.average( D[b]['weight'] )
print('男生平均體重', Bweight)


# In[46]:



g = np.where(D['sex']=='girl')
Gweight=np.average( D[g]['weight'] )
print('女生平均體重', Gweight)

