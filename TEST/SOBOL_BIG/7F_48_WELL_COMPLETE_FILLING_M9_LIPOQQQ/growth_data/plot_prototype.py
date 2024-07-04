#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import itertools
import numpy as np
import pickle as pkl
import os
get_ipython().run_line_magic('matplotlib', 'inline')


# In[146]:


for i in os.listdir():
    if "well_position" in i:
        print(i[-13:-4])


# In[10]:


df2=pd.read_excel("Ricardo_14_10_22_Bacillus_Iter_2_v2.xlsx")


# In[11]:


df2


# In[12]:


closed=df2.drop(list(range(0,35))+list(range(133,138)),axis=0)


# In[13]:


closed_2=closed.iloc[:,0:217]


# In[14]:


closed_3=closed_2.transpose().reset_index(drop=True)


# In[15]:


closed_3.columns=closed_3.iloc[0,:]


# In[16]:


closed_3=closed_3.drop(0,axis=0)


# In[17]:


closed_3


# In[18]:


wells=closed_3.columns.values[2:]


# In[ ]:





# In[19]:


labels=pd.read_csv("well_position_iter_2_v2.csv")


# In[20]:


names1=labels["name"].apply(lambda x: x.split("_")[0]+"-M9" if (("Ref" in x) or ("Control" in x)) else x.split('_')[0]+"."+x.split('_')[1]+"%C-"+x.split('_')[2]+"mM N")


# In[21]:


well1=labels["Position"].apply(lambda x: x[1:])


# In[22]:


tmpdict=dict(zip(well1,names1))


# In[23]:


sobri=list(set(wells)-set(well1))


# In[24]:


sorted(sobri)


# In[25]:


for i in sobri:
    tmpdict[i]="water"


# In[26]:


dictio=tmpdict


# In[27]:


closed_3["Time [h]"]=closed_3["Time [s]"]/3600


# In[ ]:





# In[28]:


closed_4=closed_3[["Time [h]"]+list(closed_3.columns)[1:-1]]


# In[29]:


df3=closed_4.drop(["Temp. [°C]"],axis=1)


# In[30]:


df3


# In[ ]:





# In[31]:


#df3["G4"]=pd.Series([df3['B3'].mean(),df3['C6'].mean(),df3['B3'].mean(),df3['G5'].mean(),df3['D9'].mean(),df3['D9'].mean()]).mean()


# In[ ]:





# In[32]:


controls=labels.loc[labels["name"].apply(lambda x: "Control" in x)]


# In[33]:


controls


# In[34]:


orco=['Control_M9_no_bacteria_1',
 'Control_M9_no_bacteria_4',
 'Control_M9_no_bacteria_2',
 'Control_M9_no_bacteria_5',
 'Control_M9_no_bacteria_3',
 'Control_M9_no_bacteria_6']


# In[35]:


q=pd.DataFrame({"name":orco})


# In[36]:


q2=q.merge(controls,on="name")


# In[37]:


control_list=q2["Position"].apply(lambda x: x[1:])


# In[38]:


control_list


# In[39]:


from functools import reduce


# In[40]:


blockcontrol=reduce(lambda x,y: x+y,[[i]*9 for i in control_list])


# In[41]:


for i in controls["Position"]:
    print(df3[i[1:]].mean())


# In[42]:


control_list


# In[43]:


letters=[["B","C","D"],["E","F","G"]]
numbers=[["2","3","4"],["5","6","7"],["8","9","10"]]
byblock=list(itertools.chain.from_iterable([list(itertools.chain.from_iterable([list(itertools.chain.from_iterable([[j+i for i in in2] for j in in1])) 
                                     for in1 in letters])) for in2 in numbers]))
#blockcontrol=["B3"]*9+["E2"]*9+["D7"]*9+["F6"]*9+["B9"]*9+["F9"]*9   #1_4_2_5_3_6
controlwell=dict(zip(byblock,blockcontrol))
for i in df3.columns:
    if i in list(controlwell.keys()):
        df3[i]=df3[i]-df3[controlwell[i]]


# In[44]:


controlwell


# In[45]:


df4=pd.melt(df3,id_vars="Time [h]",value_name='OD',var_name="Position")


# In[46]:


df4["Time [h]"]=pd.to_numeric(df4["Time [h]"])
df4["OD"]=pd.to_numeric(df4["OD"])


# In[ ]:





# In[ ]:





# In[47]:


df4["Experiment"]=df4['Position'].apply(lambda x: dictio[x])


# In[48]:


df4.loc[df4["Experiment"]=="Reference-M9"]


# In[ ]:





# In[49]:


df4=df4.loc[df4["Experiment"]!="water"].copy()


# In[50]:


df4


# In[51]:


#repdict={"0":"0 mM","Reference":"M9/18.7 mM","40":"40 mM","80":"80 mM","120":"120 mM","160":"160 mM","200":"200 mM","240":"240 mM","Control":"M9/Control"}


# In[52]:


#df4["Experiment"]=df4["Experiment"].apply(lambda x: repdict[x])


# In[53]:


#df4.loc[df4["Experiment"]=="M9/18.7 mM"]


# In[54]:


list(pd.unique(df4["Experiment"]))


# In[55]:


#df5=df4.loc[(df4["Time [h]"]/0.669722)%1<=0.1]


# In[56]:


#df5
#hexi=["#ff0000","#ff8000","#ffff00","#00ff00","#00ff80","#00ffff","#0000ff","#8000ff","#ff00ff"]
#ordi=["0 mM","M9/18.7 mM","40 mM","80 mM","120 mM","160 mM","200 mM","240 mM","M9/Control"]
'''
ordi=['6.00%C-240mM N',
 'Control-M9',
 '1.81%C-113mM N',
 '6.00%C-0mM N',
 '2.40%C-0mM N',
 '4.38%C-0mM N',
 'Reference-M9',
 '6.00%C-37mM N',
 '0.00%C-180mM N']

ordi=['4.71%C-188mM N',
 '2.14%C-222mM N',
 '3.85%C-17mM N',
 'Reference-M9',
 '3.0%C-154mM N',
 'Control-M9',
 '0.43%C-120mM N',
 '1.28%C-51mM N',
 '5.57%C-85mM N']
'''
ordi=list(pd.unique(df4["Experiment"]))
#coldic=dict(zip(ordi,hexi))


# In[57]:


from random import shuffle


# sam=list(sns.color_palette("tab10")[0:9])
# shuffle(sam)

# In[58]:


sam=[(0.17254901960784313, 0.6274509803921569, 0.17254901960784313),
 (0.5803921568627451, 0.403921568627451, 0.7411764705882353),
 (0.7372549019607844, 0.7411764705882353, 0.13333333333333333),
 (0.4980392156862745, 0.4980392156862745, 0.4980392156862745),
 (1.0, 0.4980392156862745, 0.054901960784313725),
 (0.8901960784313725, 0.4666666666666667, 0.7607843137254902),
 (0.12156862745098039, 0.4666666666666667, 0.7058823529411765),
 (0.5490196078431373, 0.33725490196078434, 0.29411764705882354),
 (0.8392156862745098, 0.15294117647058825, 0.1568627450980392)]


# In[59]:


coldic=dict(zip(ordi,sam))


# In[60]:


#with open("13_Oct_iter1_v2_coldic.pkl","rb") as f:
#    coldic=pkl.load(f)


# In[61]:


#coldic


# #new_ord=["240 mM","200 mM","160 mM","120 mM","80 mM","40 mM","M9/18.7 mM","0 mM","M9/Control"]
# new_ord=['4.71%C-188mM N',
#  '2.14%C-222mM N',
#  '3.85%C-17mM N',
#  '3.0%C-154mM N',
#  '0.43%C-120mM N',
#  '1.28%C-51mM N',
#  '5.57%C-85mM N','Control-M9', 'Reference-M9']

# #new_ord_2=["240 mM","200 mM","160 mM","120 mM","80 mM","40 mM","M9/18.7 mM","0 mM"]
# new_ord_2=['4.71%C-188mM N',
#  '2.14%C-222mM N',
#  '3.85%C-17mM N',
#  '3.0%C-154mM N',
#  '0.43%C-120mM N',
#  '1.28%C-51mM N',
#  '5.57%C-85mM N', 'Reference','Control']

# In[62]:


#examinating cv
df4


# condition="120 mM"

# cv=df4.loc[df4["Experiment"]==condition].groupby("Time [h]").std()/df4.loc[df4["Experiment"]==condition].groupby("Time [h]").mean()

# cv=cv.reset_index()

# cv

# av_cv=cv[cv["Time [h]"]>10]["OD"].mean()*100

# av_cv

# av_cv_total=cv["OD"].mean()*100

# av_cv_total

# means=[]
# for condition in new_ord_2:
#     cv=df4.loc[df4["Experiment"]==condition].groupby("Time [h]").std()/df4.loc[df4["Experiment"]==condition].groupby("Time [h]").mean()
#     cv=cv.reset_index()
#     av_cv=cv[cv["Time [h]"]>10]["OD"].mean()*100
#     means.append(av_cv)

# np.mean(means)

# sns.lineplot(x='Time [h]', y='OD', data=cv)

# In[201]:


#--------------------------------------------------------


# In[203]:


plt.figure(figsize=(20,16))
b=sns.lineplot(x='Time [h]', y='OD', data=df4, hue='Experiment',ci=95,palette=coldic,hue_order=list(coldic.keys())) #hue_order=new_ord #palette=colors, legend=False
plt.legend(title="$Combination$",loc=2, prop={'size': 11})
plt.xlabel('Time (h)', fontsize=16)
plt.ylabel('OD', fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlim(0,36)
plt.ylim(0,0.8)
b.tick_params(labelsize=30)
b.set_xlabel("Time (h)",fontsize=30)
b.set_ylabel("OD$_{600}$",fontsize=30)
plt.setp(b.get_legend().get_texts(), fontsize='20')
plt.setp(b.get_legend().get_title(), fontsize='20') 

plt.savefig("iter_2_v2_growth_curve.pdf",bbox_inches="tight")


# In[130]:


#----------------------------------------------------------------------------------------------------------


# In[63]:


df4


# In[64]:


#extraer puntos especificos


# In[65]:


df5=df4.drop("Position",axis=1)


# In[ ]:





# In[66]:


mean_df=df5.groupby(["Time [h]","Experiment"]).mean().reset_index()
mean_df=mean_df.rename({"OD":"mean"},axis=1)


# In[67]:


sem_df=df5.groupby(["Time [h]","Experiment"]).sem().reset_index()
sem_df=sem_df.rename({"OD":"sem"},axis=1)


# In[68]:


maxval=[]
for i in pd.unique(mean_df["Experiment"]):
    tmp=mean_df[mean_df["Experiment"]==i].copy()
    tmpma=tmp["mean"].idxmax()
    maxrow=tmp.loc[tmp["mean"].idxmax()].copy() 
    maxsem=sem_df.loc[(sem_df["Time [h]"]==maxrow["Time [h]"]) & (sem_df["Experiment"]==i)].copy()
    maxsem["mean"]=maxrow["mean"]
    maxval.append(maxsem)


# In[ ]:





# In[70]:


maxtable=reduce(lambda x,y:pd.concat([x,y]),maxval)


# In[110]:


sof=[]
for time,maine in zip(maxtable["Time [h]"],maxtable["Experiment"]):
    eri=df5.loc[(df5["Time [h]"]==time) & (df5["Experiment"]==maine) ]
    sof.append(eri)
newmax=reduce(lambda x,y:pd.concat([x,y]),sof)
newmax2=newmax.drop("Time [h]",axis=1)
newmax3=newmax2.groupby("Experiment").mean().reset_index()
refmean=newmax3.loc[newmax3["Experiment"]=="Reference-M9"]["OD"].values[0]
newmax2["OD"]=newmax2["OD"]/refmean

mean_df=newmax2.groupby(["Experiment"]).mean().reset_index()
mean_df=mean_df.rename({"OD":"mean"},axis=1)

sem_df=newmax2.groupby(["Experiment"]).sem().reset_index()
sem_df=sem_df.rename({"OD":"sem"},axis=1)

maxtable=mean_df.merge(sem_df)


# In[ ]:





# In[211]:


#lastmean=mean_df[mean_df["Time [h]"].apply(lambda x: int(x))==36]
#lastsem=sem_df[sem_df["Time [h]"].apply(lambda x: int(x))==36]


# In[ ]:





# In[212]:


#lasttable=lastmean.merge(lastsem)


# In[140]:


lastal=df5[df5["Time [h]"].apply(lambda x: int(x))==36].drop("Time [h]",axis=1)
lastal2=lastal.groupby("Experiment").mean().reset_index()
reflas=lastal2.loc[lastal2["Experiment"]=="Reference-M9"]["OD"].values[0]
lastal["OD"]=lastal["OD"]/reflas
lastmean=lastal.groupby(["Experiment"]).mean().reset_index()
lastmean=lastmean.rename({"OD":"mean"},axis=1)

lastsem=lastal.groupby(["Experiment"]).sem().reset_index()
lastsem=lastsem.rename({"OD":"sem"},axis=1)
lasttable=lastmean.merge(lastsem)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[213]:


maxtable2=maxtable[["Experiment","mean","sem"]].copy()


# In[214]:


lasttable2=lasttable[["Experiment","mean","sem"]].copy()


# In[215]:


maxtable2.to_csv("iter_2_v2_max_table.csv",index=False)


# In[216]:


lasttable2.to_csv("iter_2_v2_last_table.csv",index=False)


# In[217]:


lasttable2


# In[ ]:





# In[ ]:


#-----------------------------------------------------------------------------------


# In[134]:


condi=['4.71%C-188mM N',
     '2.14%C-222mM N',
     '3.85%C-17mM N',
     '3.0%C-154mM N',
    '0.43%C-120mM N',
     '1.28%C-51mM N',
     '5.57%C-85mM N', 'Reference','Control']
for iki in condi:    
    df5=df4.loc[df4["Experiment"]==iki]
    #new_ord_2=
    plt.figure(figsize=(20,16))
    sns.lineplot(x='Time [h]', y='OD', data=df5, hue='Experiment',ci=95,palette=coldic,hue_order=new_ord) #palette=colors, legend=False
    plt.legend(title="$Combination$",loc=2, prop={'size': 11})
    plt.xlabel('Time (h)', fontsize=16)
    plt.ylabel('OD', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlim(0,36)
    plt.ylim(0,0.75)

    plt.savefig("bacillus_iter_0_36hr_0_14_09_22_"+iki+".pdf",bbox_inches="tight")
    plt.close()


# In[37]:


df4.dtypes


# In[55]:


fig = px.line(df4,x='Time [h]', y='OD', color='Experiment')
fig.show()


# In[56]:


df4.to_csv("bacillus_nitrogen_for_drawing.csv",index=False)


# In[62]:


df6=df4.loc[df4["Experiment"]=="0"]


# In[87]:


fg = sns.FacetGrid(data=df4, hue='Experiment', palette=list(sns.color_palette()),height=10,aspect=1)
fg.map(plt.scatter, 'Time [h]', 'OD',s=20)
fg.set_axis_labels("Time [h]", "OD")
#fg.set_titles(row_template='Bacillus subtilis in microplates, 200ul volume')
plt.legend(title='Treatment/Control')
#plt.title("Bacillus subtilis in microplates, 200ul volume, 2x M9 minimal medium, all points")
plt.savefig("bacillus_subtilis_nitrogen_points.svg",bbox_inches="tight",dpi=300)
#for i in range(1,9):
#    vari="cat"+str(i)
#    plt.fill_between(eval(vari)['hours'],eval(vari)['mean'] - eval(vari)['interval'], eval(vari)['mean'] + eval(vari)['interval'], color=list(sns.color_palette())[i-1],alpha=0.2)
#plt.savefig("bacillus_subtilis_microplates_28Sep2021.jpg",bbox_inches="tight",dpi=300)
#plt.xlabel('Time (h)')
#plt.ylabel('OD')


# In[ ]:




