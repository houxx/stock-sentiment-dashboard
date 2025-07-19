#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复数据格式，确保包含正确的列结构
"""

import pandas as pd
import os
import glob
from datetime import datetime

def get_sentiment_score(judgment):
    """根据判断结果返回情绪得分"""
    if judgment == '乐观':
        return 1.0
    elif judgment == '中性':
        return 0.0
    elif judgment == '悲观':
        return -1.0
    else:
        return 0.0

def extract_numeric_value(data_str):
    """从数据字符串中提取数值"""
    if pd.isna(data_str) or data_str == 'N/A':
        return None
    
    # 尝试提取数值
    import re
    
    # 处理特殊格式
    if '/' in str(data_str):  # 如 "6243.76 / 6158.46 / 5990.01"
        numbers = re.findall(r'\d+\.?\d*', str(data_str))
        if numbers:
            return float(numbers[0])  # 返回第一个数值
    
    # 提取单个数值
    numbers = re.findall(r'\d+\.?\d*', str(data_str))
    if numbers:
        return float(numbers[0])
    
    return None

def fix_data_format():
    """
    修复数据格式
    """
    data_dir = 'data'
    all_data = []
    
    # 获取所有CSV文件
    csv_files = glob.glob(os.path.join(data_dir, '*.csv'))
    csv_files = [f for f in csv_files if not f.endswith('_all.csv')]  # 排除汇总文件
    
    print(f"找到 {len(csv_files)} 个数据文件")
    
    for file_path in sorted(csv_files):
        print(f"处理文件: {file_path}")
        try:
            # 读取CSV文件
            df = pd.read_csv(file_path)
            
            # 检查是否有数据
            if len(df) > 0:
                # 提取日期信息
                filename = os.path.basename(file_path)
                date_str = filename.replace('.csv', '')
                
                # 转换为完整日期格式 (假设是2025年)
                if len(date_str) == 4:  # 格式如 0715
                    month = date_str[:2]
                    day = date_str[2:]
                    full_date = f"2025-{month}-{day}"
                else:
                    continue
                
                # 标准化列名
                expected_columns = [
                    '日期', '指标名称', '判断结果', '最新数据', 
                    '情绪得分', '数值数据', '当前状态解读', 
                    '判断标准', '整体解读'
                ]
                
                # 创建新的DataFrame
                new_data = []
                
                for idx, row in df.iterrows():
                    if pd.isna(row.iloc[1]):  # 跳过空行
                        continue
                        
                    # 提取基本信息
                    indicator_name = row.iloc[1] if len(row) > 1 else ''
                    judgment = row.iloc[2] if len(row) > 2 else ''
                    latest_data = row.iloc[3] if len(row) > 3 else ''
                    status_interpretation = row.iloc[4] if len(row) > 4 else ''
                    judgment_criteria = row.iloc[5] if len(row) > 5 else ''
                    overall_interpretation = row.iloc[6] if len(row) > 6 else ''
                    
                    # 计算情绪得分
                    sentiment_score = get_sentiment_score(judgment)
                    
                    # 提取数值数据
                    numeric_value = extract_numeric_value(latest_data)
                    
                    new_row = {
                        '日期': full_date,
                        '指标名称': indicator_name,
                        '判断结果': judgment,
                        '最新数据': latest_data,
                        '情绪得分': sentiment_score,
                        '数值数据': numeric_value,
                        '当前状态解读': status_interpretation,
                        '判断标准': judgment_criteria,
                        '整体解读': overall_interpretation
                    }
                    
                    new_data.append(new_row)
                
                if new_data:
                    day_df = pd.DataFrame(new_data)
                    all_data.append(day_df)
                    print(f"  - 处理了 {len(new_data)} 行数据，日期: {full_date}")
            
        except Exception as e:
            print(f"处理文件 {file_path} 时出错: {e}")
    
    if all_data:
        # 合并所有数据
        combined_df = pd.concat(all_data, ignore_index=True)
        print(f"\n总共处理了 {len(combined_df)} 行数据")
        
        # 保存到各个文件
        files_to_save = [
            'all_sentiment_data.csv',
            'processed_sentiment_data.csv', 
            'enhanced_processed_sentiment_data.csv',
            'merged_stock_sentiment_data.csv'
        ]
        
        for filename in files_to_save:
            combined_df.to_csv(filename, index=False, encoding='utf-8')
            print(f"数据已保存到 {filename}")
        
        return combined_df
    else:
        print("没有找到有效的数据")
        return None

if __name__ == '__main__':
    fix_data_format()