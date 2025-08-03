# 🎮 CS Skins Profit Tracker

A streamlined web app for managing, tracking, and analyzing the purchase and sale of CS:GO/CS2 skins. Built with [Streamlit](https://streamlit.io/), it offers an intuitive UI for recording trades, calculating profit, and visualizing inventory performance.

## 🚀 Features

### 📊 Core Functionality
- 📁 **Import and clean existing logs** (CSV/Excel)
- ➕ **Add new records with**:
  - Item name
  - Purchase & sell platform
  - Float value & automatic wear classification
  - Prices, dates, and actual cash received
- ✅ **Real-time profit calculation and summaries**

### 🛠 Utility Tools
- 💳 **Credit card fee calculator** (CSFloat USD → RMB)
- 📈 **Unit & total margin calculator** for trading
- 🔍 **Keyword search & sorting by profit**
- ✏️ **Edit and delete records in-place**
- 🌐 **Fully localized for Chinese users** with a styled interface

## 📂 File Structure

```
cs-skins-tracker/
├── main.py              # Main application file
├── gloves.png          # Background image
├── cs_log.csv          # Data storage file (auto-generated)
└── README.md           # Project documentation
```

## 🔧 Installation & Setup

### Prerequisites
- Python 3.7+
- Streamlit
- Pandas
- OpenPyxl (for Excel file support)

### Installation Steps

1. **Clone the repository**
```bash
git clone https://github.com/Tete-Tete/CS-Skins-Web-Ledger.git
cd CS-Skins-Web-Ledger
```

2. **Install dependencies**
```bash
pip install streamlit pandas openpyxl
```

3. **Run the application**
```bash
streamlit run main.py
```

4. **Access the app**
Open your browser and navigate to `http://localhost:8501`

## 💡 Usage Guide

### Adding New Records
1. Fill in trade information in the "Add New Record" section
2. Float values are automatically classified into wear grades
3. Profit is calculated automatically

### Data Management
- **Search**: Use keywords to search items or platforms
- **Sort**: Sort by profit (high to low or low to high)
- **Edit**: Click "修改" (Edit) button to modify existing records
- **Delete**: Click "删除" (Delete) button to remove records

### Calculator Tools
- **Credit Card Calculator**: Calculate actual cost for CSFloat top-ups
- **Profit Calculator**: Quick calculation of market price vs pickup price profit
- **General Calculator**: Basic math operations support

## 📊 Wear Grade Classification

| Float Range | Grade (Chinese) | Grade (English) |
|-------------|-----------------|-----------------|
| 0.00 - 0.07 | 崭新出厂 | Factory New |
| 0.07 - 0.15 | 略有磨损 | Minimal Wear |
| 0.15 - 0.38 | 久经沙场 | Field-Tested |
| 0.38 - 0.45 | 战痕累累 | Well-Worn |
| 0.45 - 1.00 | 破损不堪 | Battle-Scarred |

## 💰 Profit Status Indicators

- 🟡 **Yellow**: Unsold items
- 🔴 **Red**: Profitable trades
- 🟢 **Green**: Loss-making trades

## 📋 Data Fields

The application tracks the following trade information:
- Item name
- Purchase/sell platform
- Float value and wear grade
- Purchase/sell prices and dates
- Actual cash received
- Auto-calculated profit margin

## 🔒 Data Storage

- All data is stored locally in `cs_log.csv`
- Supports import/export of CSV and Excel formats
- UTF-8 encoding ensures proper Chinese character display

## 🎨 Theme & Styling

- Dark gaming-themed background
- Gold titles and cyan-green labels
- Orange interactive buttons
- Microsoft YaHei font optimized for Chinese display

## 🤝 Contributing

Issues and Pull Requests are welcome to improve this project!

## 📄 License

This project is licensed under the MIT License.

---

# 🎮 CS 饰品记账 App

一个基于 Streamlit 构建的专业 CS:GO/CS2 饰品交易管理和利润分析工具。提供直观的用户界面，用于记录交易、计算利润和可视化库存表现。

## 🚀 功能特性

### 📊 核心功能
- 📁 **导入和清理现有账本** (CSV/Excel)
- ➕ **添加新记录**：
  - 物品名称
  - 购买和销售平台
  - 磨损数值和自动磨损等级分类
  - 价格、日期和实际到手价格
- ✅ **实时利润计算和汇总**

### 🛠 实用工具
- 💳 **信用卡充值计算器** (CSFloat USD → RMB)
- 📈 **利润计算器** 用于交易分析
- 🔍 **关键词搜索和利润排序**
- ✏️ **就地编辑和删除记录**
- 🌐 **完全中文本地化界面**，风格化设计

## 📂 文件结构

```
cs-skins-tracker/
├── main.py              # 主应用文件
├── gloves.png          # 背景图片
├── cs_log.csv          # 数据存储文件（自动生成）
└── README.md           # 项目说明
```

## 🔧 安装和运行

### 环境要求
- Python 3.7+
- Streamlit
- Pandas
- OpenPyxl (用于Excel文件支持)

### 安装步骤

1. **克隆仓库**
```bash
git clone https://github.com/Tete-Tete/CS-Skins-Web-Ledger.git
cd CS-Skins-Web-Ledger
```

2. **安装依赖**
```bash
pip install streamlit pandas openpyxl
```

3. **运行应用**
```bash
streamlit run main.py
```

4. **访问应用**
在浏览器中打开 `http://localhost:8501`

## 💡 使用指南

### 添加新记录
1. 在"添加新记录"部分填写交易信息
2. 磨损值会自动分类为对应等级（崭新出厂、略有磨损等）
3. 系统会自动计算毛利

### 数据管理
- **搜索**：使用关键词搜索物品或平台
- **排序**：按毛利高低排序查看表现
- **编辑**：点击"修改"按钮编辑现有记录
- **删除**：点击"删除"按钮移除记录

### 计算工具
- **信用卡计算器**：计算CSFloat充值的实际成本
- **利润计算器**：快速计算市场价格与提货价的利润
- **通用计算器**：支持基本数学运算

## 📊 磨损等级分类

| 磨损范围 | 中文等级 | 英文等级 |
|---------|---------|----------|
| 0.00 - 0.07 | 崭新出厂 | Factory New |
| 0.07 - 0.15 | 略有磨损 | Minimal Wear |
| 0.15 - 0.38 | 久经沙场 | Field-Tested |
| 0.38 - 0.45 | 战痕累累 | Well-Worn |
| 0.45 - 1.00 | 破损不堪 | Battle-Scarred |

## 💰 利润状态指示

- 🟡 **黄色**：未售出
- 🔴 **红色**：盈利交易
- 🟢 **绿色**：亏损交易

## 📋 数据字段

应用记录以下交易信息：
- 购买物品名称
- 购买/销售平台
- 磨损数值和等级
- 购入/卖出价格和时间
- 实际到手价格
- 自动计算的毛利

## 🔒 数据存储

- 所有数据存储在本地 `cs_log.csv` 文件中
- 支持导入/导出 CSV 和 Excel 格式
- 数据使用 UTF-8 编码，确保中文显示正常

## 🎨 主题和样式

- 深色游戏主题背景
- 金色标题和青绿色标签
- 橙色交互按钮
- Microsoft YaHei 字体优化中文显示

## 🤝 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目！

## 📄 许可证

本项目采用 MIT 许可证。

---

*为 CS:GO/CS2 饰品交易者打造的专业工具 🎯*

