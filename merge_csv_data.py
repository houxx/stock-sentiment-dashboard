import pandas as pd
import os
from datetime import datetime
import glob

def merge_csv_files():
    """
    合并data目录下所有CSV文件，为每行数据添加日期列
    """
    # 设置数据目录路径
    data_dir = 'data'
    
    # 获取所有CSV文件（排除汇总文件）
    csv_files = glob.glob(os.path.join(data_dir, '*.csv'))
    csv_files = [f for f in csv_files if '汇总' not in f]
    
    # 存储所有数据的列表
    all_data = []
    
    for file_path in csv_files:
        # 从文件名提取日期
        filename = os.path.basename(file_path)
        date_str = filename.replace('.csv', '')
        
        # 将日期字符串转换为标准格式 (假设是2024年)
        try:
            if len(date_str) == 4:  # 格式如 '0711'
                month = int(date_str[:2])
                day = int(date_str[2:])
                date = f"2025-{month:02d}-{day:02d}"
            else:
                date = date_str
        except:
            date = date_str
        
        # 读取CSV文件
        try:
            df = pd.read_csv(file_path, encoding='utf-8')
        except UnicodeDecodeError:
            try:
                df = pd.read_csv(file_path, encoding='gbk')
            except:
                df = pd.read_csv(file_path, encoding='latin-1')
        
        # 添加日期列
        df['日期'] = date
        
        # 选择核心列（如果存在的话）
        core_columns = ['日期', '指标名称', '判断结果', '最新数据']
        
        # 检查哪些列存在
        available_columns = ['日期']
        for col in ['指标名称', '判断结果']:
            if col in df.columns:
                available_columns.append(col)
        
        # 查找包含"最新数据"的列
        latest_data_col = None
        for col in df.columns:
            if '最新数据' in str(col):
                latest_data_col = col
                break
        
        if latest_data_col:
            available_columns.append(latest_data_col)
            # 重命名为标准列名
            df = df.rename(columns={latest_data_col: '最新数据'})
            available_columns[-1] = '最新数据'
        
        # 选择可用的列
        df_selected = df[available_columns].copy()
        
        # 添加到总数据列表
        all_data.append(df_selected)
        
        print(f"已处理文件: {filename}, 日期: {date}, 数据行数: {len(df_selected)}")
    
    # 合并所有数据
    if all_data:
        merged_df = pd.concat(all_data, ignore_index=True)
        
        # 按日期排序
        merged_df = merged_df.sort_values('日期')
        
        print("\n=== 合并完成 ===")
        print(f"总数据行数: {len(merged_df)}")
        print(f"包含日期范围: {merged_df['日期'].min()} 到 {merged_df['日期'].max()}")
        print(f"包含指标数量: {merged_df['指标名称'].nunique()}")
        
        print("\n=== DataFrame信息概览 ===")
        print(merged_df.info())
        
        print("\n=== 前5行数据 ===")
        print(merged_df.head())
        
        print("\n=== 各日期数据统计 ===")
        print(merged_df['日期'].value_counts().sort_index())
        
        print("\n=== 指标名称统计 ===")
        print(merged_df['指标名称'].value_counts())
        
        return merged_df
    else:
        print("未找到有效的CSV文件")
        return None

if __name__ == "__main__":
    # 执行合并
    result_df = merge_csv_files()
    
    if result_df is not None:
        # 保存合并后的数据
        output_file = 'merged_stock_sentiment_data.csv'
        result_df.to_csv(output_file, index=False, encoding='utf-8-sig')
        print(f"\n合并后的数据已保存到: {output_file}")