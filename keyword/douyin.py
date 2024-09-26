#抖音热搜插件
# @Roomid: *
# @Phrase: douyinHot
# @Level: 9
# @Target: python.exe
# @Remark: 抖音热搜

import requests  
import json 
import sys  
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8') 
  
def fetch_hot_news():  
    # API URL  
    url = 'https://api.vvhan.com/api/hotlist/douyinHot'  
      
    # 发送GET请求  
    response = requests.get(url)  
      
    # 检查请求是否成功  
    if response.status_code == 200:  
        # 解析JSON响应  
        data = response.json()  
        a =1        
        # 检查操作是否成功  
        if data.get('success'):  
            # 遍历新闻数组  
            for news_item in data.get('data', [])[:10]: 
                # 假设每条新闻至少有一个'title'键  
                title = news_item.get('title', '未知标题') 
                hot = news_item.get('hot', '未知标题') 	
                #url = news_item.get('url', '未知标题') 				

                # 这里可以根据需要添加其他字段的解析，比如'content'、'summary'等  
                # 例如：content = news_item.get('content', '无具体内容')  
                  
                # 打印新闻标题（和其他你感兴趣的字段）  
                print(f"{a}: {title}",f"🔥热度: {hot}") 
                #print(f"热度: {hot}") 
                #print(f"链接: {url}\n") 
                a=a+1
                # 如果新闻有内容或其他字段，也可以打印出来  
                # print(f"新闻内容: {content}")  
                #print("-" * 50)  # 打印分隔线以便区分不同的新闻  
        else:  
            print("API调用成功，但返回的数据表明操作未成功。")  
    else:  
        print(f"请求失败，状态码: {response.status_code}")  
  
if __name__ == "__main__":  
    fetch_hot_news()
