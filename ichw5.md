# question 1
## 北京大学某单位的某台机器IP地址为162.105.80.160, 子网掩码为255.255.255.192，
## &#160; &#160; &#160; &#160;1）该单位的网络号(网络+子网)是多少？
###### &#160; &#160; &#160; &#160;&#160; &#160; &#160; &#160;答：162.105.80.128
## &#160; &#160; &#160; &#160;2）该单位理论上可容纳多少主机？
###### &#160; &#160; &#160; &#160;&#160; &#160; &#160; &#160;答：64，如果不算全0和全1的主机号的话是62个。
## &#160; &#160; &#160; &#160;3）北大可以有多少个这样的子网(假定北大全部是162.105网段)？
###### &#160; &#160; &#160; &#160;&#160; &#160; &#160; &#160;答：1024
# question 2
## 解释TCP协议建立连接为什么设计为三步握手（3-way handshake）？
###### &#160; &#160; &#160; &#160;答：1）显然一次握手是不可行的，因为无法判断对方是否收到了消息。那么如果是两次握手，会出现第一种情况：A发出了消息，B收到消息以后回复，此时B自然而然认为链接已经建立，而此时B的回复丢失在了半路，这时候A认为链接没有建立，而B却为一个不存在的链接保留了大量资源，当然这种情况是无法避免的。第二种情况：A发送了链接请求，这时候请求因为某种原因在途中滞留，间隔了很长时间才到达B，而A没有收到消息，以为是链接失败，再次发出了链接请求。这时候B会收到两个链接请求，其中一个是失效的，B并不知道它是失效的，便回复了A,如果仅仅存在两次握手的话，这样就已经建立了一个链接，将会大大地浪费资源，而如果存在三次握手的话，A将会否定掉链接，便不会存在资源浪费的问题。
###### &#160; &#160; &#160; &#160;2）那为什么不采用四次以上的握手呢？首先我们知道，因为IP的传输是不稳定的，所以在IP的基础上建立一个百分之百确定的稳定的链接协议是不存在的。而三次握手经历了发送请求-对方确认-己方确认三步的过程后，如果再加上第四次第五次握手就仅仅是在重复前面的过程，对结果影响不大，而且请求次数多了以后会大大拖慢链接速度，起了反作用，所以三次握手是性价比最高的选择。
# question 3
## 有哪些恶意软件, 如何防范恶意软件？
###### &#160; &#160; &#160; &#160;答：恶意软件主要包括计算机病毒、蠕虫、木马、间谍软件等在计算机系统上执行恶意任务的软件。防范恶意软件的主要做法有：安装杀毒软件/安全防护软件,及时打补丁；使用防火墙,禁止外部计算机通过网络访问本机；不随便下载运行可执行程序；不打开未知的邮件附件；U盘通常带毒, 打开前要先查毒；不随便暴露自己的email、生日、手机等重要信息；不以Administrator权限操作计算机等。
