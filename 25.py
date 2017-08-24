import pymysql
import urllib.request
import datetime
from bs4 import BeautifulSoup
import traceback

def select(db,cursor):
    # SQL 查询语句
    #sql = "SELECT ENGLISH FROM ENGLISH" 
    sql = "SELECT ENGLISH FROM ENGLISH_CHINESE WHERE ID > 1105"
    var = -1
    try:
        print (1)
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for string in results:
            var = spider(db,cursor,string)
            print (string)
            if var == 0:
                continue
        print (2)
    except:
        traceback.print_exc() 
        print ("Error: unable to fecth data")
    #cursor.close()
    #db.close()

def spider(db,cursor,word):
    try:
        print (3)
        url = 'http://www.thesaurus.com/browse/%s?s=t' % word
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html,"html.parser")
        var = -1
        for string in soup.select('div[class=synonyms] a[class=common-word] span[class=text]') :
            string =  string.get_text()
            var = insert(db,cursor,word,string)
            if var == 0:
                continue
        print (4)
        return 1
    except:
        print ("spider false")
        traceback.print_exc() 
        return 0

def insert(db,cursor,word,string):
    #sql = "INSERT INTO ENGLISH_SYNONYMS(ENGLISH,SYNONYMS) VALUES ('%s', '%s' )" % (word[0],string)
    sql = "INSERT INTO EN_SYNONYMS(ENGLISH,SYNONYMS,FK_ENGLISH_BASE_ENGLISH,FK_SYNONYMS_BASE_ENGLISH,SYNONYMS_CHINESE) VALUES ('%s', '%s', 0, 0, 'null')" % (word[0],string)
    try:
       print (5)
       # 执行sql语句
       cursor.execute(sql)
       # 执行sql语句
       db.commit()
       print('insert successfully')
       print (6)
       return 1

    except:
       # 发生错误时回滚
       db.rollback()
       print('insert false')
       traceback.print_exc() 
       return 0
    # 关闭数据库连接
    #db.close()

if __name__ =="__main__":
    starttime = datetime.datetime.now()
    # 打开数据库连接
    #db = pymysql.connect("localhost","root","root","test",charset="utf8mb4")
    db = pymysql.connect("localhost","root","root","dictionary",charset="utf8mb4")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()

    select(db,cursor)

    cursor.close()
    db.close()
    endtime = datetime.datetime.now()

    print (endtime - starttime)

