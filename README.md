# 美股情绪看板 (Stock Sentiment Dashboard)

一个综合性的美股市场情绪分析看板，实时展示多个关键指标和情绪趋势。

## 🚀 功能特性

- **多维度情绪指标**：VIX恐慌指数、CNN恐惧贪婪指数、TRIN指数、Put/Call比率等
- **S&P 500指数分析**：包含MA20和MA50移动平均线，根据情绪动态调整背景颜色
- **实时数据可视化**：使用Chart.js构建的交互式图表
- **情绪趋势分析**：自动计算和显示市场情绪变化趋势
- **响应式设计**：适配不同屏幕尺寸的现代化UI界面
- **智能分类布局**：指标按类别分组显示，提供更清晰的信息架构
- **网站监控分析**：集成Google Analytics 4和Microsoft Clarity，全面监控用户行为
- **自定义事件跟踪**：监控指标卡片点击、图表交互、页面停留时间等关键指标

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
- **监控分析**: Google Analytics 4, Microsoft Clarity
- **部署**: GitHub Pages, GitHub Actions
- **版本控制**: Git

## 📁 项目结构

```
美股情绪看板/
├── integrated_dashboard.html          # 主看板页面（含监控代码）
├── index.html                        # 入口页面（含监控代码）
├── enhanced_processed_sentiment_data.csv  # 历史情绪数据
├── sentiment_distribution.json        # 情绪分布配置
├── analytics_setup.md                # 监控配置指南
├── chart.min.js                      # Chart.js库
├── chart.min.css                     # Chart.js样式
├── chartjs-plugin-annotation.min.js  # 图表注释插件
├── update_and_deploy.sh              # 自动化更新部署脚本
├── .github/workflows/deploy.yml      # GitHub Actions配置
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
# 主页面（自动跳转到仪表板）
https://houxx.github.io/stock-sentiment-dashboard/

# 直接访问仪表板
https://houxx.github.io/stock-sentiment-dashboard/integrated_dashboard.html
```

**监控功能已启用**：网站访问数据将自动收集到Google Analytics和Microsoft Clarity

## 📈 数据更新

### 🚀 快速更新（推荐方法）

使用自动化脚本一键更新和部署：

```bash
# 1. 更新数据文件
# 直接编辑 enhanced_processed_sentiment_data.csv 添加新数据

# 2. 运行自动化脚本
./update_and_deploy.sh
```

**脚本功能**：
- ✅ 自动检查数据文件
- ✅ 生成JSON配置文件
- ✅ 提交到Git仓库
- ✅ 推送到GitHub
- ✅ 触发自动部署

### 📋 手动更新流程

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

### 🔧 脚本使用说明

**update_and_deploy.sh** 是一个全自动的数据更新和部署脚本：

```bash
# 给脚本执行权限（首次使用）
chmod +x update_and_deploy.sh

# 运行自动更新脚本
./update_and_deploy.sh
```

**执行流程**：
1. 🔍 检查数据文件是否存在
2. 🔄 自动生成JSON配置文件
3. 📝 添加所有更改到Git
4. 💾 自动提交（带时间戳）
5. 🌐 推送到GitHub仓库
6. 🚀 触发GitHub Actions自动部署

**优势**：
- ⚡ 一键操作，无需手动执行多个命令
- 🛡️ 自动错误检查和处理
- 📅 自动生成时间戳提交信息
- 🔄 确保数据同步和部署一致性

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

## 📊 监控分析

### 🔍 网站监控功能

项目已集成专业级网站监控系统：

**Google Analytics 4**
- 📈 页面浏览量和用户数统计
- ⏱️ 用户会话时长和跳出率
- 🌍 访问来源和地理位置分析
- 📱 设备和浏览器使用情况

**Microsoft Clarity**
- 🎥 用户行为录屏回放
- 🔥 页面热力图分析
- 👆 点击和滚动行为追踪
- 📊 用户体验指标监控

### 📋 自定义事件跟踪

系统自动监控以下关键用户行为：

- **页面交互**：页面加载、停留时间、离开页面
- **指标卡片**：点击各类情绪指标卡片
- **图表互动**：与S&P 500情绪图表的交互
- **滚动深度**：用户阅读内容的完整程度
- **用户参与**：整体参与度和活跃度指标

### 📈 数据查看

**访问监控数据**：
- Google Analytics：[https://analytics.google.com/](https://analytics.google.com/)
- Microsoft Clarity：[https://clarity.microsoft.com/](https://clarity.microsoft.com/)

**关键指标**：
- 📊 日活跃用户数 (DAU)
- ⏰ 平均会话时长
- 🎯 指标卡片点击率
- 📱 移动端使用比例
- 🔄 用户留存率

## 🎨 界面特色

- **情绪色彩编码**：绿色(乐观)、黄色(中性)、红色(悲观)
- **动态背景**：S&P 500图表根据当前情绪自动调整背景色
- **交互式图表**：支持缩放、悬停显示详细数据
- **趋势指示器**：显示各指标的变化趋势(上升/下降/持平)


## 🤝 贡献

欢迎提交Issue和Pull Request来改进项目！

## 📄 许可证

MIT License