import os
import sys

# include current folder so I can import the other files
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

import pandas as pd


# import the data
wgm_dic = pd.read_pickle(os.path.join(os.path.dirname(__file__), 'data\wgm2018_clean_dictionary.pkl'))
wgm_numeric = pd.read_pickle(os.path.join(os.path.dirname(__file__), 'data\wgm2018_clean_numeric.pkl'))
wgm_labels = pd.read_pickle(os.path.join(os.path.dirname(__file__), 'data\wgm2018_clean_labels.pkl'))
wgm_bool = pd.read_pickle(os.path.join(os.path.dirname(__file__), 'data\wgm2018_clean_boolean.pkl'))

list_of_attitudes = list(wgm_bool.columns)
countries_list = wgm_labels["Country"].unique()

list_science_related_questions = ['Know Science', 'Understand meaning Sci', 'Study disease is science', 'Poetry is science', 'Learned Sci in Prim.School', 'Learned Sci in Sec.School', 'Learned Sci in College/Uni', 'Searched Sci past 30d', 'Searched Med past 30d', 'Searched Sci', 'Searched Med', 'Confidence NGO', 'Confidence Hospitals', 'Trust neighborhood', 'Trust government', 'Trust Scientists', 'Trust Journalists', 'Trust Doctors', 'Trust NGO workers', 'Trust traditional Healers', 'Trust science', 'Trust Scientists 4 info', 'Trust scientist intentions', 'Trust scientists honesty', 'Trust scientist in Med Comp intentions', 'Trust scientists in Med Comp honesty', 'Science benefits', 'Science benefits you', 'Science improve next gen', 'Science will increase jobs', 'Who trust most for Med Advice', 'Trust gov 4 Med Advice', 'Trust Doc 4 med advice', 'Ever heard of vaccines', 'Vaccines important to children', 'Vaccines Safe', 'Vaccines Effective', 'Have Children', 'Your Child Received Vax', 'Religion', 'Science disagreed w your religion', '(disagreement)Believe science or religion', 'How feel science']

list_science_questions2 = [
    #     'Know Science',
    #  'Understand meaning Sci',
    #  'Study disease is science',
    #  'Poetry is science',
    #  'Learned Sci in Prim.School',
    #  'Learned Sci in Sec.School',
    #  'Learned Sci in College/Uni',
    #  'Searched Sci past 30d',
    #  'Searched Med past 30d',

    #  'Searched Sci',
    #  'Searched Med',

    #  'Confidence NGO',
    #  'Confidence Hospitals',
    #  'Trust neighborhood',
    #  'Trust government',

    'Trust Scientists',
    #  'Trust Journalists',
    'Trust Doctors',
    #  'Trust NGO workers',
    #  'Trust traditional Healers',
    'Trust science',
    'Trust Scientists 4 info',
    'Trust scientist intentions',
    'Trust scientists honesty',
    'Trust scientist in Med Comp intentions',
    'Trust scientists in Med Comp honesty',
    #  'Science benefits',
    #  'Science benefits you',
    #  'Science improve next gen',
    #  'Science will increase jobs',
    #  'Who trust most for Med Advice',
    #  'Trust gov 4 Med Advice',
    #  'Trust Doc 4 med advice',
    #  'Ever heard of vaccines',
    'Vaccines important to children',
    'Vaccines Safe',
    'Vaccines Effective',
    #  'Have Children',
    #  'Your Child Received Vax',
    #  'Religion',
    #  'Science disagreed w your religion',
    #  '(disagreement)Believe science or religion',
    'How feel science']