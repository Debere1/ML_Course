# #### Load the data

# %%
import pickle

# %%
model_data = 'model_C1.bin'

# %%
with open (model_data, 'rb') as f_in:
    dv, model = pickle.load( f_in)

# %%
dv, model