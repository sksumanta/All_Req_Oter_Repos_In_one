import pandas as pd
import numpy as np

left_df = pd.DataFrame({'id' : [1,2,3,4] , 'name':['hb','ss','sk','uk'] , 'sub' : ['p1','p2','p4','p5']})
right_df = pd.DataFrame({'id' : [1,2,3,4] , 'name':['rk','ms','rs','cs'] , 'sub' : ['p1','p2','p3','p4']})

print("The data frame left_df \n", left_df ," \n and the right_df is \n", right_df)


print(pd.merge(left_df,right_df,on='sub'))


