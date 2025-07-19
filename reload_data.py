#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
重新加载data目录中的所有2025年数据
"""

import pandas as pd
import os
import glob
from datetime import datetime

def load_all_data():
    """
    从data目录加载所有CSV文件并合并
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
                
                # 添加日期列
                df['日期'] = full_date
                
                # 重新排列列的顺序
                cols = ['日期'] + [col for col in df.columns if col != '日期']
                df = df[cols]
                
                all_data.append(df)
                print(f"  - 加载了 {len(df)} 行数据，日期: {full_date}")
            
        except Exception as e:
            print(f"处理文件 {file_path} 时出错: {e}")
    
    if all_data:
        # 合并所有数据
        combined_df = pd.concat(all_data, ignore_index=True)
        print(f"\n总共加载了 {len(combined_df)} 行数据")
        
        # 保存到all_sentiment_data.csv
        combined_df.to_csv('all_sentiment_data.csv', index=False, encoding='utf-8')
        print("数据已保存到 all_sentiment_data.csv")
        
        # 同时保存到其他文件
        combined_df.to_csv('processed_sentiment_data.csv', index=False, encoding='utf-8')
        combined_df.to_csv('enhanced_processed_sentiment_data.csv', index=False, encoding='utf-8')
        combined_df.to_csv('merged_stock_sentiment_data.csv', index=False, encoding='utf-8')
        
        print("数据已同步到所有相关CSV文件")
        
        return combined_df
    else:
        print("没有找到有效的数据文件")
        return None

if __name__ == '__main__':
    load_all_data()