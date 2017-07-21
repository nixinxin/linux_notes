# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    1.目录及文件的基本操作
        1.1 pwd
            描述：显示当前工作目录
            用法：pwd [选项]
            选项：-p ( 显示链接的真实路径 ）

        1.2 cd
            描述：切换当前工作目录
            用法：cd /usr/bin/ | cd .. ( 上级目录 ) | cd - ( 返回前一个目录 ）| cd （ 切换到当前用户的家目录 ）

        1.3 ls
             描述： 显示文件及目录信息
             用法：ls [选项] [文件/目录]
             选项： -a 显示所有，包含隐藏
                    -d 显示目录本身的信息
                    -h 人性化显示
                    -l 长格式显示文档的详细信息
                    -u 显示最后访问的时间
                    -t 按修改时间排序，默认按文件名排序

        1.4 touch
            描述：创建或修改文件时间
            用法：touch [文档]

        1.5 mkdir
            描述：创建目录
            用法：mkdir [选项] [目录]
            选项：-p ( 创建多级目录 ）

        1.6 cp
            用法：复制文件及目录
            用法：cp[选项] 源 目标
            选项：  -r 递归复制子文件或子目录
                    -a 复制时保留源文档的所有属性

        1.7 rm
            描述：排除文件及目录
            用法：rm [选项] 文件
            选项：  -f 不提示，强制排除
                    -i 排除前，提示是否排除
                    -r 递归排除子文件及目录

        1.8 mv
            描述：移动（重命名）文件及目录
            用法： mv hello.txt hello.doc

        1.9 find
            描述：搜索文件及目录
            用法： find 【选项】 [路径] [表达式选项]
            选项：  -empty 查找空文件或目录
                    -group 按组查找
                    -user 按用户查找
                    -name 按文件名查找
                    -iname 按文件名查找，不区分大小写
                    -mtime 按修改时间查找
                    -size 按容量查找 +1M: >1M
                    -type 按文档类型查找 文件f，目录d，设备（b,c)，链接（l)
                    -exec 对找到的对象执行命令
                    -a 并且
                    -o 或者

        1.10 du
            描述：计算文件或目录的容量
            用法：du [选项] [文件或目录]
            选项：  -h 人性化显示
                    -a 查看所有文件及目录的容量信息
                    -s 显示总容量

    2.查看文件内容
        2.1 cat
            描述：查看文件内容
            用法：cat [选项] [文件]
            选项：  -b 显示行号，不包含空白行
                    -n 显示行号，包含空白行
        2.2 more/less
            描述：分页查看文件内容

        2.3 head /tail
            描述：查看文件的前/尾内容，默认显示10行
            用法：head/tail [选项] [文件]
            选项:   -c nK 指定显示nKB内容
                    -n 显示n行内容

        2.4 wc
            描述：显示文件的行、单词和字节统计信息
            用法：wc [选项] [文件]
            选项：  -c 字节； -l 行数； -w 单词；

        2.5 grep
            描述：查找关键词并打印匹配的行
            用法：grep [选项] 匹配模式 [ 文件]
            选项：  -i 忽略大小写
                    -v 取反匹配
                    -w 匹配单词
                    --color 显示颜色

        2.6 echo
            描述：显示一行指定的字符串
            用法：echo [选项] [字符串}
            选项：  -n 不输出换行； -e 开启转义

    3.链接文件
        3.1 软连接
            ls -s  A  B  : 创建文件或目录软连接，源文件不可排除，可跨分区

        3.2 硬链接
            ls  A  B  : 源文件可排除，但不可跨越分区

    4. 压缩及解压缩
        gzip / bzip2 [-d] [文件名称]  : -d表示解压缩

        tar 模式 [选项] [路径]
        描述：打包与解包文件
        模式：  -c 创建打包文件
                --delete 从打包文件中排除文件
                -r 追加文件至打包文件
                -t 列出打包文件的内容
                -x 释放打包文件

        选项：  -C 指定解压路径
                -f 指定打包后的文件名称
                -j 用bzip2格式压缩解压
                --remove-files 打包后排除源文件
                -z 用gzip格式压缩解压
    vim 小技巧
        1.显示行号：set number;2.忽略大小写：set ignorecase; 3.命令窗口切割：split hello.txt;vsplit hello.txt.

    账户与安全
    1.创建账户和组
        1.1 useradd
            描述：创建账号
            用法：useradd 【选项】 用户名称
            选项：  -c 设置账户描述信息，一般为账号全称
                    -d 设置账号家目录，默认为/home/用户名
                    -e 设置账户的失效日期，格式为YYYY-MM-DD
                    -g/G 设置账户的基本组/附加组
                    -M 不创建家目录，一般与-s结合使用
                    -s 设置账户的登录shell，默认bash
                    -u 指定账户UID
            useradd -c administrator -d home/admin -e 2017-09-12 -g root -G bin,adm,mail admin

        1.2 groupadd
            描述：创建组账号
            用法：groupadd 【选项】 用户名称
            选项  -g 设置组ID号
                groupadd -g 1000 hello

        1.3 id
            描述：显示账户及组信息

    2. 修改账户及组
        2.1 passwd
            描述：更新账户认证信息
            用法：passwd [选项] [账户名称]
            选项：  -l 锁定账户，仅root可用
                    -u 解锁账户，仅root可用
                    --stdin 从文件或管道中读取密码
                    -d 快速清空账户密码
                    echo 1234 |passwd --stdin tom
        2.2 usermod
            描述：修改账号信息
            用法：usermod 【选项】 用户名称
            选项：  -d 修改账户家目录
                    -e 修改账户失效日期
                    -g/G 修改账户所属基本组、附加组
                    -s 修改账户登录shell
                    -u 修改账户UID

    3.排除账户及组
        3.1 userdel
            描述：排除账户及相关信息
            用法：userdel [选项] 账户名称
            选项：  -r  排除账户及相关文件
        3.2 groupdel
            描述：排除组账户

    文档及目录权限
        R4(可读)---W2(可写)---X1(可执行)
        1 修改文档属性
            1.1 chmod
                描述：改变文档及目录的权限
                用法：chmod [选项] 权限 文件及目录
                选项： --reference=RFILE  根据参考文档设置权限
                    chmod u=rwx,g=rwx,0=rwx install.log
                    chmod a=rw install.log
                    chmod g-x,0-wx install.log
                    chmod 700 install.log
                    chmod --refernce=install.log hello.log

            1.2 chown
                描述：修改文件或者目录的所有者或所属组
                用法： chown [选项]  [所有者][：[所属组]]  文档或目录
                选项： -R 递归修改子文件及目录

    ACL访问控制权限
        1. getfacl install.log  获取ACL权限
        2. setfacl
            描述：设置文档访问控制列表
            用法：setfacl 【选项】 [{-m|-x} acl条目] 文件及目录
            选项： -b # 排除所有的ACL条目
                   -m 添加ACL条目
                   -X 排除指定的ACL条目
                   -R 递推处理所有子文件或目录

    存储管理
        设备表示：abc;分区表示：123
        1. 磁盘分区
            fdisk -l  # 查看磁盘分区列表
            fdisk /dev/sdb  # 为第二块磁盘分区
            partprobe /dev/sdb  # 立即让内核读取行的分区表

            GPT 分区方式
                parted [选项]  [磁盘 [命令]]
                修改分区表类型
                    parted /dev/sdb mklabel gpt  # 修改分区表格式
                    parted /dec/sdb print  # 查看分区表信息
                创建于删除分区
                    parted 【磁盘】 mkpart 分区类型  文件系统类型  开始 结束
                    分区类型：primary/logical/extended
                    文件系统类型：fat16/fat32/ext2/ext3/linux-swap
                    开始结束单位默认KB
                parted /dev/sdc mkpart primary fat32 1G 2G

        2. 格式化及挂载文件系统
            mkfs.xfs /dev/sdc1   # 将/dev/sdc1格式化为xfs格式
            mkswap /dev/sdc2    # 将/dev/sdc2（交换分区用mkswap）格式化swap格式

            挂载文件系统
                1.命令方式：重启后无效
                    mount 挂载文件系统
                    用法：mount [选项] [-o [选项]] 设备 挂载目录
                    选项：  -a 挂载/etc/fstab文件中所有未挂载的文件系统
                            -t 指定文件系统类型
                            -o 指定挂载属性
                            mkdir /data1
                            mount /dev/sdc1 /data1
                            umount /dev/sdc1

        3.LVM逻辑卷管理器：适用于大存储器，可动态调整文件系统大小
            物理卷PV/卷组VG/物理长度PE/逻辑卷LV
            3.1 pvcreate
                描述：使用LVM对磁盘或分区进行初始化
                用法：pvcreate [选项] 物理卷 [物理卷]
                pvcreate /dev/sdc4 /dev/sde   pvcreate /dev/sdb{1,2,3,4}

            3.2 vgcreate
                描述：创建卷组
                用法： vgcreate [选项]  卷组名称 物理设备路径 [物理设备路径]
                vgcreate test_vg2 -s 16M /dev/sdc5 /dev/sdc6  # -s 指定PE大小

            3.3 lvcreate
                描述：从卷组中提取存储空间，创建逻辑卷
                用法：lvcreate [选项]  卷组名称或路径 [物理设备路径]
                选项：  -l 指定使用多少个卷组中的PE创建逻辑卷
                        -L 直接指定逻辑卷的容量大小
                        -n 指定逻辑卷的名称
                        lvcreate -L 2G -n test_lv1 test_vg1 /dev/sdb6

                        pvdisplay/lvdisplay 查看创建卷的结果
            3.4 lvextend 修改LVM分区容量
                lvextend -L +120G /dev/test_vg/test_data

            3.5 排除LVM分区
                排除的顺序与创建相反：卸载文件系统、排除逻辑卷、排除卷组、排除物理卷
                umount--lvremove(有多个则排除多个)--vgremove--pvremove

        4. RAID 独立冗余磁盘阵列：将多块独立的磁盘组合成逻辑磁盘
            4.1 查看磁盘信息：fdisk -l
            4.2 创建硬盘分区：fdisk /dev/sdb
    软件管理
        1. RPM红帽软件包工具
            1.1 安装 ： vim -vih 软件包名称   # 默认为静默安装，v显示详细信息，h显示安装进度
            1.2 卸载 ： vim -e ftp  # 具体版本号可不写
            1.3 查询 ：  -q 查询指定软件包是否安装
                        -qa 查询安装的所有软件
                        -qi 查询指定安装软件包的详细信息
                        -ql 查询指定的软件的安装路径与文件列表
                        -qc 查询指定软件的配置文件
                        -qf 查询指定的文件由哪个软件安装
                        -qp 查询尚未安装软件的详细信息

                        -V 对指定软件进行安全验证

        2. YUM安装工具，解决了软件依赖问题
            描述：基于RPM的包管理工具
            用法：yum [选项][指令][软件包]
            选项：-y 执行非交互式安装
            指令：  install package1 package2
                    update package1 package2
                    check-update
                    remove|erase package1 package2
                    list
                    info
                    clean all 清空所有软件信息
                    groupinstall group1 [group2]
                    grouplist 列出系统中以及云源中所有可用的组包
                    groupremove group1 group2
                    search string1 string2 根据关键字查找软件
                    localinstall rpmfile1 rpmfile2
                    history 查看历史记录
                    langavailable 查看语言包
                    langinstall 安装语言包

            yum变量 $releasever/$arch/$basearch/$YUM0-9
                    系统发行版本号、CPU架构、系统架构、

        3. 源码编译安装软件：根据需求定制软件配置
            3.1 获取软件源码并解压缩
            3.2 运行configure脚本，通过特定的选项修改软件设置与功能，并检查对应开发工具是否已经安装
            3.3 运行make 命令将源代码编译为计算机可以直接识别的机器语言
            3.4 通过make install 更快配置阶段指定的路径和功能将软件以特定的方式安装

        4. 软件安装问题
            4.1 RPM软件依赖包问题：使用 --nodeps 不依赖
            4.2 RPM数据库破坏：rpm --rebuilddb  修复数据库资料
            4.3 yum繁忙问题： kill pid编号
            4.4 GCC编译器问题：yum install gcc

        服务管理
            systemctl  start/stop/status/reload 服务名称
            systemctl condrestart 服务名称  # 测试新的配置是否有问题，没有问题再重启
            systemctl enable/disable sshd 设置服务默认为开机启动或禁用服务

    计划任务
        1. at一次性计划任务
            描述：在指定的时间执行特定的操作
            用法：at 时间  小时：分钟、3pm + 3 days、 12:00 2016-12-12
            选项：  -m 当计划任务完成后发送邮件到指定用户
                    -l 查看用户计划任务
                    -d 排除用户计划任务
                    -c 查看at计划任务的具体内容

                    at -c 1 查看编号为1的计划任务的具体内容

        2. cron周期性计划任务
            描述：为每个用户维护周期性计划任务
            用法：crontab [-u 用户] [-l|-r|-e]
            选项：  -u 指定计划任务的用户，默认当前用户
                    -l 查看计划任务
                    -r 排除计划任务
                    -e 编辑计划任务
                    -i 使用r排除计划任务时要求用户确认排除
                    分00-59  时00-23  日1-31  月1-12  周0-7  命令
                    横杠（-）表示连续时间
                    逗号（，）表示若干个不连续时间
                    星号（*）表示所有时间
                    除号（/)表示间隔时间
                    crontab -e
                    分00-59  时00-23  日1-31  月1-12  周0-7  命令
                    23        */3      *        *       *    who
                    计划任务完成后退出方式与vim一样

    性能监控
        1. 监控CPU使用情况----uptime
        2. 监控内存及交换分区使用情况----free [-b|-k|-m] 指定输出容量的单位
        3. 监控磁盘使用情况----df [选项]
            选项：  -h 人性化显示
                    -i 显示磁盘inode使用量信息
                    -T 显示文件系统类型

        4. 监控网络使用情况----ip和netstat
            ip命令可以查看网卡接口信息： ip a s  / ip -s link show 网卡名 # 查看网卡流量信息
            netstat命令查看服务器开启的端口信息以及网络连接状态
                描述：打印网络连接、路由表、网络借口统计信息
                选项：  -s 显示各协议数据统计信息
                        -p 显示进程名称及对应进程的ID号
                        -l 仅显示正在监听的sockets接口信息
                        -u/t 查看udp/tcp链接信息

        5. 监控进程使用情况----ps和top
            ps: 查看当前进程信息
                ps -e   # 查看所有的进程信息
                ps -ef  # 全格式显示进程信息
            top: 动态查看进程信息
                选项：  -d 刷新间隔，默认3秒
                        -p 查看指定PID的进程信息
                        top -d 1 -p 1,2
    网络配置
        1. 网络接口参数----ifconfig
            描述：显示或设置完了接口信息
            用法：ifconfig interface 选项|地址
            设置：
                ifconfig 网卡名称 IP地址  netmask 子网掩码
                ifconfig 网卡名称 [up/down]  查看网络接口信息【开启、关闭】   

        2. 主机名参数----hostnamectl
            描述：显示或设置系统主机名称
            用法：hostnamectl [选项]
                    hostnamectl status  # 查看主机名称及信息
                    hostnamectl set-hostname 名称

        3. 路由参数----route
            描述：显示或设置静态IP路由表
            用法：route [选项]
                    route add 目标网络 gw 网关地址
                    route del 目标网络

                    route add default gw 网关地址
                    route add -net 网段 gw 网关地址 dev 网络接口

        4. 网络故障排除
            4.1 ping 定位问题网络节点位置
                顺序：本地回环、本地IP、网关IP、外网IP
                ping 127.0.0.1
            4.2 traceroute 跟踪数据包的路由过程，默认使用UDP封装数据包，可设置-I使用ICMP封装
                traceroute -I www.baidu.com
            4.3 nslookup 检查本地设置的DNS服务器是否正常
                nslookup www.baidu.com
            4.4 dig 查看更多DNS信息 
                dig www.baidu.com MX(邮件记录)
                dig www.baidu.com NS(域名服务器记录)

    内核模块
        查看已加载内核模块：lsmod,输出三列信息（模块名称、占用内存大小、是否被调用）
        加载内核信息：modprobe 模块名
        卸载内核信息：modprobe -r 模块名
        查看模块信息：modinfo 模块名
        永久修改内核参数：
            man proc 获取内核参数描述信息
            修改/etc/sysctl.conf 文件
            修改完成后使用sysctl -p使设置立即生效



"""
