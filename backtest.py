import pyupbit
import numpy as np

#OHLCV란 당일 시가, 고가, 저가, 종가, 거래량에 대한 데이터
df = pyupbit.get_ohlcv("KRW-BTC", count = 14)

df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)

# 수익률 np.where(조건문, 참일 때, 거짓일 때)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)
# 누적 곱 계산 => 누적 수익률
df['hpr'] = df['ror'].cumprod()

# Draw down(하락폭) 계산 => 가장 높은 누적 수익율 - 현재 수익율을 가장 높은 누적 수익율로 나눔
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['dd'].max())
df.to_excel("dd.xlsx")