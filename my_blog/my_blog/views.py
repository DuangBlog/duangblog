from django.http import Http404
from django.shortcuts import render
import time,os
from django.http.response import HttpResponse
from my_blog import models
from django.db import connection
import markdown2

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOST = 'https://duangblog.com'
NAME = 'root'
PASSWORD = '9BEhUz95m4vjSJC&'

"""
    "Returns all rows from a cursor as a dict"
"""
def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

"""
    导入emoji名称到数据库
"""

def emojiToDatabase(request):
    if request.method !='GET':
        raise Http404
    emojiNamesFile = open('emojiNames.txt', 'r')
    try:

        for line in emojiNamesFile:
            line = line.replace('\n','')
            models.Emojis.objects.create(emojiName=line)

        return HttpResponse('success')
    except Exception as e:
        print(e)
        return HttpResponse('fail')
    finally:
        emojiNamesFile.close()

"""
    文章列表
"""
def articleList(request):
    if request.method != 'GET':
        raise Http404
    try:
        cursor = connection.cursor()
        cursor.execute(
            'select articles.id,articles.title,articles.abstract,articles.mdFileName,articles.createTime,emojis.emojiName from articles,emojis where articles.emojiId = emojis.id')
        articles = dictfetchall(cursor)

        for article in articles:
            article['emoji'] = '%s/static/%s'%(HOST,article['emojiName'])
            del article['emojiName']

        return render(request, 'articleList.html',{'articles':articles})
    except Exception as e:
        print(e)
        raise Http404


"""
    登录
"""

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method != 'POST':
        raise Http404
    try:
        name = request.POST.get('name','')
        password = request.POST.get('password','')

        if name != NAME or password != PASSWORD:
            return render(request, 'login.html')

        return render(request,'admin.html')

    except Exception as e:
        print(e)
        raise Http404

"""
    后台管理界面
"""
def admin(request):
    if request.method != 'POST':
        raise Http404
    try:
        title = request.POST.get('title')
        abstract = request.POST.get('abstract')
        emojiName = request.POST.get('emojiName')
        mdFileName = request.POST.get('mdFileName')
        createTime = int(time.time())

        if not title or not abstract or not mdFileName:
            return render(request,'admin.html',{'lackParam':True})

        emoji = None
        if not emojiName:
            emoji = models.Emojis.objects.values('id','emojiName').order_by('?')[:1]
        else:
            emojiList = models.Emojis.objects.filter(emojiName=emojiName)
            emojiList = list(emojiList)
            if len(emojiList) == 0:
                emoji = models.Emojis.objects.values('id','emojiName').order_by('?')[:1]
            else:
                emoji = emojiList[0]

        emoji = list(emoji)[0]
        emojiId = emoji['id']
        models.Articles.objects.create(title=title,abstract=abstract,emojiId=emojiId,mdFileName=mdFileName,createTime=createTime)

        return render(request, 'admin.html')
    except Exception as e:
        print(e)
        raise Http404


"""
    文章详情
"""
def articleDetail(request,articleId):
    if request.method != 'GET':
        raise Http404

    try:
        article = models.Articles.objects.filter(id=articleId)
        article = list(article)
        if len(article) == 0:
            raise Http404
        article = article[0]

        emojiName = models.Emojis.objects.filter(id=article.emojiId)
        emojiName = list(emojiName)[0]
        emoji = '%s/static/%s' % (HOST, emojiName.emojiName)

        contentFile = open(os.path.join(BASE_DIR, 'static/files/%s'%(article.mdFileName)),'r',encoding='UTF-8')
        content = contentFile.read()
        contentFile.close()

        content = markdown2.markdown(content, extras=["fenced-code-blocks", "cuddled-lists", "metadata", "tables", "spoiler"])
        return render(request,'articleDetail.html',{'title':article.title,'content':content,'emoji':emoji})


    except Exception as e:
        print(e)
        raise Http404
