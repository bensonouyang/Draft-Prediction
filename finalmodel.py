#!/home/bensonouyang/miniconda3/bin python3.9.12
# coding: utf-8

# # Training Ordinal Regression Model

# In[1]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from statsmodels.miscmodels.ordinal_model import OrderedModel
#import sys
#print(sys.path)
#sys.path.append('/home/bensonouyang/miniconda3/bin/python')


import sys
print("User Current Version:-", sys.version)

# In[2]:


modeldf = pd.read_csv('data/modeldfcategorical.csv')


# In[3]:


#y = np.array(modeldf['DraftNumber'])
#X = np.array(modeldf.drop(columns = ['DraftNumber'], axis = 1))

y = modeldf['DraftNumber']
X = modeldf.drop(columns = ['DraftNumber'], axis = 1)


# In[4]:


newy = pd.Series([1 if x<=30 else 2 for x in modeldf['DraftNumber']])


# In[5]:


eff = (X['PTS']+ X['TRB'] + X['AST'] + X['STL'] + X['BLK'] - (X['FGA']-X['FGM']) - (X['FTA']-X['FTM']))/X['GP']


# In[6]:


eff_df = pd.DataFrame({'EFF':eff})


# In[7]:


newx = X.join(eff_df)


# In[8]:


X_train, X_test, y_train, y_test = train_test_split(X.iloc[:,0:24],y, test_size = 0.25, random_state = 42)


# In[9]:


X_train1, X_test1, y_train1, y_test1 = train_test_split(X.iloc[:,0:24],newy, test_size = 0.25, random_state = 42)


# In[10]:


# X_train2, X_test2, y_train2, y_test2 = train_test_split(newx.iloc[:,0:21].join(newx.iloc[:,45:]),newy, test_size = 0.25, random_state = 42)


# In[11]:


# https://www.statsmodels.org/dev/examples/notebooks/generated/ordinal_regression.html#examples-notebooks-generated-ordinal-regression--page-root
# https://analyticsindiamag.com/a-complete-tutorial-on-ordinal-regression-in-python/

# mod_prob = OrderedModel(y_train, X_train, distr = 'logit', hasconst= False)
# res_prob = mod_prob.fit(method = 'bfgs')
# pred = res_prob.model.predict(res_prob.params, exog = np.array(X_test))
# pred_choice = pred.argmax(1)
# print('Fraction of correct choice predictions')
# print((np.asarray(y_test) == pred_choice).mean())


# In[12]:


mod_prob1 = OrderedModel(y_train1, X_train1, distr = 'logit', hasconst= False)
res_prob1 = mod_prob1.fit(method = 'bfgs')
pred1 = res_prob1.model.predict(res_prob1.params, exog = np.array(X_test1))
pred_choice1 = pred1.argmax(1)
print('Fraction of correct choice predictions')
print((np.asarray(y_test1) == pred_choice1).mean())


# In[13]:


# mod_prob2 = OrderedModel(y_train2, X_train2, distr = 'logit', hasconst= False)
# res_prob2 = mod_prob2.fit(method = 'bfgs')
# pred2 = res_prob2.model.predict(res_prob2.params, exog = np.array(X_test2))
# pred_choice2 = pred2.argmax(1)
# print('Fraction of correct choice predictions')
# print((np.asarray(y_test2) == pred_choice2).mean())


# In[14]:


# sigX = X[res_prob1.pvalues[res_prob1.pvalues < 0.5].index]


# In[15]:


# X_train3, X_test3, y_train3, y_test3 = train_test_split(sigX,newy, test_size = 0.25, random_state = 42)


# In[16]:


# mod_prob3 = OrderedModel(y_train3, X_train3, distr = 'logit', hasconst= False)
# res_prob3 = mod_prob3.fit(method = 'bfgs')
# pred3 = res_prob3.model.predict(res_prob3.params, exog = np.array(X_test3))
# pred_choice3 = pred3.argmax(1)
# print('Fraction of correct choice predictions')
# print((np.asarray(y_test3) == pred_choice3).mean())


# # Results
# 
# With y as draft picks, and x with 0 to 24: fraction of correct choice predictions is 0.02, add 43 and 44: model fails to find the maximum of loglikelihood function
# 
# With y as rounds, and x with 0 to 24: fraction of correct choice predictions is 0.29. Fails to converge if add columns 43 and 44. 
# 
# y as rounds, x 0 to 21, and EFF: fraction = 0.25. if 0 to 24 then fails to converge.
# 
# y as rounds, x are the significant features from the second model result summary. fraction correct 0.2

# In[43]:


res_prob1.summary()


# In[ ]:




