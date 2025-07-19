import pandas as pd

# 读取CSV文件
df = pd.read_csv('all_sentiment_data.csv', 
               quotechar='"', 
               sep=',',
               escapechar='\\',
               on_bad_lines='skip')

# 打印总行数
print(f'读取后总行数: {len(df)}')

# 过滤2025-07-15日期的数据
df_filtered = df[df['日期'] == '2025-07-15']
print(f'2025-07-15日期的行数: {len(df_filtered)}')

# 排除板块ETF流向
df_filtered = df_filtered[df_filtered['指标名称'] != '板块ETF流向']
print(f'2025-07-15日期（排除板块ETF流向）的行数: {len(df_filtered)}')

# 打印这些行的详细信息
print('\n详细数据:')
for idx, row in df_filtered.iterrows():
    print(f"行 {idx}: 指标={row['指标名称']}, 情绪得分={row['情绪得分']}, 类型={type(row['情绪得分'])}")