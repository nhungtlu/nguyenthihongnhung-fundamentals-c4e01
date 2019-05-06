# import requests
# import json
# import bs4
# url ='https://dantri.com.vn/suc-khoe.htm'

# response = requests.get(url)
# # print(response.content)

# bs = bs4.BeautifulSoup(response.content,'html.parser')
# # print(bs.title)
# all_a_tag = bs.find_all('div',{'data-boxtype':"timelineposition"})
# data_crawler = []
# for v in all_a_tag:
#     post ={}
#     post[ 'title'] = v.div.h2.a.attrs['title']
#     post ['img ']= v.a.img.attrs['src']
#     post ['text'] = v.div.div.text
#     data_`crawler.append(post)
#     # print(v.div.h2.a.attrs['title'])
#     # print(v.a.img.attrs['src'])
#     # print(v.div.div.text)
#     # print()
#     # print()
#     with open('data.json','wt',encoding = 'utf-8') as f:
#         f.write(json.dumps(data_crawler,ensure_ascii = False, indent = 2))

    
# # print(len(all_a_tag))

# # print(all_a_tag)



from bs4 import BeautifulSoup

x = BeautifulSoup.find_all('div',{'data':'tin_tuc'})
x =list(x)
# print(list(x[0].children)) # dùng để xác định mọt thẻ div dễ nhớ 
exit(0)
print(...)
print(...)

html = """
<!DOCTYPE html>
<html>
<title>Trang web của tôi</title>
<body>
    <h1>Chào mừng đến với Techkids</h1>
    <p id='data'>Xin chào</p>
    <p>python</p>
    <p>c#</p>
    <p>java</p>
    
    <div>
        <div  data="tin_tuc">
            <a href='http://google.com'>Tự động hóa xét nghiệm, giảm chờ đợi cho người bệnh</a>
            <div>   
                <p>Bệnh viện Chợ Rẫy vừa đưa hệ thống xét nghiệm tự động hóa hoàn toàn thứ 2 </p>
            </div>
        </div>
        <div  data="tin_tuc">
            <a href='http://google.com'>Bất ngờ với những lợi ích sức khỏe khi ăn ớt</a>
            <div>   
                <p>Có rất nhiều lý do tốt để thêm ớt vào chế độ ăn và con số này tiếp tục tăng lên </p>
            </div>
        </div>
    </div>
 
</body>
</html>
"""

 # Sau dòng này thì soup chính là cả document.
print("------------Lấy title:", BeautifulSoup.title)  # do title là con đầu tiên của document
print("------------Lấy riêng text của title",BeautifulSoup.title.string) # .string sẽ lấy ra nội dung text của thẻ

# .p sẽ ra thẻ đầu tiên nó tìm thấy, .attrs sẽ trả về dic các thuộc tính
print("------------lấy các thuộc tính của thẻ p đầu tiên:", BeautifulSoup.p.attrs)

# do soup.p.attrs là dic, nên lấy theo key là 'id'
print("------------lấy thuộc tính id của thẻ p đầu tiên:", BeautifulSoup.p.attrs['id'])


print('------------tìm thẻ p đầu tiên:', BeautifulSoup.find('p'))
print('------------lấy tất cả các thẻ p:', BeautifulSoup.find_all('p'))

print('------------Lấy các bài viết')
# Tìm tất cả các thẻ div mà có thuộc tính data = 'tin_tuc'
list_all_post = BeautifulSoup.find_all('div', {'data': "tin_tuc"})
for v in list_all_post:
    print( v.a.text) # Lấy text của thẻ a trong bài viết
    print( v.div.p.text) # lấy phần nội dung của bài viết trong thẻ p, lưu ý đường dẫn tính từ thẻ div có data = 'tin_tuc'
    print()

