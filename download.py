#多页爬取

'''
需要环境
requests，parsel（xpath）

步骤
1.确定url地址
2.发送请求
3.解析数据（数据筛选）<两层数据解析>
4.保存数据（本地文件）
'''

#requests实现帮助请求数据的要求
import requests
import parsel
#
# page_num = 0
# #换页
# for page in range(0,55000+1,50):
#     page_num+=1
#     print('===========================正在爬取第{}页数据===================='.format(str(page_num)))
#     #1.确定url地址
#     #先确定它是静态网页还是动态网页
#     #静态网页：源代码都有网页的数据，并且没有经过浏览器的渲染以及加载
#     #判断静态数据：在源代码中搜索的到
#     url = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E5%B9%BB%E5%BD%B1%E5%9D%A6%E5%85%8B&fr=searchpn={}'.format(str(page))
#     #之后准备请求参数
#     #刷新页面后，Chrome的Network栏所有的数据包都可以呈现
#     #user-agent更换为了ie浏览器，方便后面的操作
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WoW64; Trident/7.0; rv:11.0) like Gecko'}
#
#     #2.发送请求
#     response = requests.get(url,headers=headers)
#     #状态码：200左右表示请求成功，300左右表示重定向，400左右表示URL地址有错误，500左右表示服务器错误
#     html_data = response.text #字符串类型数据，只能使用正则表达式
#     #print(html_data)
#
#     #3.解析数据（数据筛选）<两层数据解析>
#     #为了获得最高清的图片，而不是缩略图
#     #数据解析第一层：解析所有帖子的《链接》
#     #将字符串数据转换成Selector对象；该对象有re（正则表达式），css选择器，xpath路径选择器
#     html = parsel.Selector(html_data)
#     #print(html)
#     #两个/（双斜杠）表示跨节点提取，[@...]通过标签的属性值进行精确定位，标签层级递增的关系/div/a...，取到标签后获得href属性
#     #同样也返回Selector对象，getall提取出解析到的数据
#     title_url = html.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href').getall()
#     #部分url的地址，和前面的地址拼接起来去实现
#     #print(title_url) #['/p/7203233304', '/p/7197583050'...]
#
#     #拼接url地址
#     #前半部分的url
#     second_url = 'https://tieba.baidu.com'
#     for url in title_url:
#         all_url = second_url + url
#         print('当前的帖子链接为：', all_url)
#
#         # 第二层：再发送一次url请求，获得页面数据，随后解析出图片地址
#         #再次发送请求，请求帖子内部的数据
#         response_2 = requests.get(url=all_url,headers=headers).text
#         #第二次解析
#         response_2_data = parsel.Selector(response_2)
#         result_list = response_2_data.xpath('//cc/div/img[@class="BDE_Image"]/@src').getall()
#         #print(result_list) #['http://tiebapic.baidu.com/forum/w%3D580/sign=d941e7678413b07ebdbd50003cd69113/4d456709c93d70cf1974ca4befdcd100bba12b60.jpg', 'http://tiebapic.baidu.com/forum/w%3D580/sign=b6dbbb9a1ffa513d51aa6cd60d6c554c/b74ee5dde71190ef5192bc99d91b9d16fcfa6081.jpg']
#
#         for li in result_list:
#             #图片数据，需要content（二进制数据）
#             img_data = requests.get(url=li,headers=headers).content
#             #4.保存数据（本地文件）
#             #图片的文件名和后缀
#             #'http://tiebapic.baidu.com/forum/w%3D580/sign=d941e7678413b07ebdbd50003cd69113/4d456709c93d70cf1974ca4befdcd100bba12b60.jpg'
#             file_name = li.split('/')[-1]
#             #\\表示把文件保存到该文件夹下，mode文件写入方式(二进制wb)
#             with open('img\\'+file_name,mode='wb') as f:
#                 f.write(img_data)
#                 print("正在保存：",file_name)

li = 'http://tiebapic.baidu.com/forum/w%3D580/sign=7e8fe284eb039245a1b5e107b795a4a8/5ea6ab2542a7d93375d4f03aba4bd11373f00115.jpg'
li = li[0:len('http://tiebapic.baidu.com/forum/')]+'pic/item/'+li[li.rfind('/')+1:]
img_data = requests.get(url=li,headers=headers).content
file_name = li.split('/')[-1]
# \\表示把文件保存到该文件夹下，mode文件写入方式(二进制wb)
with open('test\\' + file_name, mode='wb') as f:
    f.write(img_data)
    print("正在保存：", file_name)