<!--toc-->

- [Java读取桌面路径的方法](#java读取桌面路径的方法)
	- [参考](#参考)
- [Java 窗口(JFrame/Frame)居中](#java-窗口jframeframe居中)
	- [参考](#参考-1)
- [给窗口增加滚动条](#给窗口增加滚动条)
- [TextArea 自动滚动到最后一行](#textarea-自动滚动到最后一行)
- [Hello World](#hello-world)
- [输出内容](#输出内容)
- [输入当前时间](#输入当前时间)
- [判断参数的个数](#判断参数的个数)
- [获取随机值(整型和浮点型)](#获取随机值整型和浮点型)
- [四舍五入](#四舍五入)
- [字符串处理](#字符串处理)
- [是类无法直接在外部定义出来，必须要用类的制定函数来生成](#是类无法直接在外部定义出来必须要用类的制定函数来生成)
- [单例，只能创建一个对象](#单例只能创建一个对象)
- [经验：使用父类引用子类对象](#经验使用父类引用子类对象)
- [任意类型 和 ByteArray 互相转换](#任意类型-和-bytearray-互相转换)
- [以 String 形式输出 byte 数组的内容](#以-string-形式输出-byte-数组的内容)
- [创建线程的两种方式](#创建线程的两种方式)
- [文件重命名](#文件重命名)
- [数组 一行代码初始化](#数组-一行代码初始化)
- [创建数组作参数](#创建数组作参数)
- [GUI 添加控件事件](#gui-添加控件事件)
- [Layout 使用](#layout-使用)
- [Java GUIwindowClosing](#java-guiwindowclosing)
- [判断两个数组是否相等](#判断两个数组是否相等)
- [焦点移动到下一个控件 ，发送事件 ，发送Tab事件](#焦点移动到下一个控件-发送事件-发送tab事件)
- [GUI 布局  ,一般布局](#gui-布局-一般布局)
	- [GridBagLayout 的简单使用](#gridbaglayout-的简单使用)
- [杨辉三角](#杨辉三角)
- [从控制台中输入数据](#从控制台中输入数据)

<!-- tocstop -->
# Java读取桌面路径的方法
```{java}
string path = FileSystemView.getFileSystemView().getHomeDirectory().getAbsolutePath()
```
## 参考
[Java读取桌面路径的方法](http://chinakite.iteye.com/blog/24983)

# Java 窗口(JFrame/Frame)居中
```{java}
JFrame frame = new JFrame();  
frame.setLocationRelativeTo(null);
```

## 参考

[Java 窗口(JFrame/Frame)居中](http://www.programgo.com/article/74971616450/)


# 给窗口增加滚动条
1. 需要添加的窗口加入到 **JScrollPane** 对象中
2. 使用 **JScrollPane**  对象代替原来窗口加入到 **Panel** 中

```{java}
JList<String> leftList = new JList<String> ();
JScrollPane jsl = new JScrollPane(leftList);
listPanel.add(jsl);
this.add(listPanel);
```

# TextArea 自动滚动到最后一行
``{java}
textArea.setCaretPosition(textArea.getText().length());
```

# Java 简单文本输入窗口，不需要自己创建界面
![1]

```{java}
//点击 Cancel ,返回 null
String nickname = JOptionPane.showInputDialog(this, "Input your nickname");
```
java的一些例子.md
# Hello World
```
* 输出 hello world
* 问题
    * 注意main 函数 是 static ，还有不要忘记了前面的 public
package test;
public class HelloWorld2 {
    public static void main(String srgs[]){
        System.out.println("Hello world!");
    }
}
```
# 输出内容
```
System.out.println("Hello,it's ");
```
```
* 输出 int 域 和 char 域 的默认值
* 问题
    * 创建新对象的时候，后面有个 ()
    * 输出默认的值，只有int 和 char 是类的字段的时候i，才有默认值，不然会报错。
package test;
public class a {
    int b;char c;
    public  a(){
        System.out.println("int is [" + b + "]");
        System.out.println("char is [" + c + "]");
    }   
    public static void main(String[] args) {
        new a();
    }
}
```

# 输入当前时间
Date 对象，默认初始化为当前时间
```
import java.util.*;
System.out.println(new Date());
```

# 判断参数的个数
* String 数组，可以用 length 来获取数组的元素的个数
```
package test;
public class a10 {
    public static void main(String[] args) {
        if(args.length < 3){
            System.out.println("参数输出小于3");           
        }else {
            System.out.println(args[0]);
            System.out.println(args[1]);
            System.out.println(args[2]);
        }
    }
}
```

# 获取随机值(整型和浮点型)
* Random() 默认使用当前时间作种子，也可以直接自定义Random(1)
```
import java.util.Random;
Random a = new Random();
a.nextDouble();
a.nextInt();
a.nextInt(上界);
```

# 四舍五入
```
import java.lang.Math 的 round()方法
```

# 字符串处理
```
* 判断大小写
* 类：Character.isLowerCase();
```

# 是类无法直接在外部定义出来，必须要用类的制定函数来生成
* 把构造器设置成private
```
class Sundae{
    private Sundae(){}//这句因为是private，所以不能访问
    static Sundae makeASundae(){
        return new Sundae();
    }
}
        // ! Sundae x = new Sundae();
        Sundae a = Sundae.makeASundae();
```

# 单例，只能创建一个对象
* 限制构造函数，创建要给自己的静态变量来访问。
```
class singleton{
    private singleton(){}
    private static singleton ps1 = new singleton();
    public static singleton access(){
        return ps1;
    }
    public void func(){}
}
    singleton.access().func();
```

# 经验：使用父类引用子类对象
* 这样，使用其他子类的时候，只需要更改声明处即可

<span id = "AnytypeTranformToByteArray"></span>
# 任意类型 和 ByteArray 互相转换
问题：若一直 byte[] 的内容，这个内容 用String 存放，怎么转换成 byte[] ?逐项赋值？见 [以String形式输出byte数组的内容](#ShowByteArrayInString)
注意：下面  System.out.println(b);   输出的东西不是内存里面的数据，是地址？
```
/*
 * 任意类型 和 ByteArray 互相转换
 * 即 把数据输出到 byte 数组 和 把byte数组的数据 输出到 对应的内存空间  
*/
package Learning;
import java.io.*;
public class AnytypeTranformToByteArray {   
    static public void main(String args[])throws Exception{
        byte b[] = longToByteArray(6666L);
        System.out.println(6666L + ":" + b);       
        long tsetl = byteArrayToLong(b);       
        System.out.println(b + ":" + tsetl);       
    }   
    static byte[] longToByteArray(long n)throws Exception{
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        DataOutputStream dos = new DataOutputStream(baos);
        dos.writeLong(n);
        dos.flush();       
        dos.close();
        byte ret[] = baos.toByteArray();
        baos.close();
        return ret;       
    }
    static long byteArrayToLong(byte buf[])throws Exception{
        ByteArrayInputStream bins = new ByteArrayInputStream(buf);
        DataInputStream dis = new DataInputStream(bins);
        long ret = dis.readLong();
        dis.close();
        bins.close();
        return ret;               
    }   
}
```



<span id = "ShowByteArrayInString"></span>
# 以 String 形式输出 byte 数组的内容
又见  [AnytypeTranformToByteArray](#AnytypeTranformToByteArray)
```
/*
* 把byte数组 以字符串的形式输出，即输出 byte数组 在内存中的数据 以 String 形式输出
*/
package Learning;
import java.util.Base64;

public class ShowByteArrayInString {
    public static void main(String args[])throws Exception{               
        //把66666L 存入到byte，并以字符串把内容输出
        byte bArray[] = AnytypeTranformToByteArray.longToByteArray(66666L);
        String str = Base64.getEncoder().encodeToString( bArray );

        //把字符串转换成byte数组，在转换成对应的类型输出,
        bArray = Base64.getDecoder().decode(str);
        Long testlong = AnytypeTranformToByteArray.byteArrayToLong(bArray);
        System.out.println(testlong);
    }
}
```

# 创建线程的两种方式
```
package Learning;
public class UsingThread implements  Runnable{

    public static void main(String args[]){
        new Thread(new UsingThread()).start();
        new hyThread(666).start();
    }

    public void run() {
        System.out.println("In thread -1");
    }

}

class hyThread extends Thread{
    public int id;
    public hyThread(int id){
        this.id = id;
    }
    public void run() {
        System.out.println("In thread -2:" + id);
    }       
}
```

# 文件重命名
```
        File f = new File("C:\\");
        //列举目录下的所有文件,判断是否是文件，并重命名后缀名
        for(File t:f.listFiles()){
            if(t.isFile()){

                //System.out.println(t);//输出文件的路径和名字
                //System.out.println(t.getAbsolutePath());

                //System.out.println(t.getParent());//输出路径
                String str[] = t.getName().split("\\.");
                t.renameTo(new File(t.getParent() + File.separator + str[0] + ".mp4"));               
            }
        }
```

# 数组 一行代码初始化
```
final String choicesStr[] = {"剪刀","石头","布"};//选择    
```

# 创建数组作参数
```
new JComboBox<String>(new String[]{"剪刀","石头","布"});
```

# GUI 添加控件事件
```
clearButton.addActionListener(new ActionListener(){
            @Override
            public void actionPerformed(ActionEvent arg0) {
                System.out.println("删档！");
            }
});
```

# Layout 使用
注意：
**GridLayout(1,1); ** 是对于 **panelCenter** 内的控件 **panelCenter** 对于 而言的
**BorderLayout.SOUTH** 是 **panelCenter** 对于 "this"窗口而言
1. 使用步骤，setLayout 之后，依次添加即可
```
JPanel panelCenter = new JPanel(new GridLayout(1,1));
add(panelSouth,BorderLayout.SOUTH);         
```

# Java GUIwindowClosing
必须监听 windowClosing ，否则点×之后，窗口关闭，进程没有退出
```
        //响应关闭窗口
        this.addWindowListener(new WindowAdapter(){
                    @Override
                    public void windowClosing(WindowEvent e){
                        System.exit(0);
                    }
        });
```

# 判断两个数组是否相等
```
        import java.util.Arrays;
        int a[] = {1,1,1,1,2};
        int b[] = {1,1,1,1,2};
        Arrays.equals(a, b);
```

# 焦点移动到下一个控件 ，发送事件 ，发送Tab事件
```
KeyEvent ke = new KeyEvent(某控件,KeyEvent.KEY_PRESSED,0,0,KeyEvent.VK_TAB,KeyEvent.CHAR_UNDEFINED);
某控件.dispatchEvent(ke);    
```



# GUI 布局  ,一般布局
使用panel 和 GridBagLayout 把窗口分成指定大小
再在 panel 里面布置控件
## GridBagLayout 的简单使用
```
GridBagLayout gbLayout= new GridBagLayout();                           
setControlPos(0,0,0,1,0,panelNorth,gbLayout);                                  
setLayout(gbLayout);
void setControlPos(int gridx,int gridy,int gridwidth,double weightx,double weighty, Component comp ,GridBagLayout gbLayout ){
    GridBagConstraints gbConstraint= new GridBagConstraints();
    gbConstraint.fill =  GridBagConstraints.BOTH;
    gbConstraint.gridx = gridx;//设置comp的左上角的位置
    gbConstraint.gridy = gridy;
    gbConstraint.weightx = weightx;//控件长度是否往右延伸
    gbConstraint.weighty = weighty;//控件高度是否往下延伸
    gbConstraint.gridwidth = gridwidth;//控件的宽度,值为0的时候，表示是本行最后一个控件
    gbLayout.setConstraints(comp, gbConstraint);
}
```



# 杨辉三角
```

public class PascalTriangle {
    int arr[] = new int[]{1};

    void next(){
        int tmp[] = new int[arr.length + 1];
        tmp[0] = tmp[tmp.length - 1] = 1;
        for(int i = 1 ; i < arr.length;++i){
            tmp[i] = arr[i - 1] + arr[i];
        }
        arr = tmp;
    }

    public static void main(String[] args) {
        PascalTriangle y = new PascalTriangle();
        int cnt = 10;
        String str[] = new String[cnt];

        for(int i = 0 ; i < cnt ; ++i){
            str[i] = "";
            for(int j = 0 ; j < y.arr.length ; ++j){
                str[i] = str[i] + y.arr[j] + " ";
            }
            y.next();
        }

        for(int i = 0 ; i < cnt ; ++i){
            for(int j = 0 ; j < (str[str.length - 1].length() - str[i].length()) / 2; ++j){
                System.out.print(" ");
            }
            System.out.println(str[i]);
        }

    }

}
```


# 从控制台中输入数据
```
        import java.util.Scanner;
        Scanner scanner = new Scanner(System.in);
        if(scanner.hasNextInt()){
            count = scanner.nextInt();
        }

```


[1]:assets/javaExamples-16370.png
