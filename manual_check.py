import csv
import pandas as pd

# 使用csv模块读取文件
with open('all_sentiment_data.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 打印总行数
print(f'CSV文件总行数: {len(lines)}')

# 统计2025-07-15日期的行数
july_15_lines = [line for line in lines if '2025-07-15' in line and '板块ETF流向' not in line]
print(f'2025-07-15日期（排除板块ETF流向）的行数: {len(july_15_lines)}')

# 打印这些行
print('\n2025-07-15日期的行:')
for i, line in enumerate(july_15_lines):
    print(f'{i+1}. {line.strip()}')

# 尝试使用csv模块读取
print('\n使用csv模块读取:')
try:
    with open('all_sentiment_data.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, quotechar='"', escapechar='\\')
        rows = list(reader)
    
    # 打印总行数
    print(f'CSV模块读取的总行数: {len(rows)}')
    
    # 统计2025-07-15日期的行数
    july_15_rows = [row for row in rows if len(row) > 0 and row[0] == '2025-07-15' and row[1] != '板块ETF流向']
    print(f'2025-07-15日期（排除板块ETF流向）的行数: {len(july_15_rows)}')
    
    # 打印这些行的指标名称
    print('\n2025-07-15日期的指标:')
    for i, row in enumerate(july_15_rows):
        if len(row) > 1:
            print(f'{i+1}. {row[1]}')
        else:
            print(f'{i+1}. 行格式错误: {row}')
            
except Exception as e:
    print(f'CSV模块读取错误: {e}')

# 尝试使用pandas读取
print('\n使用pandas读取:')
try:
    df = pd.read_csv('all_sentiment_data.csv', 
                     quotechar='"', 
                     sep=',',
                     escapechar='\\',
                     on_bad_lines='skip',
                     engine='python')
    
    # 打印总行数
    print(f'Pandas读取的总行数: {len(df)}')
    
    # 统计2025-07-15日期的行数
    july_15_df = df[(df['日期'] == '2025-07-15') & (df['指标名称'] != '板块ETF流向')]
    print(f'2025-07-15日期（排除板块ETF流向）的行数: {len(july_15_df)}')
    
    # 打印这些行的指标名称
    print('\n2025-07-15日期的指标:')
    for i, (idx, row) in enumerate(july_15_df.iterrows()):
        print(f'{i+1}. {row["指标名称"]}')
        
except Exception as e:
    print(f'Pandas读取错误: {e}')