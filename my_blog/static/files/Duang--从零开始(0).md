# Duang Blog -- 从零开始（0）

**pre：**边搭边记。


## 开始

- **本博客简单实现下列三个页面，后续再慢慢优化**
	+ 首页
	+ 详情页
	+ 上传文章页

<img src="https://duangblog.com/static/myblog_0_1.png" style="width:100%"/>
<img src="https://duangblog.com/static/myblog_0_2.png" style="width:100%"/>
<img src="https://duangblog.com/static/myblog_0_3.png" style="width:100%"/>

- **数据库**

 ```c
 文章表
	 id
	 title
	 abstract
	 emojiId
	 mdFileName
	 createTime
 ```

 ```c
emoji表
	id
	emojiName
 ```

>如果我们使用了Django的model，它会自动在每张表帮我们生成id；
>在列表的每个单元随机放个emoji图片感觉不错；
>这里不打算把文章的内容放在数据库，数据量不大，放不放数据库都可以。

- **用Pycharm新建一个新的Django项目，不打算用Django自带的后台管理界面**
<img src="https://duangblog.com/static/myblog_win_7_11_4.png" style="width:100%"/>

修改settings.py中的INSTALLED_APPS和MIDDLEWARE：

```python
INSTALLED_APPS = [
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'my_blog',
]
MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	# 'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static/emojis'),
    os.path.join(BASE_DIR,'static/css'),
    os.path.join(BASE_DIR,'static/files'),
)

```
- **在项目下新建static/css、static/emojis、static/files**

>在emojis目录下添加一些emoji图片,files目录用来存放markdown格式的文件

在static/css中新建vim.css

```css
.codehilite .hll { background-color: #222222 }
.codehilite  { background: #000000; color: #cccccc }
.codehilite .c { color: #000080 } /* Comment */
.codehilite .err { color: #cccccc; border: 1px solid #FF0000 } /* Error */
.codehilite .esc { color: #cccccc } /* Escape */
.codehilite .g { color: #cccccc } /* Generic */
.codehilite .k { color: #cdcd00 } /* Keyword */
.codehilite .l { color: #cccccc } /* Literal */
.codehilite .n { color: #cccccc } /* Name */
.codehilite .o { color: #3399cc } /* Operator */
.codehilite .x { color: #cccccc } /* Other */
.codehilite .p { color: #cccccc } /* Punctuation */
.codehilite .ch { color: #000080 } /* Comment.Hashbang */
.codehilite .cm { color: #000080 } /* Comment.Multiline */
.codehilite .cp { color: #000080 } /* Comment.Preproc */
.codehilite .cpf { color: #000080 } /* Comment.PreprocFile */
.codehilite .c1 { color: #000080 } /* Comment.Single */
.codehilite .cs { color: #cd0000; font-weight: bold } /* Comment.Special */
.codehilite .gd { color: #cd0000 } /* Generic.Deleted */
.codehilite .ge { color: #cccccc; font-style: italic } /* Generic.Emph */
.codehilite .gr { color: #FF0000 } /* Generic.Error */
.codehilite .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.codehilite .gi { color: #00cd00 } /* Generic.Inserted */
.codehilite .go { color: #888888 } /* Generic.Output */
.codehilite .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.codehilite .gs { color: #cccccc; font-weight: bold } /* Generic.Strong */
.codehilite .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.codehilite .gt { color: #0044DD } /* Generic.Traceback */
.codehilite .kc { color: #cdcd00 } /* Keyword.Constant */
.codehilite .kd { color: #00cd00 } /* Keyword.Declaration */
.codehilite .kn { color: #cd00cd } /* Keyword.Namespace */
.codehilite .kp { color: #cdcd00 } /* Keyword.Pseudo */
.codehilite .kr { color: #cdcd00 } /* Keyword.Reserved */
.codehilite .kt { color: #00cd00 } /* Keyword.Type */
.codehilite .ld { color: #cccccc } /* Literal.Date */
.codehilite .m { color: #cd00cd } /* Literal.Number */
.codehilite .s { color: #cd0000 } /* Literal.String */
.codehilite .na { color: #cccccc } /* Name.Attribute */
.codehilite .nb { color: #cd00cd } /* Name.Builtin */
.codehilite .nc { color: #00cdcd } /* Name.Class */
.codehilite .no { color: #cccccc } /* Name.Constant */
.codehilite .nd { color: #cccccc } /* Name.Decorator */
.codehilite .ni { color: #cccccc } /* Name.Entity */
.codehilite .ne { color: #666699; font-weight: bold } /* Name.Exception */
.codehilite .nf { color: #cccccc } /* Name.Function */
.codehilite .nl { color: #cccccc } /* Name.Label */
.codehilite .nn { color: #cccccc } /* Name.Namespace */
.codehilite .nx { color: #cccccc } /* Name.Other */
.codehilite .py { color: #cccccc } /* Name.Property */
.codehilite .nt { color: #cccccc } /* Name.Tag */
.codehilite .nv { color: #00cdcd } /* Name.Variable */
.codehilite .ow { color: #cdcd00 } /* Operator.Word */
.codehilite .w { color: #cccccc } /* Text.Whitespace */
.codehilite .mb { color: #cd00cd } /* Literal.Number.Bin */
.codehilite .mf { color: #cd00cd } /* Literal.Number.Float */
.codehilite .mh { color: #cd00cd } /* Literal.Number.Hex */
.codehilite .mi { color: #cd00cd } /* Literal.Number.Integer */
.codehilite .mo { color: #cd00cd } /* Literal.Number.Oct */
.codehilite .sa { color: #cd0000 } /* Literal.String.Affix */
.codehilite .sb { color: #cd0000 } /* Literal.String.Backtick */
.codehilite .sc { color: #cd0000 } /* Literal.String.Char */
.codehilite .dl { color: #cd0000 } /* Literal.String.Delimiter */
.codehilite .sd { color: #cd0000 } /* Literal.String.Doc */
.codehilite .s2 { color: #cd0000 } /* Literal.String.Double */
.codehilite .se { color: #cd0000 } /* Literal.String.Escape */
.codehilite .sh { color: #cd0000 } /* Literal.String.Heredoc */
.codehilite .si { color: #cd0000 } /* Literal.String.Interpol */
.codehilite .sx { color: #cd0000 } /* Literal.String.Other */
.codehilite .sr { color: #cd0000 } /* Literal.String.Regex */
.codehilite .s1 { color: #cd0000 } /* Literal.String.Single */
.codehilite .ss { color: #cd0000 } /* Literal.String.Symbol */
.codehilite .bp { color: #cd00cd } /* Name.Builtin.Pseudo */
.codehilite .fm { color: #cccccc } /* Name.Function.Magic */
.codehilite .vc { color: #00cdcd } /* Name.Variable.Class */
.codehilite .vg { color: #00cdcd } /* Name.Variable.Global */
.codehilite .vi { color: #00cdcd } /* Name.Variable.Instance */
.codehilite .vm { color: #00cdcd } /* Name.Variable.Magic */
.codehilite .il { color: #cd00cd } /* Literal.Number.Integer.Long */
```

运行--->浏览器输入http://127.0.0.1:8000/--->It worked!

## code
- **首页** 


在项目的templates目录下新建一个articleLists.html文件，先弄一段测试代码


```html
<!DOCTYPE html>
<html lang="en">
<head>
   	<meta charset="UTF-8">
   	<title>文章列表</title>
</head>
<body>
<ul>
   	<li>
   	    <a>C++基础</a>
   	    <p>
   	    C++...
   	    </p>
   	</li>
</ul>
<ul>
   	<li>
   	    <a>C语言基础</a>
   	    <p>
   	    C语言...
   	    </p>
   	</li>
</ul>
<ul>
   	<li>
   	    <a>iOS runtime</a>
   	    <p>
   	    iOS运行时...
   	    </p>
   	</li>
</ul>
</body>
</html>
```

html文件弄好了，浏览器还不能访问到这个html。在my_blog目录下创建views.py文件
然后在views.py里面添加如下代码


```python
from django.shortcuts import render

def articleList(request):
	return  render(request,'articleLists.html')
```

修改urls.py

```python
from django.conf.urls import url
from my_blog import views

urlpatterns = [
   	url(r'^$', views.articleList),
]
```

重启服务--->浏览器输入http://127.0.0.1:8000/--->首页

现在已经能够简单的显示一个静态的首页了。

- **数据库**

因为默认是用的sqlite3，目前博客数据比较少，避免麻烦，就不换成mysql了

在my_blog下创建models.py：

```python
from django.db import models
class Articles(models.Model):
	title = models.CharField(max_length=20)
	abstract = models.CharField(max_length=100)
	emojiId = models.IntegerField(default=0)
	mdFileName = models.CharField(max_length=50)
	createTime = models.IntegerField(default=0)
	class Meta:
		db_table = 'articles'
class Emojis(models.Model):
	emojiName = models.CharField(max_length=50,unique=True)
	class Meta:
		db_table = 'emojis'
```

我们在命令行键入：
>这里当前目录要是项目所在目录，不然会找不到manage.py文件，pycharm直接点击底部的Terminal即可；
>部分机器上Python3需要换成Python

```shell
$ python3 manage.py makemigrations --empty my_blog  
$ python3 manage.py makemigrations 
$ python3 manage.py migrate
```

Django已经帮忙创建好了两张表

- **emoji**      

>创建临时接口将emoji的名称写入数据库

在views.py添加

```python
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
```

修改urls.py

```python
urlpatterns = [
    url(r'^emojiToDatabase',views.emojiToDatabase),
    url(r'^$',views.articleList),
]
```

<font color='red'>**添加emoji名称文件emojiNames.txt**</font>
>我在一些网站上获取到了Facebook全套的emoji表情文件，并且将表情文件的名称全部
>提前写入了emojiNames.txt

重启------>http://127.0.0.1:8000/emojiToDatabase------>emoji名称已经被写入数据库

- **上传文章页**

在templates目录下新建login.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Duang</title>
</head>
<body>

<h1 style="text-align: center">Duang</h1>
<div style="background-color: #e5e5e5;height: 1px;width: 100%"></div>

<div style="display: flex;flex-direction: row;justify-content: center;margin-top: 30px">
    <form method="post">
        <div style="height: 40px">用户名：<input name="name"></div>
        <div style="height: 40px">密码：<input name="password"></div>
        <div style="text-align: center">
            <button type="submit" style="height: 40px;width: 100px;font-size: 16px;">登录</button>
        </div>
    </form>
</div>
</body>
</html>
```

在templates目录下新建admin.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Duang</title>
</head>
<body>

{% if lackParam %}
    <div style="color: red">
        标题、概要、MarkDown文件名称不能为空!!!
    </div>
{% endif %}

<div>
    <form method="post" action="/admin/upload">

        <div style="margin-top: 30px;height: 40px">
            <div style="float: left;width: 30%;text-align: right;height: 40px;font-size: 20px;line-height: 40px">
                文章标题：
            </div>
            <input style="width: 60%;height: 40px;font-size: 20px;padding:0;margin: 0" name="title">
        </div>
        <div style="margin-top: 30px;height: 40px">
            <div style="float: left;width: 30%;text-align: right;height: 40px;font-size: 20px;line-height: 40px">
                概要：
            </div>
            <input style="width: 60%;height: 40px;font-size: 20px;padding:0;margin: 0" name="abstract">
        </div>
        <div style="margin-top: 30px;height: 40px">
            <div style="float: left;width: 30%;text-align: right;height: 40px;font-size: 20px;line-height: 40px">
                emoji图片名称：
            </div>
            <input style="width: 60%;height: 40px;font-size: 20px;padding:0;margin: 0" name="emojiName">
        </div>
        <div style="margin-top: 30px;height: 40px">
            <div style="float: left;width: 30%;text-align: right;height: 40px;font-size: 20px;line-height: 40px">
                MarkDown文件名称：
            </div>
            <input style="width: 60%;height: 40px;font-size: 20px;padding:0;margin: 0" name="mdFileName">
        </div>
        <div style="margin-top: 30px;height: 40px;text-align: center;">
            <button type="submit"
                    style="margin:auto;width: 100px;height: 40px;font-size: 20px;border-radius: 5px;border: 1px solid;background-color: white">
                上传
            </button>
        </div>
    </form>
</div>
</body>
</html>
```

然后在views.py**添加**

>这里实现一个简单的登录功能，登录之后才能进入后台上传文章页面

```python
NAME = 'admin'
PASSWORD = '123456'

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
```

修改路由文件urls.py

```python
urlpatterns = [
    #url(r'^emojiToDatabase',views.emojiToDatabase),
    url(r'^admin$|^admin/$',views.login),
    url(r'^admin/upload$',views.admin),
    url(r'^$',views.articleList),
]
```

重启--->http://127.0.0.1:8000/admin--->上传文章页

- **继续首页**

前面简单的做了一个静态的首页，现在改成动态的，修改articleLists.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Duang</title>
</head>
<body>

<h1 style="text-align: center">Duang</h1>
<div style="background-color: #e5e5e5;height: 1px;width: 100%"></div>

<div style="display: flex;flex-direction: column;margin-left: 20%;margin-right: 20%">
    {% for item in articles %}

        <div style="display: flex;flex-direction: row;margin-top: 30px">
            <img src="{{ item.emoji }}" style="width: 80px;height: 80px;"
                 onclick="window.open('/detail/{{ item.id }}')">
            <div style="margin-left: 20px">
                <a href="/detail/{{ item.id }}"
                   style="font-size: 25px;text-decoration: none;color: #333333">{{ item.title }}</a>
                <div style="margin-top: 10px;color: #888888">{{ item.abstract }}</div>
            </div>
        </div>
        <div style="background-color: #e5e5e5;height: 1px;width: 100%;margin-top: 30px;"></div>
    {% endfor %}
</div>

</body>
</html>
```

然后再修改views.py

```python
from django.db import connection
	
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
```

重启------>http://127.0.0.1:8000----->首页
			http://127.0.0.1:8000/admin----->上传文章页面
			

- **文章详情页**

新建articleDetail.html

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Duang</title>
    <link href="/static/vim.css" rel="stylesheet" type="text/css" />
</head>
<body>

<h1 style="text-align: center">Duang</h1>
<div style="background-color: #e5e5e5;height: 1px;width: 100%"></div>

<div style="display: flex;flex-direction: column;margin-left: 20%;margin-right: 20%">
    <div style="display: flex;flex-direction: row; justify-content: center;align-items: center;margin-top: 30px;margin-bottom: 30px">
        <img src="{{ emoji }}" style="width: 30px;height: 30px;" onclick="window.open('/detail/{{ item.id }}')">
        <div style="text-align: center;font-size: 30px;color: #333333;margin-left: 10px">{{ title }}</div>
    </div>
    <div>
        {{ content|safe }}
    </div>
</div>

</body>
</html>
```
	
在views.py添加

```python
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
```
 
修改urls.py

```python
urlpatterns = [
    url(r'^emojiToDatabase',views.emojiToDatabase),
    url(r'^admin$|^admin/$',views.login),
    url(r'^admin/upload$',views.admin),
    url(r'^$',views.articleList),
    url(r'^detail/(?P<articleId>\d+)', views.articleDetail),
]
```

最后文件列表

<img src="https://duangblog.com/static/myblog_0_4.png" style="width:100%"/>

**end：**到目前为止博客基本上博客代码已经完成，在本地可以愉快的玩耍了，接下来就是到服务器上去部署。
