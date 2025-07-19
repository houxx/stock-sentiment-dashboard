#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从enhanced_processed_sentiment_data.csv生成sentiment_distribution.json
这个脚本替代了原有的复杂数据处理逻辑
"""

import pandas as pd
import json
from datetime import datetime
from collections import defaultdict

def generate_sentiment_json():
    """
    从enhanced_processed_sentiment_data.csv读取数据并生成sentiment_distribution.json
    """
    try:
        # 读取CSV文件
        df = pd.read_csv('enhanced_processed_sentiment_data.csv')
        
        # 确保必要的列存在
        required_columns = ['日期', '指标名称', '判断结果']
        for col in required_columns:
            if col not in df.columns:
                print(f"错误: CSV文件中缺少必要的列: {col}")
                return False
        
        # 按日期分组统计情绪分布
        sentiment_distribution = []
        
        # 获取所有唯一日期并排序
        dates = sorted(df['日期'].unique())
        
        for date in dates:
            # 过滤当天的数据，排除板块ETF流向
            day_data = df[(df['日期'] == date) & (df['指标名称'] != '板块ETF流向')]
            
            # 统计各种情绪的数量
            sentiment_counts = {
                'optimistic': 0,
                'neutral': 0, 
                'pessimistic': 0,
                'missing': 0
            }
            
            for _, row in day_data.iterrows():
                judgment = str(row['判断结果']).strip().lower()
                
                if judgment in ['乐观', 'optimistic']:
                    sentiment_counts['optimistic'] += 1
                elif judgment in ['中性', 'neutral']:
                    sentiment_counts['neutral'] += 1
                elif judgment in ['悲观', 'pessimistic', '警示']:
                    sentiment_counts['pessimistic'] += 1
                else:
                    sentiment_counts['missing'] += 1
            
            # 计算总数
            total = sum(sentiment_counts.values())
            
            # 添加到分布列表
            sentiment_distribution.append({
                'date': date,
                'optimistic': sentiment_counts['optimistic'],
                'neutral': sentiment_counts['neutral'],
                'pessimistic': sentiment_counts['pessimistic'],
                'missing': sentiment_counts['missing'],
                'total': total
            })
        
        # 生成最终的JSON结构
        result = {
            'overall_sentiment_distribution': sentiment_distribution
        }
        
        # 写入JSON文件
        with open('sentiment_distribution.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
        print(f"成功生成sentiment_distribution.json，包含{len(sentiment_distribution)}天的数据")
        return True
        
    except FileNotFoundError:
        print("错误: 找不到enhanced_processed_sentiment_data.csv文件")
        return False
    except Exception as e:
        print(f"生成JSON文件时发生错误: {e}")
        return False

if __name__ == '__main__':
    success = generate_sentiment_json()
    if not success:
        exit(1)