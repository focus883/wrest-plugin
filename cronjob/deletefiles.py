
# @Name: 删除下载图片
# @Second: 0
# @Minute: 0
# @Hour: 1
# @DayOfMonth: *
# @Month: *
# @DayOfWeek: 3
# @Timeout: 300
# @Content: python.exe
# @Deliver: wechat,xxx@room,wxid_xxxx

import os 
import time
import sys  
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8') 

def delete_older_files(folder_path, days):
    # 获取当前时间
    current_time = time.time()
    count = 0
    # 计算时间上的差值，转换成秒
    time_difference = days * 24 * 60 * 60
    # 遍历指定文件夹下的所有文件
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        # 判断文件的修改时间是否在指定天数之前
        if os.path.isfile(file_path) and (current_time - os.path.getmtime(file_path)) > time_difference:
            # 删除文件
            os.remove(file_path) 
            count=count+1
    print(f"已删除文件数量:{count}")
# 调用函数删除指定文件夹下7天前的图片
folder_path = r"D:\wrest-windows\storage\chat-images"
days = 7 
delete_older_files(folder_path, days)


