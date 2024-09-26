# 这是今日头条热榜
# 插件开发语言不限于 node.js，只要添加下列注释参数，并设置正确的 @Target 作为解析器即可

# @Roomid: *
# @Phrase: toutiaohot
# @Level: 9
# @Target: python.exe
# @Remark: 今日头条热榜

import requests  
import json 
import sys  
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8') 
  
def fetch_hot_news():  
    # API URL  
    url = 'https://wrest.rehi.org/news/toutiao'  
      
    # 发送GET请求  
    response = requests.get(url)  
      
    # 检查请求是否成功  
    if response.status_code == 200:  
        # 解析JSON响应  
        data = response.json()  
        content = data.get('text')
        print(content)

    else:  
        print(f"请求失败，状态码: {response.status_code}")  
  
if __name__ == "__main__":  
    fetch_hot_news()
