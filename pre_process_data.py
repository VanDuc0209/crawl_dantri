import json
with open('./dantri.json', 'r') as f:
    datas = json.load(f)

# for data in datas:
#     title1 = data['title1']
#     title1 = " ".join(title1.split())
#     print(title1)
#     tmps = title1.split(" ")
#     print(tmps)

result = []
for data in datas:
    link = data['link']
    title = data['title']
    title = " ".join(title.split())
    title1 = data['title1']
    title1 = " ".join(title1.split())
    content = data['content']
    content = " ".join(content.split())
    author = data['author']
    author = " ".join(author.split())
    topic = data['topic']
    _tags = data['tags']
    tags = []
    for tag in _tags:
        tag = " ".join(tag.split())
        tags.append(tag)
    datetime_post = data['datetime']
    datetime_post = " ".join(datetime_post.split())
    datetime_crawl = data['datetime_crawl']
    # print(link)
    # print(title)
    # print(title1)
    # print(content)
    # print(tags)
    # print(datetime)
    # print(datetime_crawl)
    item = {
            'link': link,
            'title': title,
            'title1': title1,
            'content': content,
            'author': author,
            'topic': topic,
            'tags':tags,
            'datetime_post': datetime_post,
            'datetime_crawl': datetime_crawl
        }
    result.append(item)
    
with open('dantri_result.json', 'w') as f:
    json.dump(result, f)