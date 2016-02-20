这里我们将称我们的博客应用为 flaskr，也可以取一个不那么 web 2.0 的名字。基本上我们想要它做如下的事情：

根据配置文件中的认证允许用户登录以及注销。仅仅支持一个用户。
当用户登录后，他们可以添加新的条目，这些条目是由纯文本的标题和 HTML 的正文构成。因为我们信任 用户这里的 HTML 是安全的。
页面倒序显示所有条目（新的条目在前），并且用户登入后可以在此添加新条目。
我们将在这个应用中直接使用 SQLite 3 因为它足够应付这种规模的应用

1 创建文件夹
	/flaskr
	    /static
		/templates
	flaskr 文件夹不是一个 Python 的包，只是我们放置文件的地方。 在接下来的步骤中我们会直接把数据库模式和主模块放在这个文件夹中。应用的使用用户可以通过 HTTP 访问 static 文件夹中的文件。这里也是 css 和 javascript 文件存放位置。Flask 将会在 templates 文件夹中寻找 Jinja2 模版。

2 数据库模式
	首先我们要创建数据库模式。对于这个应用仅一张表就足够了，而且我们只想支持 SQLite ，所以很简单。 只要把下面的内容放入一个名为 schema.sql 的文件，文件置于刚才创建的 flaskr 文件夹中：
	drop table if exists entries;
	create table entries (
	id integer primary key autoincrement,
	title string not null,
	text string not null
	);
	这个模式由一个称为 entries 的单表构成，在这个表中每行包含一个 id ，一个 title 和一个 text。 id 是一个自增的整数而且是主键，其余两个为非空的字符串。


3 应用设置代码
	现在我们已经有了数据库模式了，我们可以创建应用的模块了。让我们称为 flaskr.py ，并 放置于 flaskr 文件夹中。对于初学者来说，我们会添加所有需要的导入像配置的章节中一样。对于小应用，直接把配置放在主模块里，正如我们现在要做的一样，是可行的。然而一个更干净的解决方案就是单独创建 .ini 或者 .py 文件接着加载或者导入里面的值。

4 创建数据库
	可以通过管道把 schema.sql 作为 sqlite 3 命令的输入来创建这个模式，命令如下:
	sqlite3 /tmp/flaskr.db < schema.sql
	这种方法的缺点是需要安装 sqlite 3 命令，而并不是每个系统都有安装。而且你必须提供数据库的路径，否则将报错。添加一个函数来对初始化数据库是个不错的想法。

	添加一个函数来对初始化数据库是个不错的想法。
	如果你想要这么做，首先你必须从 contextlib 包中导入 contextlib.closing() 函数。并且在 flaskr.py 文件中添加如下的内容:
	from contextlib import closing
	接着我们可以创建一个称为 init_db 函数，该函数用来初始化数据库。为此我们可以使用之前定义的 connect_db 函数。 只要在 connect_db 函数下添加这样的函数:
	def init_db():
	    with closing(connect_db()) as db:
		    with app.open_resource('schema.sql') as f:
				db.cursor().executescript(f.read())
			db.commit()
	closing() 助手函数允许我们在 with 块中保持数据库连接可用。 应用对象的 open_resource() 方法在其方框外也支持这个功能， 因此可以在 with 块中直接使用。这个函数从资源位置（你的 flaskr 文 件夹）中打开一个文件，并且允许你读取它。我们在这里用它在数据库连接上执行一个脚本。
	当我们连接到数据库时会得到一个数据库连接对象（这里命名它为 db ），这个对象提供给我们一个数据库指针。指针上有一个可以执行完整脚本的方法。最后我们不显式地提交更改， SQLite 3 或者其它事务数据库不会这么做。
	现在可以在 Python shell 里创建数据库，导入并调用刚才的函数:
	>>> from flaskr import init_db
	>>> init_db()
