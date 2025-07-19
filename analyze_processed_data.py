import pandas as pd
import numpy as np

def analyze_processed_data():
    """
    分析处理后的情绪数据
    """
    # 读取处理后的数据
    df = pd.read_csv('processed_sentiment_data.csv')
    
    print("=== 处理后的DataFrame概览 ===")
    print(f"总行数: {len(df)}")
    print(f"总列数: {len(df.columns)}")
    print(f"列名: {list(df.columns)}")
    
    print("\n=== 前10行数据 ===")
    print(df.head(10).to_string())
    
    print("\n=== 数据类型 ===")
    print(df.dtypes)
    
    print("\n=== 情绪得分分布 ===")
    sentiment_counts = df['情绪得分'].value_counts(dropna=False)
    print(sentiment_counts)
    print(f"\n情绪得分统计:")
    print(f"乐观 (1.0): {sentiment_counts.get(1.0, 0)} 条 ({sentiment_counts.get(1.0, 0)/len(df)*100:.1f}%)")
    print(f"中性 (0.0): {sentiment_counts.get(0.0, 0)} 条 ({sentiment_counts.get(0.0, 0)/len(df)*100:.1f}%)")
    print(f"悲观 (-1.0): {sentiment_counts.get(-1.0, 0)} 条 ({sentiment_counts.get(-1.0, 0)/len(df)*100:.1f}%)")
    print(f"缺失值: {df['情绪得分'].isna().sum()} 条 ({df['情绪得分'].isna().sum()/len(df)*100:.1f}%)")
    
    print("\n=== 数值数据解析成功率 ===")
    print(f"成功解析: {df['数值数据'].notna().sum()} 条 ({df['数值数据'].notna().sum()/len(df)*100:.1f}%)")
    print(f"解析失败: {df['数值数据'].isna().sum()} 条 ({df['数值数据'].isna().sum()/len(df)*100:.1f}%)")
    
    print("\n=== 各指标解析详情 ===")
    for indicator in sorted(df['指标名称'].unique()):
        if pd.notna(indicator):
            indicator_data = df[df['指标名称'] == indicator]
            total = len(indicator_data)
            valid_sentiment = indicator_data['情绪得分'].notna().sum()
            valid_numeric = indicator_data['数值数据'].notna().sum()
            
            print(f"{indicator}:")
            print(f"  总数据: {total} 条")
            print(f"  情绪得分有效: {valid_sentiment}/{total} ({valid_sentiment/total*100:.1f}%)")
            print(f"  数值数据有效: {valid_numeric}/{total} ({valid_numeric/total*100:.1f}%)")
            
            # 显示数值范围
            if valid_numeric > 0:
                numeric_data = indicator_data['数值数据'].dropna()
                print(f"  数值范围: {numeric_data.min():.2f} ~ {numeric_data.max():.2f}")
                print(f"  平均值: {numeric_data.mean():.2f}")
    
    print("\n=== 按日期统计情绪分布 ===")
    daily_sentiment = df.groupby('日期')['情绪得分'].agg(['count', 'mean', 'std']).round(2)
    print(daily_sentiment)
    
    print("\n=== 数据质量检查 ===")
    print("缺失值统计:")
    missing_stats = df.isnull().sum()
    for col, missing_count in missing_stats.items():
        if missing_count > 0:
            print(f"  {col}: {missing_count} 条 ({missing_count/len(df)*100:.1f}%)")
    
    # 检查异常值
    print("\n数值数据异常值检查:")
    numeric_data = df['数值数据'].dropna()
    if len(numeric_data) > 0:
        q1 = numeric_data.quantile(0.25)
        q3 = numeric_data.quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers = numeric_data[(numeric_data < lower_bound) | (numeric_data > upper_bound)]
        print(f"  潜在异常值数量: {len(outliers)}")
        if len(outliers) > 0:
            print(f"  异常值范围: {outliers.min():.2f} ~ {outliers.max():.2f}")
    
    print("\n=== 示例数据展示 ===")
    # 显示每个指标的一个示例
    sample_data = df.groupby('指标名称').first()[['判断结果', '最新数据', '情绪得分', '数值数据']]
    print(sample_data.to_string())
    
    return df

if __name__ == "__main__":
    result_df = analyze_processed_data()