import pandas as pd
import numpy as np
from snsynth import Synthesizer

survey_df = pd.read_csv('combined_survey.csv')

numerical_cols = survey_df.select_dtypes(include='number').columns
numerical_df = survey_df[numerical_cols]
for i in range(1,10): #generate 10 versions of the dataset, to account for randomness of AIM generator
    numerical_syn_df = numerical_df.copy()
    synth = Synthesizer.create('aim', epsilon=5, verbose=True)
    sample = synth.fit_sample(numerical_syn_df, preprocessor_eps=0.5)
    numerical_syn_df = sample

    numerical_syn_df.to_csv(f'survey_syn_5_{i}.csv')