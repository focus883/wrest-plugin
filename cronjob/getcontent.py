
# @Name: 获取简报
# @Second: 0
# @Minute: 0
# @Hour: 3
# @DayOfMonth: *
# @Month: *
# @DayOfWeek: *
# @Timeout: 300
# @Content: python.exe
# @Deliver: 

import sys  
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import sqlite3  
#import datetime  
from datetime import datetime, timedelta
from bs4 import BeautifulSoup 
  
def find_recent_messages_with_keyword(db_path, keyword, limit=1):  
    """  
    查询指定SQLite数据库中的最近10条包含特定关键词的ChatMsg记录。  
  
    :param db_path: 数据库文件的路径  
    :param keyword: 要搜索的关键词  
    :param limit: 返回的记录数限制，默认为10  
    :return: None，但会打印查询结果  
    """  
    # 连接到SQLite数据库  
    # 如果数据库文件不存在，sqlite3会自动在当前目录创建:  
    conn = sqlite3.connect(db_path)  
      
    # 创建一个Cursor对象并使用它来执行查询  
    cur = conn.cursor()  
      
    # SQL查询语句，假设ChatMsg表中有一个名为'Content'的列包含消息内容  
    # 并且有一个名为'Timestamp'（或任何实际存储时间戳的列名）的列来排序  
    query = """  
    SELECT * FROM message  
    WHERE sender LIKE ?  
    ORDER BY ts DESC  
    LIMIT ?  
    """  
      
    # 注意：LIKE操作符中的%是通配符，表示任意字符序列，不加%表示精确查找
    # 第二个参数是LIMIT的数量  
    # cur.execute(query, ('%' + keyword + '%', limit))  
    cur.execute(query, (keyword, limit))
      
    # 获取所有匹配的行  
    rows = cur.fetchall()  
      
    # 打印查询结果  
    for row in rows:  
        # 假设你的表结构中有ID, Timestamp, Content等列  
        # 根据实际情况调整下面的打印语句  
        senderID = row[8]
        re_time = row [5]
        content = row [7]
        dt_object = datetime.fromtimestamp(re_time)
        now = datetime.now()  
        if dt_object.date() == now.date(): 
 
            #写入文件
            file_path = r'D:\简报\newslink.xml'
            with open(file_path, "w", encoding="utf-8") as file:  
                file.write(content)	
				
            print(f"公众号: {senderID}, 接收时间: {dt_object}, 获取简报成功") 				
        else :
           print("时间不对，请检查源文件")
      
    # 关闭Cursor和Connection  
    cur.close()  
    conn.close()  
  
# 使用函数  
db_path = 'D:\wrest-windows\storage\wrest.db3'  # 替换为你的数据库文件路径  
keyword = 'gh_aa0dee3d8e84'  
find_recent_messages_with_keyword(db_path, keyword)


def find_xml_with_keyword(file_path2,keyword2): 
    # 步骤1: 打开文件以读取内容  
    with open(file_path2, 'r', encoding='utf-8') as file:  
        content_item = file.read()  # 读取内容
        # 使用BeautifulSoup解析文本  

        soup = BeautifulSoup(content_item, 'html.parser')  
  
        # 查找所有<item>标签，并检查其内容是否包含关键字  
        for item in soup.find_all('item'): 
            #print("Item text:", item.get_text(strip=True))

            #print(item.prettify()) 	
            title_tag = item.find('title') 	
            if title_tag and keyword2 in title_tag.text:  # 检查<title>标签的文本是否包含's' 			
                # 如果包含，则查找对应的<url>标签并提取链接
                url_tag	= item.find('url') 				
                if url_tag:  
                    print(f"Found {keyword2} in title: {title_tag.text}, URL: {url_tag.text}")  
                    # 如果找到包含关键字的<item>，则提取其内容  
                    with open(file_path3, "w", encoding="utf-8") as file:  
                        file.write(url_tag.text)

            else :
               print("未找到关键信息")
		   
# 使用函数  
file_path2 = r'D:\简报\newslink.xml'  # 替换为你的数据库文件路径  
file_path3 = r'D:\简报\newsurl.txt'  # 替换为你的数据库文件路径  
keyword2 = '星期'    # 定义要搜索的关键字
find_xml_with_keyword(file_path2, keyword2)	   
