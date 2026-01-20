import sys

import akshare as ak
import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime
matplotlib.use('TkAgg')

# ======================
# 参数
# ======================
formatted_time = datetime.now().strftime("%Y%m%d")

SYMBOL = "059770"
START = "20250101"
END = formatted_time

# ======================
# 获取股票数据
# ======================
# df = ak.stock_zh_a_hist(
#     symbol=SYMBOL,
#     period="daily",
#     start_date=START,
#     end_date=END,
#     adjust="qfq"
# )
# ======================
# 获取ETF数据
# ======================
df = ak.fund_etf_hist_em(
    symbol=SYMBOL,         # ETF代码，例如 510300 是沪深300ETF
    period="daily",        # 周期 daily/weekly/monthly
    start_date=START,      # 开始日期
    end_date=END,          # 结束日期
    adjust="qfq"           # 复权类型："" 不复权 / "qfq" 前复权 / "hfq" 后复权
)

# df.rename(columns={
#     "收盘": "Close",
#     "日期": "Time"
# }, inplace=True)

print(df)
if df.empty:
    print('未拉取到有效数据！')
    sys.exit()

df.to_csv(f'data_{SYMBOL}.csv', index=False, encoding='utf-8-sig')

# ======================
# 技术指标
# ======================
df["MA20"] = df["收盘"].rolling(20).mean()
df["MA60"] = df["收盘"].rolling(60).mean()

# MACD
df["EMA12"] = df["收盘"].ewm(span=12, adjust=False).mean()
df["EMA26"] = df["收盘"].ewm(span=26, adjust=False).mean()
df["MACD"] = df["EMA12"] - df["EMA26"]
df["SIGNAL"] = df["MACD"].ewm(span=9, adjust=False).mean()

# RSI
delta = df["收盘"].diff()
gain = delta.clip(lower=0)
loss = -delta.clip(upper=0)
rs = gain.rolling(14).mean() / loss.rolling(14).mean()
df["RSI"] = 100 - (100 / (1 + rs))

# ======================
# 输出结论
# ======================
latest = df.iloc[-1]

trend = "上升" if latest["MA20"] > latest["MA60"] else "走弱"

print("====== 股票行情 ======")
print(f"趋势：{trend}")
print(f"RSI：{latest['RSI']:.2f}")
print(f"MACD：{latest['MACD']:.2f}")

# ======================
# 画图
# ======================
plt.figure(figsize=(12,6))
plt.plot(df["日期"], df["收盘"], label="price")
plt.legend()
plt.show()
