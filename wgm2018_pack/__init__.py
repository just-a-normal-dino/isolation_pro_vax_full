import os
import sys

# include current folder so I can import the other files
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from datas import *

import numpy as np
import pandas as pd
import networkx as nx

# import the functions
from make_att_from_quest import make_att_from_quest
from clean_df import clean_df
from get_col_values import get_col_values
from correlations import *
from make_graph import make_graph

# Other useful data
list_science_related_attitudes = make_att_from_quest(list_science_related_questions)


if (__name__ == '__main__'):
    print('')
    # print(wgm_dic.head())
    # print(list_of_attitudes)
    print(make_att_from_quest('Know Science'))