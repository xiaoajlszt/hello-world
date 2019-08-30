https://www.jianshu.com/p/701952ffb755
https://bbs.51cto.com/thread-1104907-1-1.html

1. & 和 wait
for i in `seq 1 10` 
do
    echo $i &   //如果命令耗时较长导致总时间较长。如果命令之间没有互相依赖关系时，可以让命令并行执行，并行执行的方法就是在命令后加上 & 符号。
done
wait   //有的时候需要保证for循环所有命令执行完后再向后执行接下来的命令。可以使用 wait 实现
...

2. 使用管道和令牌原理实现并发控制。
当需要并行执行的命令数量特别多的时候，特别是执行命令的资源占用较多时，直接用 & 实现并行容易将服务器资源占用打满，影响其他程序运行。

-------------
eg:

#!/bin/bash
# Step1 创建有名管道
[ -e ./fd1 ] || mkfifo ./fd1

# 创建文件描述符，以可读（<）可写（>）的方式关联管道文件，这时候文件描述符3就有了有名管道文件的所有特性
exec 3<> ./fd1   

# 关联后的文件描述符拥有管道文件的所有特性,所以这时候管道文件可以删除，我们留下文件描述符来用就可以了
rm -rf ./fd1                    

# Step2 创建令牌 
for i in `seq 1 2`;
do
    # echo 每次输出一个换行符,也就是一个令牌
    echo >&3                   
done

# Step3 拿出令牌，进行并发操作
for line in `seq 1 10`;
do
    read -u3                    # read 命令每次读取一行，也就是拿到一个令牌   
    {
        echo $line 
        echo >&3                # 执行完一条命令会将令牌放回管道
    }&
done

wait

exec 3<&-                       # 关闭文件描述符的读
exec 3>&-                       # 关闭文件描述符的写

-------------

1. mkfifo

NAME
       mkfifo - make FIFOs (named pipes)

SYNOPSIS
       mkfifo [OPTION]... NAME...

DESCRIPTION
       Create named pipes (FIFOs) with the given NAMEs.


2. exec
Bash内置命令exec可以替换当前程序而不需要启动一个新的进程，可以改变标准输入和输出而不需要启动一个新的子进程。

<1> 替换当前shell，执行某个命令，命令终止，shell也就终止了
$exec ls

<2> 打开文件作为当前shell的标准输入
$exec <file_name

<3> 打开文件作为当前shell的标准输出
$exec >file_name

<4> 打开文件作为输入，并分配文件描述符
$exec 3<datafile

<5> 打开文件作为输出，并分配文件描述符
$exec 4>datafile

<6> 创建文件描述符fd4的拷贝fd5
$exec 5<&4

<7> 关闭文件描述符
$exec 3<&- //关闭输入文件描述符
$exec 4>&- //关闭输出文件描述符

eg:
$exec 3>filex //打开文件filex并分配文件描述符3，作为输出
$who >& 3     //who命令的输出输出到filex
$date >& 3    //date命令的输出输出到filex
$exec 3>&-    //关闭filex
$exec 3<filex //重新打开文件filex并分配文件描述符3，作为输入
$cat <& 3     //重定向cat命令的输入到文件描述符3，即文件filex
$exec 3<&-    //关闭filex