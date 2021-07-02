import pandas as pd

#Get lucky number from command line
#num = int(input("Input the lucky number: "))
#print (df_luckydraw.iloc[num,:])

#pd.set_option('display.max_rows', None)

# Assume the csv file has 3 columns (1. HKID, 2. MOBILE NO, 3. NAME)
df_luckydraw = pd.read_csv('luckydraw_result.csv')
print('Raw data')
print(df_luckydraw)

#selected_columns = df_luckydraw_raw[["HKID","MOBILE"]]
#df_luckydraw = selected_columns.copy()

print("\nStatistic: Duplicated records (key = HKID + MOBILE)")
dups_hkid_mobile = df_luckydraw.pivot_table(index=['HKID','MOBILE'], aggfunc='size')
print(dups_hkid_mobile)

pd.set_option('display.max_rows', None)

print("\nStatistic: Duplicated records (key = HKID)")
dups_hkid = df_luckydraw.pivot_table(index=['HKID'], aggfunc='size')
print(dups_hkid)

print("\nStatistic: Duplicated records (key = MOBILE)")
dups_mobile = df_luckydraw.pivot_table(index=['MOBILE'], aggfunc='size')
print(dups_mobile)

pd.set_option('display.max_rows', 20)

#Generate dataset (df_hkid) for the column [HKID]
df_hkid = df_luckydraw.copy()

#Remove duplicated records (df_hkid_unique)
print("\nBefore: df_hkid")

df_hkid = df_hkid.sort_values('HKID',ascending=True)
print(df_hkid)

df_hkid_unique = df_hkid.drop_duplicates(subset='HKID', keep="first")

print("After: df_hkid")
print(df_hkid_unique)
print("\n")

#Generate dataset (df_mobile) for the column [MOBILE]
df_mobile = df_luckydraw.copy()

#Remove duplicated records (df_mobile_unique)
print("\nBefore: df_mobile")

df_mobile = df_mobile.sort_values('MOBILE', ascending=True)
print(df_mobile)

df_mobile_unique = df_mobile.drop_duplicates(subset='MOBILE', keep="first")

print("After: df_mobile")
print(df_mobile_unique)
print("\n")

#Combine df_hkid_unique and df_mobile_unique (df_combined)
print("Result: ")
#result = pd.merge(df_hkid_unique,
#	              df_mobile_unique,
#	              left_on='HKID',
#	              right_on='HKID',
#	              how='inner')
#print(result)

df_merge = pd.concat([df_hkid_unique, df_mobile_unique])
print("Before: df_merge")
print(df_merge)

df_merge_hkid_unique = df_merge.drop_duplicates(subset='HKID', keep="first")
df_merge_hkid_mobile_unique = df_merge_hkid_unique.drop_duplicates(subset='MOBILE', keep="first")

pd.set_option('display.max_rows', None)

print("After: df_merge")
print(df_merge_hkid_mobile_unique)

#Remove dupliacated recores (df_combined_unique)

#Assign index numbers to df_combined_unique

