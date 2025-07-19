import pandas as pd
import os
import re

# 定义函数用于从CSV文件中提取SPY当日净流入金额数据
def extract_spy_flow_data(file_path):
    try:
        # 读取CSV文件
        df = pd.read_csv(file_path, encoding='utf-8')
        
        # 查找SPY当日净流入金额的行
        spy_flow_row = None
        for index, row in df.iterrows():
            # 检查第二列是否包含SPY当日净流入金额
            if isinstance(row.iloc[1], str) and 'SPY 当日净流入金额' in row.iloc[1]:
                spy_flow_row = row
                break
        
        if spy_flow_row is not None:
            # 提取日期（从文件名）
            date_match = re.search(r'(\d{4})\.(csv)$', file_path)
            if date_match:
                month = date_match.group(1)[:2]
                day = date_match.group(1)[2:]
                date_str = f'2025-{month}-{day}'
            else:
                return None
            
            # 提取判断结果、最新数据、当前状态解读等
            judgment = spy_flow_row.iloc[2] if len(spy_flow_row) > 2 else ''
            latest_data = spy_flow_row.iloc[3] if len(spy_flow_row) > 3 else ''
            status_interpretation = spy_flow_row.iloc[4] if len(spy_flow_row) > 4 else ''
            judgment_criteria = spy_flow_row.iloc[5] if len(spy_flow_row) > 5 else ''
            overall_interpretation = spy_flow_row.iloc[6] if len(spy_flow_row) > 6 else ''
            
            # 计算情绪得分
            sentiment_score = 0
            if judgment == '乐观':
                sentiment_score = 1.0
            elif judgment == '悲观' or judgment == '悲观/警示':
                sentiment_score = -1.0
            elif judgment == '中性':
                sentiment_score = 0.0
            
            # 提取数值数据
            numerical_data = 0
            if latest_data != 'N/A' and latest_data:
                # 处理带有M、B、k后缀的数值
                if isinstance(latest_data, str):
                    latest_data = latest_data.strip()
                    if '+' in latest_data or '-' in latest_data:
                        sign = 1 if '+' in latest_data else -1
                        value_str = latest_data.replace('+', '').replace('-', '')
                        
                        if 'B' in value_str:
                            numerical_data = sign * float(value_str.replace('B', '')) * 1000
                        elif 'M' in value_str:
                            numerical_data = sign * float(value_str.replace('M', ''))
                        elif 'k' in value_str:
                            numerical_data = sign * float(value_str.replace('k', '')) / 1000
                        else:
                            try:
                                numerical_data = sign * float(value_str)
                            except:
                                numerical_data = 0
            
            return {
                'date': date_str,
                'indicator': 'SPY 当日净流入金额',
                'judgment': judgment,
                'latest_data': latest_data,
                'sentiment_score': sentiment_score,
                'numerical_data': numerical_data,
                'status_interpretation': status_interpretation,
                'judgment_criteria': judgment_criteria,
                'overall_interpretation': overall_interpretation
            }
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
    
    return None

# 主函数
def add_spy_flow_data_to_csv():
    # 读取现有的all_sentiment_data.csv文件
    all_sentiment_data_path = '/Users/houxx/Desktop/code/美股情绪看板/all_sentiment_data.csv'
    all_sentiment_df = pd.read_csv(all_sentiment_data_path, encoding='utf-8')
    
    # 获取data文件夹中的所有CSV文件
    data_folder = '/Users/houxx/Desktop/code/美股情绪看板/data'
    csv_files = [os.path.join(data_folder, f) for f in os.listdir(data_folder) if f.endswith('.csv') and not f.startswith('汇总')]
    
    # 提取SPY当日净流入金额数据
    spy_flow_data = []
    for file_path in csv_files:
        data = extract_spy_flow_data(file_path)
        if data:
            spy_flow_data.append(data)
    
    # 创建新的DataFrame
    spy_flow_df = pd.DataFrame(spy_flow_data)
    
    # 检查是否有数据
    if spy_flow_df.empty:
        print("没有找到SPY当日净流入金额数据")
        return
    
    # 格式化数据以匹配all_sentiment_data.csv的格式
    formatted_data = []
    for _, row in spy_flow_df.iterrows():
        formatted_row = {
            '日期': row['date'],
            '指标名称': row['indicator'],
            '判断结果': row['judgment'],
            '最新数据': row['latest_data'],
            '情绪得分': row['sentiment_score'],
            '数值数据': row['numerical_data'],
            'MA20': '',
            'MA50': '',
            '当前状态解读': row['status_interpretation'],
            '判断标准': row['judgment_criteria'],
            '整体解读': row['overall_interpretation']
        }
        formatted_data.append(formatted_row)
    
    # 创建新的DataFrame
    new_data_df = pd.DataFrame(formatted_data)
    
    # 合并数据
    combined_df = pd.concat([all_sentiment_df, new_data_df], ignore_index=True)
    
    # 保存到all_sentiment_data.csv
    combined_df.to_csv(all_sentiment_data_path, index=False, encoding='utf-8')
    print(f"已成功将SPY当日净流入金额数据添加到{all_sentiment_data_path}")

# 执行主函数
if __name__ == '__main__':
    add_spy_flow_data_to_csv()