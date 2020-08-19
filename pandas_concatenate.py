#%% create test data frames
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    },
                    index=[0, 1, 2, 3])


df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'C': ['B4', 'B5', 'B6', 'B7'],
                    },
                     index=[0, 1, 2, 4])

s2 = pd.Series(['X0', 'X1', 'X2'], index=['A', 'B', 'C'])

df3 = pd.DataFrame({
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                    index=[8, 9, 10, 11])

#%%
display(df1)
display(df2)
display(df3)
# %%
# concatenates data frame rows by default (axis=0)
# merging common columns
pd.concat([df1, df2])

#%%
# concatenates data frame columns (axis=1)
# merging common rows (using index)
display(df1), display(df2)
pd.concat([df1, df2], axis=1)

#%%
# keys provide multi-index
pd.concat([df1, df2], axis=1, keys=["a", "b"])

#%%
# ignore index is like resetting the index/columns after concat
pd.concat([df1, df2], axis=1, keys=["a", "b"], ignore_index=True)

# %%
# series is considered like a 1 column data frame
pd.concat((df1, s2))
# %%
# append a row to data frame
df1.append(s2, ignore_index=True)
# %%
df1

# %%
