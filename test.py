import pyupbit

access = "B3btCOI420ambV5vq5QhXdyo2pugarwpqGe998nV"          # 본인 값으로 변경
secret = "5j47xiFPvzSrSmEvPgoxAbyATxxxuWEEp4h75Jfg"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회