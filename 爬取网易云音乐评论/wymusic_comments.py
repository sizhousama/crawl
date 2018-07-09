
#第一步 导入模块
import requests
import json
from bs4 import BeautifulSoup



def get_hot_comments(res):
    comments_json = json.loads(res.text)
    hot_comments = comments_json['hotComments']
    with open('hot_comments.txt','w',encoding = 'utf-8') as f:
        for each in hot_comments:
            f.write(each['user']['nickname'] + ':\n\n')
            f.write(each['content'] + '\n')
            f.write('---------------------------------\n')

# 第三步 定义爬取方法函数
def get_comments(url):
    #获取自定义页面的分割方法，视url不同而定
    name_id = url.split('=')[1]


    #1.定义头
    headers = {

        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Referer': 'https://music.163.com/song?id=525278524'
        }
    #动态页面抓取的必要条件 params encseckey
    params = 'sI33x4ZJp4PmPbw20V9IpJga5LV/0LFE23ma06MFAZSDt+LFZAUKh0G57k7HLIxVyPdq7ig3Jh025s9aC3wLThV5SS9iaY8NvLCDNWI0l8SWou3EsnhnB7yMsXjb0wVAXYJMhF2YSDXn5/sAYpuzijnvn7YK+JSc8LAokTGpAlrPlzPHhpFf24PbY8RZMu0d'

    encSecKey = '7873150aea07e625affdbbd9972059af03274969ce19de74f6bc97003e54efd976e7017fcaec6f4f913581004021f054c175a8512ed3a521a01299da96722893ed4ce032d8b6af19570f3e2050e17d6d413513a6d191ec2aab03596842aff12cb72022a6737580df951444d48035631eebeeaec7611d24cb2bd5feae1ca4732e'
    #以字典的方式传给request
    data = {
        'params' : params,
        'encSecKey' : encSecKey
        }    

    
    #动态页面的 url
    target_url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token='.format(name_id)
    # 获取页面 post or get
    res = requests.post(target_url,headers = headers,data=data)

    return res


# 第二步 定义主函数
def main():
    url = input("请输入链接地址：")
   
    #获取 url
    res = get_comments(url)

    #以txt文件将获取到的页面保存
    with open('res.txt','w',encoding = 'utf-8') as f:
        f.write(res.text)
        get_hot_comments(res)
    


if __name__ == '__main__':
    main()
