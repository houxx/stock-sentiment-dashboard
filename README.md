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

项目包含多个Python脚本用于数据处理和更新：

- `process_sentiment_data.py` - 处理原始情绪数据
- `enhance_processed_data.py` - 增强数据处理
- `generate_sentiment_json.py` - 生成JSON配置文件
- `merge_csv_data.py` - 合并CSV数据文件

## 🎨 界面特色

- **情绪色彩编码**：绿色(乐观)、黄色(中性)、红色(悲观)
- **动态背景**：S&P 500图表根据当前情绪自动调整背景色
- **交互式图表**：支持缩放、悬停显示详细数据
- **趋势指示器**：显示各指标的变化趋势(上升/下降/持平)


## 🤝 贡献

欢迎提交Issue和Pull Request来改进项目！

## 📄 许可证

MIT License