#!/bin/bash

# 美股情绪看板数据更新和部署脚本
# 版本: 2.0
# 更新时间: 2025-07-23

set -e  # 遇到错误立即退出

echo "🚀 开始更新美股情绪看板数据..."
echo "📅 当前时间: $(date '+%Y-%m-%d %H:%M:%S')"
echo "📂 工作目录: $(pwd)"
echo "🌐 远程仓库: $(git remote get-url origin)"
echo ""

# 检查Git状态
echo "🔍 检查Git状态..."
git status --porcelain
if ! git diff --quiet; then
    echo "⚠️  检测到未提交的更改，正在处理..."
else
    echo "✅ 工作目录干净"
fi
echo ""

# 数据处理步骤已简化，用户直接更新 enhanced_processed_sentiment_data.csv
echo "📊 检查数据文件更新..."
if [ ! -f "enhanced_processed_sentiment_data.csv" ]; then
    echo "❌ enhanced_processed_sentiment_data.csv 文件不存在"
    exit 1
fi

# 显示CSV文件信息
CSV_SIZE=$(wc -l < enhanced_processed_sentiment_data.csv)
CSV_MODIFIED=$(stat -f "%Sm" -t "%Y-%m-%d %H:%M:%S" enhanced_processed_sentiment_data.csv)
echo "✅ 检测到 enhanced_processed_sentiment_data.csv 文件"
echo "   📏 文件行数: $CSV_SIZE"
echo "   🕒 最后修改: $CSV_MODIFIED"
echo ""
echo "🔄 生成JSON文件..."

# 生成JSON文件
echo "   🐍 运行Python脚本: generate_json_from_csv.py"
python3 generate_json_from_csv.py
if [ $? -ne 0 ]; then
    echo "❌ 错误: 生成JSON文件失败"
    exit 1
fi

# 检查生成的JSON文件
if [ -f "sentiment_distribution.json" ]; then
    JSON_SIZE=$(wc -c < sentiment_distribution.json)
    echo "✅ JSON文件生成成功"
    echo "   📏 文件大小: $JSON_SIZE 字节"
else
    echo "❌ 错误: JSON文件未生成"
    exit 1
fi
echo ""
echo "🚀 准备部署..."

# 添加所有更改到Git
echo "📝 添加文件到Git..."
echo "   📋 添加前的状态:"
git status --porcelain
git add .
echo "   📋 添加后的状态:"
git diff --cached --name-status

# 检查是否有更改需要提交
echo ""
if git diff --cached --quiet; then
    echo "ℹ️  没有检测到数据更改，无需提交"
    echo "📊 当前数据已是最新版本"
else
    # 提交更改
    TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
    echo "💾 提交更改: $TIMESTAMP"
    git commit -m "数据更新: $TIMESTAMP"
    
    # 推送到远程仓库
    echo "🌐 推送到GitHub..."
    echo "   📡 正在上传到远程仓库..."
    git push
    
    if [ $? -eq 0 ]; then
        echo "✅ 推送成功！"
        echo "🎉 部署完成！GitHub Actions将自动更新网站"
        echo "📱 请稍等2-3分钟后访问您的GitHub Pages网站查看更新"
        echo "🔗 网站地址: https://houxx.github.io/stock-sentiment-dashboard/"
        echo "📊 数据文件: https://houxx.github.io/stock-sentiment-dashboard/sentiment_distribution.json"
    else
        echo "❌ 推送失败，请检查网络连接和GitHub权限"
        exit 1
    fi
fi

echo ""
echo "✨ 脚本执行完成！"
echo "📅 完成时间: $(date '+%Y-%m-%d %H:%M:%S')"
echo "⏱️  总耗时: $SECONDS 秒"