# latex 多子图

```latex
\usepackage{subfigure}
\begin{figure*}[!htbp]
    \centering
    \subfigure[title1]{
        \includegraphics[width = 0.3\textwidth]{...}
    }
    \subfigure[title2]{
        \includegraphics[width = 0.3\textwidth]{...}
    }
    \caption{...}
    \label{...}
\end{figure*}
```

```latex
\usepackage{subfig}
\begin{figure*}[!htbp]
    \centering
    \subfloat[title1]{
        \includegraphics[width = 0.3\textwidth]{...}
    }
    \subfloat[title2]{
        \includegraphics[width = 0.3\textwidth]{...}
    }
    \caption{...}
    \label{...}
\end{figure*}
```