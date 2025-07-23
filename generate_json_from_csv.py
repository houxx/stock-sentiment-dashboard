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
            # 跳过表头行（日期列为"日期"的行）
            if date == '日期':
                continue
                
            # 过滤当天的数据，排除板块ETF流向和表头行
            day_data = df[(df['日期'] == date) & 
                         (df['指标名称'] != '板块ETF流向') & 
                         (df['指标名称'] != '指标名称')]
            
            # 统计各种情绪的数量
            sentiment_counts = {
                'optimistic': 0,
                'neutral': 0, 
                'pessimistic': 0,
                'missing': 0
            }
            
            for _, row in day_data.iterrows():
                judgment = str(row['判断结果']).strip()
                indicator_name = str(row['指标名称']).strip()
                
                # 调试7月22日的TRIN指数
                if date == '2025-07-22' and 'TRIN' in indicator_name:
                    print(f"调试TRIN指数: 指标='{indicator_name}', 判断结果='{judgment}'")
                
                # 处理带括号说明的判断结果，提取主要判断
                if '(' in judgment:
                    main_judgment = judgment.split('(')[0].strip()
                else:
                    main_judgment = judgment
                
                main_judgment_lower = main_judgment.lower()
                
                # 检查是否包含乐观相关词汇
                if (main_judgment in ['乐观'] or main_judgment_lower in ['optimistic'] or 
                    '乐观' in judgment or 'optimistic' in judgment.lower()):
                    if date == '2025-07-22' and 'TRIN' in indicator_name:
                        print(f"TRIN指数被识别为乐观")
                    sentiment_counts['optimistic'] += 1
                elif (main_judgment in ['中性'] or main_judgment_lower in ['neutral'] or
                      '中性' in judgment or 'neutral' in judgment.lower()):
                    if date == '2025-07-22' and 'TRIN' in indicator_name:
                        print(f"TRIN指数被识别为中性")
                    sentiment_counts['neutral'] += 1
                elif (main_judgment in ['悲观', '警示'] or main_judgment_lower in ['pessimistic'] or
                      '悲观' in judgment or 'pessimistic' in judgment.lower() or '警示' in judgment):
                    if date == '2025-07-22' and 'TRIN' in indicator_name:
                        print(f"TRIN指数被识别为悲观")
                    sentiment_counts['pessimistic'] += 1
                elif judgment in ['N/A', '', 'nan'] or pd.isna(row['判断结果']):
                    if date == '2025-07-22' and 'TRIN' in indicator_name:
                        print(f"TRIN指数被识别为缺失")
                    sentiment_counts['missing'] += 1
                else:
                    # 如果都不匹配，打印出来以便调试
                    print(f"未识别的判断结果: '{judgment}' (指标: {indicator_name}) 日期: {date}")
                    if date == '2025-07-22' and 'TRIN' in indicator_name:
                        print(f"TRIN指数进入else分支，被识别为缺失")
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