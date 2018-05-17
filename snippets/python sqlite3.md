# python sqlite3

```python
# author: hy
# date: 2018-05-17
# 数据库操作
import sqlite3
import csv
import math
import json
db_table = 'ImageInfo'
db_file = "ImageInfo.db"

# 创建表 (imgname, width, height, tag)
# 其中, imgname 为文件名, 主键, 采用某个算法以大概率避免重复
#       height 为图片的高度
#       width 为图片的宽度
#       tag 为识别出来的图片的标签
# 只保存图片名, 图片的路径默认为 flaskapp.py 文件所在的目录下的 static/images/ 子目录
def createTable():
    with sqlite3.connect(db_file) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE %s
            (imgname text not null unique PRIMARY KEY,
            width int not null,
            height int not null,
            tag_classification text not null DEFAULT '',
            imagecaption text not null DEFAULT '',
            caption_score REAL not null default 0,
            tag_caption text not null DEFAULT '',
            tag_caption_score not null DEFAULT ''
                )''' % db_table)
        conn.commit()


# 插入图片, 成功返回真, 失败返回假
def insertImage(img_name, width, height):
    with sqlite3.connect(db_file) as conn:
        c = conn.cursor()
        try:
            c.execute(
                "INSERT into %s (imgname,width,height) VALUES ('%s',%d, %d)" %
                (db_table, img_name, width, height))
            conn.commit()
            return True
        except:
            return False


# 导出数据库为csv文件
def exportToCsv():
    with sqlite3.connect(db_file) as conn:
        c = conn.cursor()
        with open(db_table + '.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile)

            # iterate through the records
            for row in c.execute('SELECT * FROM %s' % db_table):
                (imgname, width, height, tag) = row
                spamwriter.writerow([imgname, width, height, tag])


# 更新编号为id的图片的tag
def insertTag(imgname, tag):
    with sqlite3.connect(db_file) as conn:
        c = conn.cursor()
        c.execute("UPDATE %s SET tag_classification='%s' WHERE imgname='%s'" %
                  (db_table, tag, imgname))
        conn.commit()


def insertCaptionTag(imgname, captions, caption_score, tags, tag_scores):
    with sqlite3.connect(db_file) as conn:
        c = conn.cursor()

        c.execute(
            "UPDATE %s SET imagecaption='%s',caption_score = '%f',tag_caption='%s',tag_caption_score = '%s' WHERE imgname='%s'"
            % (db_table, captions, caption_score, tags, tag_scores, imgname))
        conn.commit()


pagesize = 2

# 按页，按条件查询结果
def generateJson(page, tags):
    try:
        page = int(page)
    except:
        return
    sqltagstring = ''
    if len(tags):
        sqltagstring = [
            "tag_classification like '%%%s%%' or imagecaption like '%%%s%%'" %
            (tag, tag) for tag in tags
        ]
        sqltagstring = ' and '.join(sqltagstring)
        sqltagstring = 'WHERE ' + sqltagstring
    ret = dict()
    result = list()
    with sqlite3.connect(db_file) as conn:
        c = conn.cursor()
        sqlstr = "(SELECT * FROM %s %s)" % (db_table, sqltagstring)
        totalitem = c.execute(
            "SELECT COUNT(*) FROM (%s)" % sqlstr).fetchone()[0]
        totalpage = math.ceil(totalitem / pagesize)
        for row in c.execute("select * from (%s)  limit %d OFFSET %d" %
                             (sqlstr, pagesize, (page - 1) * pagesize)):
            # print(row)
            (imgname, width, height, tag_classification, imagecaption,
             caption_score, tag_caption, tag_caption_score) = row
```

## 参考

[Python标准库14 数据库 (sqlite3) - Vamei - 博客园](http://www.cnblogs.com/vamei/p/3794388.html)