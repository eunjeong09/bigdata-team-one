import pandas as pd
output_df = pd.read_csv('서울시 자치구별 민방위 비상급수시설 현황 자료.csv', encoding='cp949')
converted_addresses_df = pd.read_csv('converted_addresses.csv', encoding='utf-8')
merged_df = pd.merge(output_df, converted_addresses_df, on='시설주소', how='left')
merged_df.to_csv('merged_output.csv', index=False, encoding='utf-8-sig')
filtered_df = merged_df[merged_df['자치구'] == '영등포구'].drop_duplicates()
filtered_df.to_csv('filtered_output.csv', index=False, encoding='utf-8-sig')