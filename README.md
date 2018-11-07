# easyLabel
一个简单的为图片进行打标签的网站，基于Django

依赖有

> django
>
> djangorestframework - restful API
>
> pillow -图形处理
>
> django-extensions - 扩展 python manage.py 功能
>
> django-cors-headers  -  解决跨域问题
>
> sqlite3



这里写了三个脚本

- upload2qiniu.py  这个脚本可以dfs文件夹并将每个子文件传到七牛云的图床上
- upload.py 这个脚本可以dfs文件夹并将每个子文件信息传到数据库里

（以上两个其实可以而且也应当写成一个脚本）

- export2csv.py 导出数据库内容为csv



提供的接口有

| 功能说明              | url                | 方法  | 需要内容（data              |
| --------------------- | ------------------ | ----- | --------------------------- |
| 管理界面              | admin/             | -     | -                           |
| 获取所有标签          | tag/tags/          | GET   | -                           |
| 提交一个新的标签      | tag/tags/          | POST  | “label”:<label_name>        |
| 获取数据库基本信息    | tag/pictures/      | GET   | -                           |
| *获取所有图片详细信息 | tag/pictures/list/ | GET   | -                           |
| 获取某张图片信息      | tag/pictures/<id>/ | GET   | -                           |
| 更新某张图片标签      | tag/pictures/<id>/ | PATCH | “label1”:<label_name_in_db> |
| 随机获取3张无标签图片 | tag/pictures/any/  | GET   | -                           |

\* 建议谨慎使用