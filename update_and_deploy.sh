#!/bin/bash

# 美股情绪看板数据更新和部署脚本

echo "🚀 开始更新美股情绪看板数据..."

# 检查是否有未提交的更改
if ! git diff --quiet; then
    echo "⚠️  检测到未提交的更改，正在处理..."
fi

# 数据处理步骤已简化，用户直接更新 enhanced_processed_sentiment_data.csv
echo "📊 检查数据文件更新..."
if [ ! -f "enhanced_processed_sentiment_data.csv" ]; then
    echo "❌ enhanced_processed_sentiment_data.csv 文件不存在"
    exit 1
fi

echo "检测到 enhanced_processed_sentiment_data.csv 文件，生成JSON文件..."

# 生成JSON文件
python3 generate_json_from_csv.py
if [ $? -ne 0 ]; then
    echo "错误: 生成JSON文件失败"
    exit 1
fi

echo "JSON文件生成成功，准备部署..."

# 添加所有更改到Git
echo "📝 添加文件到Git..."
git add .

# 检查是否有更改需要提交
if git diff --cached --quiet; then
    echo "ℹ️  没有检测到数据更改，无需提交"
else
    # 提交更改
    TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
    echo "💾 提交更改: $TIMESTAMP"
    git commit -m "数据更新: $TIMESTAMP"
    
    # 推送到远程仓库
    echo "🌐 推送到GitHub..."
    git push
    
    if [ $? -eq 0 ]; then
        echo "🎉 部署完成！GitHub Actions将自动更新网站"
        echo "📱 请稍等几分钟后访问您的GitHub Pages网站查看更新"
    else
        echo "❌ 推送失败，请检查网络连接和GitHub权限"
        exit 1
    fi
fi

echo "✨ 脚本执行完成！"