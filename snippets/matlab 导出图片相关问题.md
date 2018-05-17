# matlab 导出图片相关问题

1. 如何导出高清的图片?
    主要是导出矢量图(pdf,svg格式),函数有`saveas`和`print`等

2. 如何控制大小?
    通过`gca,gcf`的`position`等属性控制
    ```matlab
    set(gcf, 'outerposition', [0           0       400 400]);
    ```
3. 如何控制导出图片的边距? 导出图片的白边特别多?
    ```matlab
    set(gca,'looseInset',[0 0 0 0]);
    set(gca,'LooseInset',get(gca,'TightInset'))
    ```

4. 如何控制导出的pdf的页面大小为所显示图片大小?导出的pdf默认A4大小?
    通过控制`papersize`图片的大小
    ```matlab
    function mysaveas(h, filename)
        set(h,'Units','Inches');
        pos = get(h,'Position');
        set(h,'PaperPositionMode','Auto','PaperUnits','Inches','PaperSize',[pos(3), pos(4)])
        print(h,filename,'-dpdf','-r0')

    mysaveas(gcf, str);
    ```

5. 如何直接导出图片而不显示?
    ```matlab
    set(h, 'Visible', 'off');
    ```

6. 控制legend的位置
    ```matlab
    set(h,'Location','south')
    ```

7. 设置legend的字体大小
    ```matlab
    set(h,'Fontsize',6);
    ```
## 参考
* [Create Figure Without Displaying it - MATLAB Answers - MATLAB Central](https://ww2.mathworks.cn/matlabcentral/answers/43326-create-figure-without-displaying-it)
* [如何通过代码实现放大坐标轴至充满图形？ – MATLAB中文论坛](http://www.ilovematlab.cn/thread-297264-1-1.html)
* [Legend Position on a plot - MATLAB Answers - MATLAB Central](https://ww2.mathworks.cn/matlabcentral/answers/12555-legend-position-on-a-plot)
* [在坐标区上添加图例 - MATLAB legend](https://ww2.mathworks.cn/help/matlab/ref/legend.html?#bt6ef_q-1-lcn)
* [How to save a MATLAB graphic in a right size .pdf? - MATLAB Answers - MATLAB Central](https://ww2.mathworks.cn/matlabcentral/answers/12987-how-to-save-a-matlab-graphic-in-a-right-size-pdf)
* [Matlab的legend输出字怎么设置字体大小？ – MATLAB中文论坛](http://www.ilovematlab.cn/thread-69390-1-1.html)