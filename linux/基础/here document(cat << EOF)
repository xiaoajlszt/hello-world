Here Document 是在Linux Shell 中的一种特殊的重定向方式，它的基本的形式如下：
cmd << delimiter
  Here Document Content
delimiter
它的作用就是将两个 delimiter 之间的内容(Here Document Content 部分) 传递给cmd 作为输入参数。

eg:
比如在终端中输入cat << EOF ，系统会提示继续进行输入，输入多行信息再输入EOF，中间输入的信息将会显示在屏幕上。如下：
fish@mangos:~$ cat << EOF
> First Line
> Second Line
> Third Line EOF
> EOF
First Line
Second Line
Third Line EOF

注：
- > 是终端产生的提示输入信息的标识符
- EOF 只是一个标识而已，可以替换成任意的合法字符
- 作为起始的delimiter前后的空格会被省略掉
- 作为结尾的delimiter一定要顶格写，前面不能有任何字符，后面也不能有任何的字符（包括空格）
