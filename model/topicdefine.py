from utils.query import query
from utils.getPublicData import *
articleList = getAllArticleData()
commentList = getAllCommentsData()

def column_exists(table_name, column_name):
    sql = "SHOW COLUMNS FROM {} LIKE %s".format(table_name)
    params = [column_name]
    result = query(sql, params, type='select')
    return len(result) > 0
# 添加新的标注列
def add_label_article(): # 为文章添加标注列
    if not column_exists('article', 'label'):
        sql = "ALTER TABLE article ADD COLUMN label TEXT NULL"
        params = []
        query(sql, params)

def add_label_comments(): # 为评论添加标注列
    if not column_exists('comments', 'label'):
        sql = "ALTER TABLE comments ADD COLUMN label TEXT NULL"
        params = []
        query(sql, params)

def drop_label():# 删除标注列
    sql = "ALTER TABLE article DROP COLUMN label "
    params = []
    query(sql, params)

def drop_label1():# 删除标注列
    sql = "ALTER TABLE comments DROP COLUMN label "
    params = []
    query(sql, params)


# 处理数据并添加标注
def process_data(data):
    processed_data =testmodel(data)
    return processed_data

def testmodel(test):
    return "wicao"

def topicdefine():
    label_article=[]
    label_comments=[]
    for x in articleList:
        label_article.append((x[0],process_data(x[5])))
    for x in commentList:
        label_comments.append((x[5],process_data(x[4])))
    return label_article,label_comments

# 更新数据库
def update_data(label_article,label_comments):
    add_label_comments()
    add_label_article()
    for row in label_article:
        id, label = row
        sql = "UPDATE article SET label = %s WHERE id = %s"
        params = [str(label),str(id)]
        query(sql, params)
    for row in label_comments:
        label, id = row
        sql = "UPDATE comments SET label = %s WHERE authorName = %s"
        params = [str(label),str(id)]
        query(sql, params)

# x,y=topicdefine()
# update_data(x,y)
drop_label()
drop_label1()