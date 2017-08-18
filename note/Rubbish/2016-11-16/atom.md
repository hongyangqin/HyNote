再次安装的时候，完善截图等

# 插件安装
1. 安装node.js
2. 下载插件安装包
3. 解压到 C:\Users\qhy\.atom\packages 目录
4. 命令行 cd 到那里目录
5. 运行
    ```
    npm install
    ```

# 常用插件
1. atom-local-history
    历史纪录插件，能进行备份

2. atom-pdf-view
    在 atom 里面直接打开 pdf 文件

3. atom-simplified-chinese-menu
    汉化显示

4. markdown-image-helper
    贴图插件，从剪贴板 中 粘贴图片到 .md 中，图片会复制到跟木下 assets 目录下，图片名字前缀 和 文件名相同

5. markdown-preview-enhanced-0.8.7
    实时显示，同步显示

6. sync-settings
    同步配置
    ```
    Usage:
    sync-settings:backup
    sync-settings:restore
    sync-settings:fork
    sync-settings:view-backup
    sync-settings:check-backup
    sync-settings:fork
    ```

# 使用国内源（包括直接在atom内安装）
1. npm使用国内源

2. apm使用国内源(这个修改了才能在atom内使用国内源)
    1. 在 `C:\Users\用户名\.atom目录` 下，创建 名字为 ` .apmrc` 文件（没错，只有后缀名）
    2. 使用记事本打开这个文件，输入一下内容(注意每行后面没有空格)
        ```
        registry=https://registry.npm.taobao.org/
        strict-ssl=false
        ```
    3. 检查是否成功
        ```
        apm install --check
        ```
        出现 `done` 就表示正确（很快的）
        ![1]



[1]:assets/atom-a56ac.png
