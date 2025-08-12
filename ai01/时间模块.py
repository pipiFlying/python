import time

# time.time() 返回以浮点数表示的从 epoch 开始的秒数形式的时间
# 检测程序运行时间
start = time.time()
print(start)

# time.sleep(secs) 调用方线程暂停执行给定的秒速。该参数可以给定浮点数以精确控制
print('开始')
# time.sleep(6) # 阻塞6s后输出结束
print('结束')

# time.gmtime() 返回从 epoch 开始 UTC 结构时间
ta = time.gmtime()
print(ta)

# time.localtime() 与gmtime相似，相差8小时
tb = time.localtime()
print(tb)

# time.strftime(format[,t]) 转换一个元组或者struct_time 由format格式指定的字符串如果未提供t,则使用由locatime()返回的
# 当前时间，format必须是一个字符串
tc = time.strftime('%Y-%m-%d %H:%M:%S', tb)
print(tc)

# 传入的t
# 传值可查询 python 文档
td = time.strftime('%Y-%m-%d %H:%M:%S', (2025, 8, 5, 10, 58, 52, 1, 8, 0))
print(td)
