#### UTC(Universal Time Coordinated) 和 GMT(Greenwich Mean Time)
UTC是我们现在用的时间标准，GMT是老的时间计量标准。UTC是根据原子钟来计算时间，而GMT是根据地球的自转和公转来计算时间。

#### UTC时间的表示格式
根据 ISO 8601《数据存储和交换形式·信息交换·日期和时间的表示方法》，UTC时间，也就是国际统一时间/国际协调时，表示方法如下：
YYYYMMDD T HHMMSS Z(或者时区标识)。
```
- 20100607T152000Z，表示2010年6月7号15点20分0秒，Z表示是标准时间
- 北京时间:20100607T152000+08，其中“+08”表示东八区。
```

#### Example
- 1985-04-12T23:20:50.52Z
This represents 20 minutes and 50.52 seconds after the 23rd hour of 12 April 1985 in UTC.

- 1985-04-12T19:20:50.52-04:00
//表示本地时间是19:20:50.52，本地时区是-4，即可得UTC时间为23:20:50.52
This represents the same time as in example 1, but expressed in US Eastern Standard Time (observing daylight savings time).
