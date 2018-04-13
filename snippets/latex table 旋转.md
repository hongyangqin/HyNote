# latex table 旋转

* 这个标题不会旋转, 页面还是竖向

    ```latex
    \rotatebox{90}{
        \begin{tabular}{ll}
        First First & First Second\\
        Second First & Second Second
        \end{tabular}
    }
    ```

* 整个页面旋转

    ```latex
    \documentclass{article}
    \usepackage{pdflscape}

    \begin{document}
    \begin{landscape}
        \begin{tabular}{ll}
        First First & First Second\\
        Second First & Second Second
        \end{tabular}
    \end{landscape}
    \end{document}
    ```

## 参考

[rotating - How to rotate a table? - TeX - LaTeX Stack Exchange](https://tex.stackexchange.com/questions/25369/how-to-rotate-a-table/25371)