# Loss Functions in Artificial Neural Networks

## 常见损失函数

* Mean Squared Error
    $$\boldsymbol{\mathcal{L}}=\frac{1}{n}\sum_{i=1}^{n}(y^{(i)}-\hat{y}^{(i)})^{2}$$

    > widely used in linear regression , 线性回归
    > if using Sigmoid as the activation function, the quadratic loss function would suffer the problem of slow convergence (learning speed), 不适合 sigmoid

* Mean Squared Logarithmic Error
    $$\boldsymbol{\mathcal{L}}=\frac{1}{n}\sum_{i=1}^{n}\big(\log(y^{(i)}+1)-\log(\hat{y}^{(i)}+1)\big)^{2}$$
    > It is usually used when you do not want to penalize huge differences in the predicted and the actual values when both predicted and true values are huge numbers.
    > 适合"大值"

* L2
    $$\boldsymbol{\mathcal{L}}=\sum_{i=1}^{n}(y^{(i)}-\hat{y}^{(i)})^{2}$$

* Mean Absolute Error
    $$\boldsymbol{\mathcal{L}}=\frac{1}{n}\sum_{i=1}^{n}\big\lvert y^{(i)}-\hat{y}^{(i)}\big\rvert$$
    > easier to compute the gradient 梯度

* Mean Absolute Percentage Error
    $$\boldsymbol{\mathcal{L}}=\frac{1}{n}\sum_{i=1}^{n}\bigg\lvert\frac{y^{(i)}-\hat{y}^{(i)}}{y^{(i)}}\bigg\rvert\centerdot100$$
    > It cannot be used if there are zero values

* L1
    $$\boldsymbol{\mathcal{L}}=\sum_{i=1}^{n}\big\lvert y^{(i)}-\hat{y}^{(i)}\big\rvert$$

* Kullback Leibler (KL) Divergence
    $$\boldsymbol{\mathcal{L}}=\frac{1}{n}\sum_{i=1}^{n}\mathcal{D}_{KL}(y^{(i)}||\hat{y}^{(i)})=\frac{1}{n}\sum_{i=1}^{n}\big[y^{(i)}\centerdot\log\big(\frac{y^{(i)}}{\hat{y}^{(i)}}\big)\big]\\=\underbrace{\frac{1}{n}\sum_{i=1}^{n}\big(y^{(i)}\centerdot\log(y^{(i)})\big)}_{\boldsymbol{entropy}}\underbrace{-\frac{1}{n}\sum_{i=1}^{n}\big(y^{(i)}\centerdot\log(\hat{y}^{(i)})\big)}_{\boldsymbol{cross-entropy}}$$
    > a measure of how one probability distribution diverges from a second expected probability distribution
    > 两个分布的距离

* Cross Entropy
    $$\boldsymbol{\mathcal{L}}=-\frac{1}{n}\sum_{i=1}^{n}\big[y^{(i)}\log(\hat{y}^{(i)})+(1-y^{(i)})\log(1-\hat{y}^{(i)})\big]$$
    > commonly-used in classification

* Negative Logarithmic Likelihood
    $$\boldsymbol{\mathcal{L}}=-\frac{1}{n}\sum_{i=1}^{n}\log(\hat{y}^{(i)})$$
    > widely used in neural networks, it measures the accuracy of a classifier.
    > similar to cross entropy

* Poisson
    $$\boldsymbol{\mathcal{L}}=\frac{1}{n}\sum_{i=1}^{n}\big(\hat{y}^{(i)}-y^{(i)}\centerdot\log(\hat{y}^{(i)})\big)$$
    >  measure of how the predicted distribution diverges from the expected distribution

* Cosine Proximity
    $$\boldsymbol{\mathcal{L}}=-\frac{\mathbf{y}\centerdot\mathbf{\hat{y}}}{||\mathbf{y}||_{2}\centerdot||\mathbf{\hat{y}}||_{2}}=-\frac{\sum_{i=1}^{n}y^{(i)}\centerdot\hat{y}^{(i)}}{\sqrt{\sum_{i=1}^{n}\big(y^{(i)}\big)^{2}}\centerdot\sqrt{\sum_{i=1}^{n}\big(\hat{y}^{(i)}\big)^{2}}}$$

* Hinge
    $$\boldsymbol{\mathcal{L}}=\frac{1}{n}\sum_{i=1}^{n}\max(0,m-y^{(i)}\centerdot\hat{y}^{(i)})$$
    > known as max-margin objective used for training classifiers

* Squared Hinge
    $$\boldsymbol{\mathcal{L}}=\frac{1}{n}\sum_{i=1}^{n}\big(\max(0,1-y^{(i)}\centerdot\hat{y}^{(i)})\big)^{2}$$
    > it solves the problem in hinge loss that the derivative of hinge loss has a discontinuity at $y^{(i)}\centerdot\hat{y}^{(i)}=1$

## 参考

[Loss Functions in Artificial Neural Networks | Isaac Changhau](https://isaacchanghau.github.io/2017/06/07/Loss-Functions-in-Artificial-Neural-Networks/)