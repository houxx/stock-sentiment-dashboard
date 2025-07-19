import pandas as pd

# 读取临时处理文件
try:
    df = pd.read_csv('temp_processed.csv')
    print(f'临时文件总行数: {len(df)}')
    
    # 过滤2025-07-15日期的数据
    filtered = df[(df['日期'] == '2025-07-15') & (df['指标名称'] != '板块ETF流向')]
    print(f'2025-07-15日期（排除板块ETF流向）的行数: {len(filtered)}')
    
    # 打印指标列表
    print('指标列表:')
    for idx, row in filtered.iterrows():
        print(f"  - {row['指标名称']}")
        
    # 检查SPY当日净流入金额和避险资产流向
    spy_flow = filtered[filtered['指标名称'] == 'SPY 当日净流入金额']
    safe_assets = filtered[filtered['指标名称'] == '避险资产流向 (TLT+GLD)']
    
    print('\nSPY当日净流入金额:')
    if len(spy_flow) > 0:
        for idx, row in spy_flow.iterrows():
            print(f"  - 情绪得分: {row['情绪得分']}, 类型: {type(row['情绪得分'])}")
    else:
        print('  - 未找到')
        
    print('\n避险资产流向 (TLT+GLD):')
    if len(safe_assets) > 0:
        for idx, row in safe_assets.iterrows():
            print(f"  - 情绪得分: {row['情绪得分']}, 类型: {type(row['情绪得分'])}")
    else:
        print('  - 未找到')
        
except Exception as e:
    print(f'错误: {e}')