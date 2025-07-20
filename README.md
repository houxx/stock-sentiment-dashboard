# 美股情绪看板 (Stock Sentiment Dashboard)

一个综合性的美股市场情绪分析看板，实时展示多个关键指标和情绪趋势。

## 🚀 功能特性

- **多维度情绪指标**：VIX恐慌指数、CNN恐惧贪婪指数、TRIN指数、Put/Call比率等
- **S&P 500指数分析**：包含MA20和MA50移动平均线，根据情绪动态调整背景颜色
- **实时数据可视化**：使用Chart.js构建的交互式图表
- **情绪趋势分析**：自动计算和显示市场情绪变化趋势
- **响应式设计**：适配不同屏幕尺寸的现代化UI界面

## 📊 主要指标

| 指标 | 描述 | 情绪判断 |
|------|------|----------|
| VIX指数 | 市场波动率恐慌指数 | 乐观: <20, 中性: 20-30, 悲观: >30 |
| CNN恐惧贪婪指数 | 市场情绪综合指标 | 乐观: >50, 中性: 25-50, 悲观: <25 |
| TRIN指数 | 短期交易指数 | 乐观: <1, 中性: 1-1.5, 悲观: >1.5 |
| Put/Call比率 | 看跌看涨期权比率 | 乐观: <0.8, 中性: 0.8-1.2, 悲观: >1.2 |
| S&P 500 | 标普500指数与均线 | 基于价格与MA20/MA50关系判断 |

## 🛠️ 技术栈

- **前端**: HTML5, CSS3, JavaScript (ES6+)
- **图表库**: Chart.js + chartjs-plugin-annotation
- **数据格式**: CSV, JSON
- **样式**: 现代化响应式设计

## 📁 项目结构

```
美股情绪看板/
├── integrated_dashboard.html          # 主看板页面
├── enhanced_processed_sentiment_data.csv  # 历史情绪数据
├── sentiment_distribution.json        # 情绪分布配置
├── chart.min.js                      # Chart.js库
├── chart.min.css                     # Chart.js样式
├── chartjs-plugin-annotation.min.js  # 图表注释插件
├── data/                             # 原始数据文件夹
│   ├── 0623.csv ~ 0717.csv           # 每日数据文件
└── *.py                              # 数据处理脚本
```

## 🚀 快速开始

### 本地运行

1. 克隆项目到本地
```bash
git clone https://github.com/houxx/stock-sentiment-dashboard.git
cd stock-sentiment-dashboard
```

2. 启动本地服务器
```bash
python3 -m http.server 8000
```

3. 在浏览器中访问
```
http://localhost:8000/integrated_dashboard.html
```

### GitHub Pages 部署

项目已配置GitHub Pages，可直接访问：
```
https://houxx.github.io/stock-sentiment-dashboard/integrated_dashboard.html
```

## 📈 数据更新

### 完整更新流程

#### 1. **准备工作**
```bash
# 确保本地仓库是最新的
git pull origin main

# 检查当前状态
git status
```

#### 2. **更新主数据文件**
```bash
# 方式一：直接编辑CSV文件
vim enhanced_processed_sentiment_data.csv

# 方式二：使用数据处理脚本
python3 add_spy_flow_data.py  # 添加新的SPY流入数据
python3 merge_csv_data.py     # 合并多个CSV文件
```

**数据格式说明：**
- 列1: 日期 (YYYY-MM-DD)
- 列2: 指标名称
- 列3: 判断结果 (乐观/中性/悲观/悲观/警示)
- 列4: 情绪得分 (1.0/0.0/-1.0)
- 列5: 数值数据
- 列6: 判断标准
- 列7: 当前状态解读

#### 3. **数据验证**
```bash
# 检查数据格式是否正确
python3 check_csv.py

# 修复数据格式问题（如果需要）
python3 fix_data_format.py

# 分析处理后的数据
python3 analyze_processed_data.py
```

#### 4. **生成配置文件**
```bash
# 从CSV生成JSON配置文件
python3 generate_json_from_csv.py
```

#### 5. **本地测试**
```bash
# 启动本地服务器测试
python3 -m http.server 8000

# 在浏览器中访问 http://localhost:8000/integrated_dashboard.html
# 验证数据更新是否正确显示
```

#### 6. **提交到Git**
```bash
# 添加所有更改的文件
git add .

# 提交更改（建议使用描述性的提交信息）
git commit -m "数据更新: 添加YYYY-MM-DD的情绪指标数据"

# 推送到远程仓库
git push origin main
```

#### 7. **验证部署**
- GitHub Actions会自动检测更新并重新部署
- 等待1-2分钟后访问线上页面：https://houxx.github.io/stock-sentiment-dashboard/integrated_dashboard.html
- 检查数据是否正确更新

### 快速更新脚本

为了简化更新流程，可以使用提供的自动化脚本：

```bash
# 使用自动更新脚本
./update_and_deploy.sh
```

### 常见问题解决

#### 数据格式错误
```bash
# 如果遇到CSV格式问题
python3 fix_data_format.py

# 手动检查特定日期的数据
python3 manual_check.py
```

#### Git推送失败
```bash
# 如果推送失败，先拉取最新代码
git pull origin main

# 解决冲突后重新推送
git push origin main

# 如果是首次推送，设置上游分支
git push --set-upstream origin main
```

#### 部署验证
```bash
# 检查GitHub Actions部署状态
# 访问: https://github.com/houxx/stock-sentiment-dashboard/actions

# 如果部署失败，检查workflow配置
cat .github/workflows/deploy.yml
```

### 数据处理脚本

项目包含多个Python脚本用于数据处理和更新：

- `generate_json_from_csv.py` - 从CSV生成JSON配置文件
- `process_sentiment_data.py` - 处理原始情绪数据
- `enhance_processed_data.py` - 增强数据处理
- `merge_csv_data.py` - 合并CSV数据文件
- `check_csv.py` - 检查CSV数据格式
- `fix_data_format.py` - 修复数据格式问题

## 🎨 界面特色

- **情绪色彩编码**：绿色(乐观)、黄色(中性)、红色(悲观)
- **动态背景**：S&P 500图表根据当前情绪自动调整背景色
- **交互式图表**：支持缩放、悬停显示详细数据
- **趋势指示器**：显示各指标的变化趋势(上升/下降/持平)


## 🤝 贡献

欢迎提交Issue和Pull Request来改进项目！

## 📄 许可证

MIT License