import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

lines =2043057
result = pd.read_csv('/home/zft/log_iou.txt' ,error_bad_lines=False, names=['Region Avg IOU', 'Class', 'Obj', 'No Obj', '.5R','.75R','count'])
result.head()

result['Region Avg IOU']=result['Region Avg IOU'].str.split(': ').str.get(1)
result['Class']=result['Class'].str.split(': ').str.get(1)
result['Obj']=result['Obj'].str.split(': ').str.get(1)
result['No Obj']=result['No Obj'].str.split(': ').str.get(1)
result['.5R']=result['.5R'].str.split(': ').str.get(1)
result['.75R']=result['.75R'].str.split(': ').str.get(1)
result['count']=result['count'].str.split(': ').str.get(1)
result.head()
result.tail()

    

#print(result.head())
# print(result.tail())
# print(result.dtypes)
#print(result['Region Avg IOU'])

result['Region Avg IOU']=pd.to_numeric(result['Region Avg IOU'])
result['Class']=pd.to_numeric(result['Class'])
result['Obj']=pd.to_numeric(result['Obj'])
result['No Obj']=pd.to_numeric(result['No Obj'])
result['.5R']=pd.to_numeric(result['.5R'])
result['.75R']=pd.to_numeric(result['.75R'])
result['count']=pd.to_numeric(result['count'])
result.dtypes

iou_value = result['Class'].values
mean_len = 1000
iou_len = int(len(iou_value) / mean_len) * mean_len
iou_value = iou_value[0:iou_len]
reshape_iou_value = iou_value.reshape((mean_len,int(len(iou_value)/mean_len)))
iou_value_mean = np.mean(reshape_iou_value,axis=0)


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(iou_value_mean,label='Class')
#ax.plot(result['Class'].values,label='Class')
#ax.plot(result['Obj'].values,label='Obj')
#ax.plot(result['No Obj'].values,label='No Obj')
#ax.plot(result['Avg Recall'].values,label='Avg Recall')
#ax.plot(result['count'].values,label='count')
plt.ylim(0.5,1)
ax.legend(loc='best')
#ax.set_title('The Region Avg IOU curves')
ax.set_title('The Class curves')
ax.set_xlabel('batches')
#fig.savefig('Avg IOU')
fig.savefig('Class')
