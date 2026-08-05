import datetime as DT # 取得目前的日期與時間
nowTime = DT.datetime.now()
print('{:%Y/%b/%d  %A}'.format(nowTime))
print(f'{nowTime:%Y/%b/%d  %A}') # 使用 f-string 格式化
print(nowTime.strftime('%Y/%b/%d  %A')) # 使用 strftime 方法格式化