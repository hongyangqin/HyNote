# [python uuid](https://www.cnblogs.com/dkblog/archive/2011/10/10/2205200.html)

    资料：

        Python官方Doc：《20.15. uuid — UUID objects according to RFC 4122》
        UUID的算法介绍：《A Universally Unique IDentifier (UUID) URN Namespace》

    概述：

        UUID是128位的全局唯一标识符，通常由32字节的字符串表示。
        它可以保证时间和空间的唯一性，也称为GUID，全称为：
                UUID —— Universally Unique IDentifier      Python 中叫 UUID
                GUID —— Globally Unique IDentifier          C#  中叫 GUID

        它通过MAC地址、时间戳、命名空间、随机数、伪随机数来保证生成ID的唯一性。
        UUID主要有五个算法，也就是五种方法来实现：

           1、uuid1()——基于时间戳

                   由MAC地址、当前时间戳、随机数生成。可以保证全球范围内的唯一性，
                   但MAC的使用同时带来安全性问题，局域网中可以使用IP来代替MAC。

           2、uuid2()——基于分布式计算环境DCE（Python中没有这个函数）

                    算法与uuid1相同，不同的是把时间戳的前4位置换为POSIX的UID。
                    实际中很少用到该方法。

          3、uuid3()——基于名字的MD5散列值

                    通过计算名字和命名空间的MD5散列值得到，保证了同一命名空间中不同名字的唯一性，
                    和不同命名空间的唯一性，但同一命名空间的同一名字生成相同的uuid。

           4、uuid4()——基于随机数

                    由伪随机数得到，有一定的重复概率，该概率可以计算出来。

           5、uuid5()——基于名字的SHA-1散列值

                    算法与uuid3相同，不同的是使用 Secure Hash Algorithm 1 算法

    使用方面：

        首先，Python中没有基于DCE的，所以uuid2可以忽略；
        其次，uuid4存在概率性重复，由无映射性，最好不用；
        再次，若在Global的分布式计算环境下，最好用uuid1；
        最后，若有名字的唯一性要求，最好用uuid3或uuid5。

    编码方法：

        # -*- coding: utf-8 -*-

        import uuid

        name = "test_name"
        namespace = "test_namespace"

        print uuid.uuid1()  # 带参的方法参见Python Doc
        print uuid.uuid3(namespace, name)
        print uuid.uuid4()
        print uuid.uuid5(namespace, name)