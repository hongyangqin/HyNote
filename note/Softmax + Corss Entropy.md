# Softmax + Corss Entropy

Softmax + Corss Entropy 公式与梯度推导

## 符号定义

样本数目：$N$

样本维度：$D$

类别数：$K$

输入数据：$X\in R^{N\times D}$

标签：$Y \in R^{N\times K}$

神经元数目：$n$

激活值：$\phi\in R^{N\times n}$

全连接：$Y_{score} \in R^{N\times K}$

全连接层权重：$W \in R^{k \times (n + 1)}$

激活值拼接偏置项：$\hat \phi\in R^{N\times (n + 1)}$

softmax 层：$Y_{softmax} \in R^{N\times K}$

损失函数：$E \in R^{1\times 1}$

样本索引：$i$

神经元索引：$j$

类索引:$k$

## 计算公式

$$\phi_{i,j} = \phi_j(x_i)$$

$$\hat \phi_{i,:} = [1,\phi_{i,:}]$$

$$Y_{score,i,k} = \sum_{j = 1}^n w_{k,j}\hat \phi_{i , j}$$

$$Y_{softmax,i,k} = \frac{exp{(Y_{score,i,k} - a)}}{
    \sum_{kk = 1}^K exp{(Y_{score,i,kk} - a)}
}$$

$$E = -\frac{1}{N} \sum_{i = 1}^N \sum_{k = 1}^K Y_{i,k}\log Y_{softmax,i,k} $$

$$\frac{\partial E}{\partial Y_{softmax,i,k}} = -\frac{1}{N} \frac{Y_{i,k}}{Y_{softmax,i,k}}$$

$$\frac{\partial Y_{softmax,i,k}}{\partial Y_{score,i,k} } = \frac{\left (exp{(Y_{score,i,k} - a)}\right )^2}{
    \left (\sum_{kk = 1}^K exp{(Y_{score,i,kk} - a)}\right )^2
} + \frac{exp{(Y_{score,i,k} - a)}}{
    \sum_{kk = 1}^K exp{(Y_{score,i,kk} - a)}
} =  - Y_{softmax,i,k}^2 + Y_{softmax,i,k} $$

$$\frac{\partial Y_{softmax,i,k'}}{\partial Y_{score,i,k} } = -\frac{exp{(Y_{score,i,k'} - a)}exp{(Y_{score,i,k} - a)}}{\left  (\sum_{kk = 1}^K exp{(Y_{score,i,kk} - a)}\right )^2},k \neq k'$$

$$ \frac{\partial Y_{score,i,k}}{\partial w_{k,j}} = \hat \phi_{i,j}$$

$$ \frac{\partial  Y_{score,i,k}}{\partial \hat \phi_{i,j}} =   w_{k,j}$$

$$\begin{array}{ll}
\frac{\partial E}{\partial w_{k,j}} &= \sum_{i = 1}^N \frac{\partial E}{\partial Y_{softmax,i,k}}  \frac{\partial Y_{softmax,i,k}}{\partial Y_{score,i,k} } \frac{\partial Y_{score,i,k}}{\partial w_{k,j}} +  \sum_{i = 1}^N \sum_{k' = 1 , k'\neq k}^K \frac{\partial E}{\partial Y_{softmax,i,k'}}  \frac{\partial Y_{softmax,i,k'}}{\partial Y_{score,i,k} } \frac{\partial Y_{score,i,k}}{\partial w_{k,j}} \\&= -\frac{1}{N} \sum_{i = 1}^N \left ( \frac{Y_{i,k}}{Y_{softmax,i,k}} \left (  - Y_{softmax,i,k}^2 + Y_{softmax,i,k} \right ) \hat \phi_{i,j} - \sum_{k' = 1 , k'\neq k}^K \frac{Y_{i,k}}{Y_{softmax,i,k'}} \frac{exp{(Y_{score,i,k'} - a)}exp{(Y_{score,i,k} - a)}}{\left  (\sum_{kk = 1}^K exp{(Y_{score,i,kk} - a)}\right )^2} \hat \phi_{i,j} \right )\\&=
-\frac{1}{N} \sum_{i = 1}^N  \left (Y_{i,k}
     \frac{1}{Y_{softmax,i,k}} \left (  - Y_{softmax,i,k}^2 + Y_{softmax,i,k} \right ) \hat \phi_{i,j} - \sum_{k' = 1 , k'\neq k}^K Y_{i,k'}\frac{1}{Y_{softmax,i,k'}} Y_{softmax,i,k'}Y_{softmax,i,k} \hat \phi_{i,j} 
\right )
\\&=
-\frac{1}{N} \sum_{i = 1}^N  \left (Y_{i,k}
     \left (  - Y_{softmax,i,k} + 1 \right ) - \sum_{k' = 1 , k'\neq k}^K Y_{i,k'} Y_{softmax,i,k}
\right )\hat \phi_{i,j}
\\&=
-\frac{1}{N} \sum_{i = 1}^N  \left (Y_{i,k} -  Y_{softmax,i,k}
\right )\hat \phi_{i,j}
\\&=
\frac{1}{N} \sum_{i = 1}^N  \left (Y_{softmax,i,k} - Y_{i,k}
\right )\hat \phi_{i,j}
\end{array}
$$

$$
\begin{array}{ll}
\frac{\partial E}{\partial Y_{score,i,k}}
&=  \frac{\partial E}{\partial Y_{softmax,i,k}}  \frac{\partial Y_{softmax,i,k}}{\partial Y_{score,i,k} }  +   \sum_{k' = 1 , k'\neq k}^K \frac{\partial E}{\partial Y_{softmax,i,k'}}  \frac{\partial Y_{softmax,i,k'}}{\partial Y_{score,i,k} }
\\&= -\frac{1}{N}  \left ( \frac{Y_{i,k}}{Y_{softmax,i,k}} \left (  - Y_{softmax,i,k}^2 + Y_{softmax,i,k} \right )  - \sum_{k' = 1 , k'\neq k}^K \frac{Y_{i,k}}{Y_{softmax,i,k'}} \frac{exp{(Y_{score,i,k'} - a)}exp{(Y_{score,i,k} - a)}}{\left  (\sum_{kk = 1}^K exp{(Y_{score,i,kk} - a)}\right )^2}  \right )
\\&=
-\frac{1}{N}   \left (Y_{i,k}
     \frac{1}{Y_{softmax,i,k}} \left (  - Y_{softmax,i,k}^2 + Y_{softmax,i,k} \right )  - \sum_{k' = 1 , k'\neq k}^K Y_{i,k'}\frac{1}{Y_{softmax,i,k'}} Y_{softmax,i,k'}Y_{softmax,i,k} 
\right )
\\&=
-\frac{1}{N}   \left (Y_{i,k}
     \left (  - Y_{softmax,i,k} + 1 \right ) - \sum_{k' = 1 , k'\neq k}^K Y_{i,k'} Y_{softmax,i,k}
\right )
\\&=
\frac{1}{N}  \left ( Y_{softmax,i,k} - Y_{i,k}
\right )
\end{array}
$$

$$\frac{\partial E }{\partial \beta_j} = \sum_{i = 1}^N \sum_{k = 1}^K \frac{\partial E}{\partial Y_{score,i,k}}\frac{\partial Y_{score,i,k}}{\partial \partial \hat \phi_{i,j}} \frac{\partial \phi_{i,j}}{\partial \beta_j}
=  \frac{1}{N} \sum_{i = 1}^N \sum_{k = 1}^K \left ( Y_{softmax,i,k} - Y_{i,k}\right )
w_{k,j}
\sum_{s = 1}^S exp\left (-\beta_j * (x_i[s] - c_j[s])^2 \right) \left (- (x_i[s] - c_j[s])^2\right )
$$

$$\begin{array}{ll}
\frac{\partial E}{\partial w_{k,j}} &= \sum_{i = 1} ^N  \frac{\partial E}{\partial Y_{score,i,k}} \frac{\partial Y_{score,i,k}}{\partial w_{k,j}}
\\&=
\sum_{i = 1} ^N   \frac{1}{N}  \left ( Y_{softmax,i,k} - Y_{i,k}
\right )\hat \phi_{i,j}
\end{array}$$

## 参考

[Peter's Notes](http://peterroelants.github.io/posts/neural_network_implementation_intermezzo02/)