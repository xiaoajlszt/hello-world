#### 1.一些操作
- 列出库名
`\l  或  SELECT dataname FROM pg_database;`

- 列出当前库所有表
`\d  或  \dt`

- 切换库
`\c 数据库名`

- 表结构
`\d 表名`

- 查询当前库
`select current_database()`

- 打开/关闭竖状展示查询结果
`\x`

- \d+
`\d and 显示子表`

#### 2.commit
- postgresql默认是自动提交的

- 查看是否是自动提交:
```
\echo :AUTOCOMMIT
on
```

- 关闭自动提交:
```
\set AUTOCOMMIT off
\echo :AUTOCOMMIT 
off
```

#### 3.防止 SQL injection
```
http://initd.org/psycopg/docs/usage.html#query-parameters
the second argument must always be a sequence, even if it contains a single variable (remember that Python requires a comma to create a single element tuple):
>>> cur.execute("INSERT INTO foo VALUES (%s)", "bar")    # WRONG
>>> cur.execute("INSERT INTO foo VALUES (%s)", ("bar"))  # WRONG
>>> cur.execute("INSERT INTO foo VALUES (%s)", ("bar",)) # correct //单个元素必须有逗号
>>> cur.execute("INSERT INTO foo VALUES (%s)", ["bar"])  # correct

[in message queue]
'); create table a(a int); --

[in product hacker]
String query = String.format("select * from users where usr='%s' and pwd='%s'",usr,pwd);
//USER为 admin' or '1' = '1 时即可破解。
```

#### 4.与NULL比较
- IS NULL
- IS NOT NULL

#### 5.数据导入导出
- 导出整个数据库
```
pg_dump -h localhost -U postgres(用户名) 数据库名(缺省时同用户名) > *.sql(文件名)
```

- 导出某个表
```
pg_dump -h localhost -U postgres(用户名) 数据库名(缺省时同用户名)  -t table(表名) > *.sql(文件名)
```

- 导入之前导出的单个表结构及数据
```
psql -h localhost -d 数据库名 -U 用户名 -f .sql文件
//导入和手动insert的数据，不算在id自增中。
```

- CSV导出
```
COPY (select * from tb_sandbox_report_file_analyze where create_time>'2018-05-20 23:59:59') to '/home/sql_new/report_file_analyze.csv' with csv header;
```

- CSV导入
```
COPY tb_msg_tracing from '/home/sql/tb_msg_tracing.csv' WITH CSV HEADER;
```

- 其他说明
```
http://www.cnblogs.com/baxk/p/4895573.html
```
