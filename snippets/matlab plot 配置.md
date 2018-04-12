# matlab plot 配置

* 配置网格线
* 配置标签
* 各个子图配置(图上而不是数据)等间隔的的网格线

```matlab
% 设置 plot的窗口的大小和位置
set(gcf, 'outerposition', [0           0        400   400]);

% 设置x 和 y轴的取值
set(gca, 'ytick',linspace(0,1,9));
set(gca, 'xtick',linspace(0,1,9));

% 设置x,y取值范围, 上面那个设置是画出来的数值
set(gca, 'YLim',[0.5 0.95]);
set(gca, 'XLim',[0 21]);

% 打开网格, 也可以用set
grid on;
% set(gca, 'YGrid','on');
% 只画横线

% 隐藏y轴上的数值标识
set(gca,'yticklabel',[]);

% 图注
legend('line 1','line 2' );

% 设置标签
ylabel('x');
xlabel('y');

% 标题
title('title');
```

## 参考

[控制图窗窗口的外观和行为 - MATLAB - MathWorks 中国](https://ww2.mathworks.cn/help/matlab/ref/matlab.ui.figure-properties.html)
[控制坐标区的外观和行为 - MATLAB - MathWorks 中国](https://ww2.mathworks.cn/help/matlab/ref/matlab.graphics.axis.axes-properties.html#budumk7-XTick)
[设置图形对象属性 - MATLAB set - MathWorks 中国](https://ww2.mathworks.cn/help/matlab/ref/set.html)