import pymysql
import urllib.request
import datetime
from bs4 import BeautifulSoup
import traceback
import threading
import time

class myThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print ("开始线程：" + self.name)
        # 打开数据库连接
        db = pymysql.connect("localhost","root","root","dictionary",charset="utf8mb4")
        # 使用cursor()方法获取操作游标 
        cursor = db.cursor()

        select(db,cursor)

        #关闭游标
        cursor.close()
        #关闭数据库连接
        db.close()
        print ("退出线程：" + self.name)


def select(db,cursor):#取出查找关键词
    # SQL 查询语句
    sql = "SELECT ENGLISH FROM ENGLISH_CHINESE "
    var = -1
    try:
        #print (1)
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for string in results:
            var = spider(db,cursor,string)
            print (string)
            if var == 0:
                continue
        #print (2)
    except:
        traceback.print_exc() 
        print ("Error: unable to fecth data")


def spider(db,cursor,word):#爬取数据
    try:
        #print (3)
        url = 'http://www.thesaurus.com/browse/%s?s=t' % word
        html = urllib.request.urlopen(url,timeout = 12).read()
        soup = BeautifulSoup(html,"html.parser")
        var = -1
        for string in soup.select('div[class=synonyms] a[class=common-word] span[class=text]') :
            string =  string.get_text()
            var = insert(db,cursor,word,string)
            if var == 0:
                continue
        #print (4)
        return 1
    except:
        print ("spider false")
        traceback.print_exc() 
        return 0

def insert(db,cursor,word,string):#将爬到的数据插入数据库
    sql = "INSERT INTO EN_SYNONYMS(ENGLISH,SYNONYMS,FK_ENGLISH_BASE_ENGLISH,FK_SYNONYMS_BASE_ENGLISH,SYNONYMS_CHINESE) VALUES ('%s', '%s', 0, 0, 'null')" % (word[0],string)
    try:
       #print (5)
       # 执行sql语句
       cursor.execute(sql)
       # 执行sql语句
       db.commit()
       print('insert successfully')
       #print (6)
       return 1

    except:
       # 发生错误时回滚
       db.rollback()
       print('insert false')
       traceback.print_exc() 
       return 0


if __name__ =="__main__":
    starttime = datetime.datetime.now()


    #select(db,cursor)
    thread1 = myThread(1, "Thread-1")
    thread2 = myThread(2, "Thread-2")
    thread3 = myThread(3, "Thread-3")
    thread4 = myThread(4, "Thread-4")

    # 开启新线程
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    endtime = datetime.datetime.now()

    print (endtime - starttime)

