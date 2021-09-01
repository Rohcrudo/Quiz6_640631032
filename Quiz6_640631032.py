# -*- coding: utf-8 -*-
"""

@author: Nattapat Tangniyom 640631032
"""

import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl
import seaborn as sns

df = pd.read_csv("Salaries.csv")
df.head()
print(df.head(10))
'''
        rank discipline  phd  service   sex  salary
0       Prof          B   56       49  Male  186960
1       Prof          A   12        6  Male   93000
2       Prof          A   23       20  Male  110515
3       Prof          A   40       31  Male  131205
4       Prof          B   20       18  Male  104800
5       Prof          A   20       20  Male  122400
6  AssocProf          A   20       17  Male   81285
7       Prof          A   18       18  Male  126300
8       Prof          A   29       19  Male   94350
9       Prof          A   51       51  Male   57800
'''
print(df.head(20))
print(df.head(50))
print(df.tail())
'''
         rank discipline  phd  service     sex  salary
73       Prof          B   18       10  Female  105450
74  AssocProf          B   19        6  Female  104542
75       Prof          B   17       17  Female  124312
76       Prof          A   28       14  Female  109954
77       Prof          A   23       15  Female  109646
'''

#Group data using rank
df_rank = df.groupby(['rank'])

#Calculate mean value for each numeric column per each group
print(df_rank.mean())
'''
                 phd    service         salary
rank                                          
AssocProf  15.076923  11.307692   91786.230769
AsstProf    5.052632   2.210526   81362.789474
Prof       27.065217  21.413043  123624.804348
'''

#Calculate mean salary for each professor rank:
print(df.groupby('rank')[['salary']].mean())
'''
                  salary
rank                    
AssocProf   91786.230769
AsstProf    81362.789474
Prof       123624.804348
'''

#Calculate mean salary for each professor rank:
print(df.groupby(['rank'], sort=False)[['salary']].mean())
'''
                  salary
rank                    
Prof       123624.804348
AssocProf   91786.230769
AsstProf    81362.789474
'''

#Calculate mean salary for each professor rank:
df_sub = df[ df['salary'] > 120000 ]
print(df_sub)
'''
    rank discipline  phd  service     sex  salary
0   Prof          B   56       49    Male  186960
3   Prof          A   40       31    Male  131205
5   Prof          A   20       20    Male  122400
7   Prof          A   18       18    Male  126300
10  Prof          B   39       33    Male  128250
11  Prof          B   23       23    Male  134778
13  Prof          B   35       33    Male  162200
14  Prof          B   25       19    Male  153750
15  Prof          B   17        3    Male  150480
19  Prof          A   29       27    Male  150500
26  Prof          A   38       19    Male  148750
27  Prof          A   45       43    Male  155865
29  Prof          B   21       20    Male  123683
31  Prof          B   22       21    Male  155750
35  Prof          B   28       23    Male  126933
36  Prof          B   45       45    Male  146856
39  Prof          B   18       18  Female  129000
40  Prof          A   39       36  Female  137000
44  Prof          B   23       19  Female  151768
45  Prof          B   25       25  Female  140096
49  Prof          B   17       18  Female  122960
51  Prof          B   20       14  Female  127512
58  Prof          B   36       26  Female  144651
72  Prof          B   24       15  Female  161101
75  Prof          B   17       17  Female  124312
'''

#Select only those rows that contain female professors:
df_f = df[ df['sex'] == 'Female' ]
print(df_f)
'''
         rank discipline  phd  service     sex  salary
39       Prof          B   18       18  Female  129000
40       Prof          A   39       36  Female  137000
41  AssocProf          A   13        8  Female   74830
42   AsstProf          B    4        2  Female   80225
43   AsstProf          B    5        0  Female   77000
44       Prof          B   23       19  Female  151768
45       Prof          B   25       25  Female  140096
46   AsstProf          B   11        3  Female   74692
47  AssocProf          B   11       11  Female  103613
48       Prof          B   17       17  Female  111512
49       Prof          B   17       18  Female  122960
50   AsstProf          B   10        5  Female   97032
51       Prof          B   20       14  Female  127512
52       Prof          A   12        0  Female  105000
53   AsstProf          A    5        3  Female   73500
54  AssocProf          A   25       22  Female   62884
55   AsstProf          A    2        0  Female   72500
56  AssocProf          A   10        8  Female   77500
57   AsstProf          A    3        1  Female   72500
58       Prof          B   36       26  Female  144651
59  AssocProf          B   12       10  Female  103994
60   AsstProf          B    3        3  Female   92000
61  AssocProf          B   13       10  Female  103750
62  AssocProf          B   14        7  Female  109650
63       Prof          A   29       27  Female   91000
64  AssocProf          A   26       24  Female   73300
65       Prof          A   36       19  Female  117555
66   AsstProf          A    7        6  Female   63100
67       Prof          A   17       11  Female   90450
68   AsstProf          A    4        2  Female   77500
69       Prof          A   28        7  Female  116450
70   AsstProf          A    8        3  Female   78500
71  AssocProf          B   12        9  Female   71065
72       Prof          B   24       15  Female  161101
73       Prof          B   18       10  Female  105450
74  AssocProf          B   19        6  Female  104542
75       Prof          B   17       17  Female  124312
76       Prof          A   28       14  Female  109954
77       Prof          A   23       15  Female  109646
'''

#Select column salary:
print(df['salary'])
'''
0     186960
1      93000
2     110515
3     131205
4     104800
       ...
73    105450
74    104542
75    124312
76    109954
77    109646
Name: salary, Length: 78, dtype: int64
'''

#Select column salary:
print(df[['rank','salary']])
'''
         rank  salary
0        Prof  186960
1        Prof   93000
2        Prof  110515
3        Prof  131205
4        Prof  104800
..        ...     ...
73       Prof  105450
74  AssocProf  104542
75       Prof  124312
76       Prof  109954
77       Prof  109646

[78 rows x 2 columns]
'''

#Select rows by their position:
print(df[10:20])
'''
        rank discipline  phd  service   sex  salary
10      Prof          B   39       33  Male  128250
11      Prof          B   23       23  Male  134778
12  AsstProf          B    1        0  Male   88000
13      Prof          B   35       33  Male  162200
14      Prof          B   25       19  Male  153750
15      Prof          B   17        3  Male  150480
16  AsstProf          B    8        3  Male   75044
17  AsstProf          B    4        0  Male   92000
18      Prof          A   19        7  Male  107300
19      Prof          A   29       27  Male  150500
'''

#Select rows by their labels:
print(df_sub.loc[10:20,['rank','sex','salary']])
'''
    rank   sex  salary
10  Prof  Male  128250
11  Prof  Male  134778
13  Prof  Male  162200
14  Prof  Male  153750
15  Prof  Male  150480
19  Prof  Male  150500
'''

#Select rows by their labels:
print(df_sub.iloc[10:20,[0, 3, 4, 5]])
'''
    rank  service     sex  salary
26  Prof       19    Male  148750
27  Prof       43    Male  155865
29  Prof       20    Male  123683
31  Prof       21    Male  155750
35  Prof       23    Male  126933
36  Prof       45    Male  146856
39  Prof       18  Female  129000
40  Prof       36  Female  137000
44  Prof       19  Female  151768
45  Prof       25  Female  140096
'''

# Create a new data frame from the original sorted by the column Salary
df_sorted = df.sort_values( by ='service')
print(df_sorted.head())
'''
        rank discipline  phd  service     sex  salary
55  AsstProf          A    2        0  Female   72500
23  AsstProf          A    2        0    Male   85000
43  AsstProf          B    5        0  Female   77000
17  AsstProf          B    4        0    Male   92000
12  AsstProf          B    1        0    Male   88000
'''

df_sorted = df.sort_values( by =['service', 'salary'], ascending = [True, False])
print(df_sorted.head(10))
'''
        rank discipline  phd  service     sex  salary
52      Prof          A   12        0  Female  105000
17  AsstProf          B    4        0    Male   92000
12  AsstProf          B    1        0    Male   88000
23  AsstProf          A    2        0    Male   85000
43  AsstProf          B    5        0  Female   77000
55  AsstProf          A    2        0  Female   72500
57  AsstProf          A    3        1  Female   72500
28  AsstProf          B    7        2    Male   91300
42  AsstProf          B    4        2  Female   80225
68  AsstProf          A    4        2  Female   77500
'''
