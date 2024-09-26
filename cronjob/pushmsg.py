

# @Name: 每日简报
# @Second: 0
# @Minute: 0
# @Hour: 9
# @DayOfMonth: *
# @Month: *
# @DayOfWeek: *
# @Timeout: 300
# @Content: python.exe
# @Deliver: wechat,xxx@room,wxid_xxxx

import pandas as pd
import sys  
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8') 

def read_excel_first_column(file_path):
    # 尝试读取Excel文件
    try:
        # 使用pandas的read_excel函数读取文件
        # 假设Excel文件的第一行是列名，我们不需要设置header参数
        # 如果第一行不是列名，可以设置header=None
     
        df = pd.read_excel(file_path,header=None)
        
        # 读取第一列的数据，这里假设列名未知，所以使用iloc[:, 0]
        # 如果知道列名，可以直接使用df['列名']
        first_column_data = df.iloc[:, 0].tolist()  # 将第一列的数据转换成列表
        
        # 打印第一列的数据
        print("")
        for data in first_column_data:
            print(data)
    
    except FileNotFoundError:
        print(f"大家好1")
    except Exception as e:
        print(f"大家好")

# 指定Excel文件的路径
file_path = r'D:\简报\影刀简报数据.xlsx'

# 调用函数
read_excel_first_column(file_path)

