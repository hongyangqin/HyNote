<!--toc-->

- [Android 应用程序框架](#android-应用程序框架)
- [调试器的使用](#调试器的使用)
- [LOGCAT的使用](#logcat的使用)
- [界面布局](#界面布局)
	- [线性布局](#线性布局)
	- [相对布局](#相对布局)
	- [表格布局](#表格布局)
	- [帧布局](#帧布局)
	- [网格布局](#网格布局)
- [TextView 控件](#textview-控件)
	- [案例 跑马灯效果](#案例-跑马灯效果)
	- [显示文字和图片](#显示文字和图片)
- [Button 按钮](#button-按钮)
	- [Button 按钮的4种监听](#button-按钮的4种监听)
- [CheckBox](#checkbox)
	- [常用事件/属性](#常用事件属性)
- [Toast](#toast)
- [RadioButtonm](#radiobuttonm)
- [EditText](#edittext)
	- [常用属性/事件/方法/对象](#常用属性事件方法对象)
	- [明密文切换](#明密文切换)
- [ImageView 控件](#imageview-控件)
	- [常用](#常用)
- [ImageButton 控件](#imagebutton-控件)
- [AdapterView 控件](#adapterview-控件)
	- [常用](#常用-1)
	- [给listView添加列表头和列表尾](#给listview添加列表头和列表尾)
	- [省市区的三级联动](#省市区的三级联动)
- [Adapter](#adapter)
	- [使用方法](#使用方法)
	- [自定义Adapter](#自定义adapter)
	- [自定义布局文件](#自定义布局文件)
- [AutoCompleteTextView 自动补全](#autocompletetextview-自动补全)
	- [常用](#常用-2)
- [Activity](#activity)
	- [入口Activity](#入口activity)
	- [常用](#常用-3)
	- [Activity 的生命周期](#activity-的生命周期)

<!-- tocstop -->
<!--unfinished-->
# Android 应用程序框架
res资源文件的索引R.XXX.XXX
在xml中引入res的资源 @

# 调试器的使用

# LOGCAT的使用
LOG.i.("cat",);

# 界面布局
每一个控件都是view，
多个view组成一个 viewgroup (relativeLayout)
view最多不要嵌套超过10层(系统本身就包括了两层)

## 线性布局
线性布局：有权重layout_weight
在线性布局中，先给无权重的控件分配空间，剩余空间再给有权重的空间按照权重分配

## 相对布局
相对布局的控件一般都有id这个属性。
id = @+id/button:'+'表示系统中本来不存在的id值，需要将这个id值添加到系统中
@id/button：表示从系统中已经存在的id

对其某个控件右方:layout_toRightOf='@id/button1'

对其某个控件右方，基准线对其(中轴线相同)：align_Baseline="@id/button"

怎么检验相对布局的属性:看控件视图的箭头及箭头长度

相对布局一般都不会给定很多相关联的属性，因为越多越麻烦越复杂

## 表格布局
类似表格排布

## 帧布局
以坐标(0,0)放组件，后面出现的组件会覆盖前面出现的组件。可以用于实现动画效果。

## 网格布局
可以实现合并行/列的效果

# TextView 控件
用来显示文本的控件，文本域
常用属性：
1. text:文字属性
	android:text = "@string/helloword"
2. textColor:文字颜色
	android:textColor = "#00ff00"
3. textSzie:文字大小
	android:textSzie="20sp"
4. visibility 可见性
	android:visibility="visible/invisible/gone"
5. maxLength
	超过长度后续的内容不会显示
6. maxLines
	超过指定行数就不会显示
7. autoLink
	可以指定链接，点击可以打开
8. singleLine 单行显示
	singleLine="true"
9. ellipsize
	none:没
	start:省略开头
	middle:省略结尾
	marquee:跑马灯效果
10. focusableInTouchMode
	true/false
11. focusable
	true/false
12. scrollHorizontally
	水平滚动
	true/false
13. background 背景
	android:background="@drawable/xxx"

14. drawableTop
	显示图片，同时文字在图片上方

## 案例 跑马灯效果
文字循环滚动显示，必须要获取焦点
ellipsize="marquee"
focusable="true"
focusableInTouchMode="true"
marqueeRepeatLimit="marquee_forever"
scrollHorizontally="true"
singleLine="true"

## 显示文字和图片
设置background的话，会文字图片会重叠
应该设置 drawableTop 等属性

# Button 按钮
## Button 按钮的4种监听
1. 使用匿名内部类
	```
	//通过id找到关联布局中的view控件
	Button btn = (Button)findViewById(R.id.xxx);
	btn.setOnClickListener(new view.onClickListener(){
		poublic void onClick(View v){
			//do something
		}
	});
	```
2. 在XML文件中定义onClick属性，在java代码中对应方法
	```
	//xxx_main.xml文件中
	android:onClick="xxx"
	//MainActivity.java中添加对相应的xxx方法
	public void xxx(View v){
		//do something
	}
	```
3. Activity实现onClickListener接口
	实际上就是调用 setOnClickListener 和方法1一样

4. 其他类实现onClickListener
	实际上就是调用 setOnClickListener 和方法1一样

# CheckBox
选择框，只有选中和未选中的两种状态
## 常用事件/属性
1. onCheckedChangedListener

2. text 文字内容
3. isChecked 是否选中

# Toast
Toast 提示机制，不能和用户交互
```
Toast.makeText(this,"xxx",Toast.LENGTH_SHORT).show();
```

# RadioButtonm
单选按钮，在同一个RadioGroup中只有一个能被选中

# EditText
EditText 可编辑文本控件，继承自TextView

## 常用属性/事件/方法/对象
1. TextWatcher 对象
```
xxx.addTextChangedListener(new TextWatcher(){//xxxxx});
```

2. ems 属性
	默认EditText的长度
	android:ems="xx"
3. inputType 输入类型

4. hint 提示
	编辑框灰色字提示

5. 	setSelection
	设置光标位置

6. setCursorVisible
	设置光标是否显示

## 明密文切换
仅仅更改inputType是不行的
```
//显示明文
xxx.setTransformationMethod(HideReturnsTransformationMethod.getInstance());
//显示密文
xxx.setTransformationMethod(PasswordTransformationMethod.getInstance());
//修改之后，光标位置移动到了前面，需要移动光标到文字末尾
xxx.setSelection(xxx.getText().length());
```

# ImageView 控件
ImageView 用来显示图片的控件。

## 常用
1. src
	指定当前ImageView中填充的内容

2. BackGround
	指定当前控件的背景

3. setImageResource 方法
	设置src

4. scaleType 属性
	用来呈现图片的不同显示类型，如何进行缩放，以及显示图片的整体还是部分等
	centerGroup
	centerInside
	matrix

5. setScaleType 方法
	设置scaleType属性

# ImageButton 控件
ImageButton 带图片的按钮,继承自ImageView

# AdapterView 控件
AdapterView 为 Adapter的控件
把Adapter的数据进行显示的控件
```
xxxAdapterView.setAdapter(xxxAdapter);
```
1. ListView 列表

2. Spinner 下拉列表

3. GridView 网格图

## 常用
1. onItemClick
	setOnItemClickListener 来设置
	一个项目被点击的时候产生的事件。

2. onItemLongClick
	长按事件,返回false会产生Click事件

## 给listView添加列表头和列表尾
```
//在setAdapter之前设置
xxxlistView.setHeaderView()
xxxlistView.setFooterView()
```
## 省市区的三级联动
spinner的关联,实际上就是一个spinner的onSelected事件里面给下一级setAdapter

# Adapter
AdapterView 的数据源

1. ArrayAdapter
	单数据的时候进行显示，即每个列表项只有一个控件

2. SimpleAdapter
	一个列表项有多个控件

3. 自定义Adapter
	就是继承 BaseAdapter 自己写

## 使用方法
可以直接用 ArrayList 进行 Adapter的初始化
```
new Adapter<String>(this,android.R.layout.simple_list_item_1,xxlist)
```
也可以读取xml中的string-array进行初始化
```
ArrayAdapter.createFromResource(this,R.layout.simple_list_item_1,xxarray_stringId)
```

每次修改数据源list中的数据，需要通知Adapter修改
```
xxxadapter .notifyDataSetChanged();
```

SimpleAdapter在初始化的时候，需要构建的数据源格式为ArrayList<Map<String,Object>>

通过from和to来达到Map中的key和to中的id进行对应

## 自定义Adapter
自定义Adapter之getView 自定义渲染一个item
1. 根据自定义好的xml文件转换view对象
	使用布局映射器
	```
	LayoutInflater.from(xxx.this).inflate(R.layout.XXX_xmlid,null);
	```
2. 给view对象中的控件进行赋值
	```
	xxcontrol = xxxView.findViewById();
	xxcontrol.setxxx();
	```
3. 增加缓存机制
	每一个item都创建一个item，会极大的消耗内存，但是屏幕能显示的item数目是固定的，所以增加缓存机制来优化。

	实际上不需要自己创建控件，getView有一个参数就是convertView 就是可以复用的控件
	当convertView为空的时候才需要创建一个新的view
	```
	//convertView是不能直接操作的，所以需要Holder对象来保存需要操作的控件
	//每次创建view的时候要保存
	xxxholder = new Holder();
	xxxholder.tv = convertView.findViewById(R.id.xxx);
	convertView.setTag(xxxholder);

	//复用的时候直接获取holder进行赋值
	xxxholder = convertView.getTag();
	xxxholder.tv.setxxx();
	```

## 自定义布局文件
文件名一般以item进行结尾
根节点为 TextView

# AutoCompleteTextView 自动补全
```
xxxAutoCopmpleteTextView.setAdapter();

```

## 常用
completionHint：设置出现在下拉菜单的提示标题
completionThreshold:设置用户至少输入多少才出现提示
dropDownHorizontalOffset
dropDownHeight
dropDownWidth
singleLine

# Activity
Activity:活动，一个页面就是一个活动,可以处理和用户交互的工作。

## 入口Activity
程序的入口
入口Activity ：在 xxxMainifsest中进行配置，在对应的activity下添加一下代码
```
<intent-filter>
	<action android:name="android.intent.action.MAIN" />
	<category android:name="android.intent.category.LAUNCHER" />
</intent-filter>
```

## 常用
2. startActivity
	跳转到新的activity
	```
	Intent intent = new Intent(当前Activity.this,目标Activity.class);
	startAcstivity(intent);
	`
## Activity 的生命周期
1. onCreate
	实例被创建

2. onStart
	启动当前activity的方法

3. onResume
	如果该方法执行，那么页面的实例就能和用户进行交互

4. onPause
	如果该方法执行，那么页面就和用户不交互，失去焦点，但是页面仍可见

5. onStop
	页面不可见

6. onDestroy
	销毁当前activity实例

7. onRestart
	当程序从后台重新显示到前台的时候会调用（后面一般也调用onStart onResume）
