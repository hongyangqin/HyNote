# Linear Regression

hypothesis:
$$h_\theta(x) = \theta^Tx = \theta_0 + \theta_1x$$

cost function:
$$J(\theta) = \frac{1}{2m} \sum_{i = 1}^m \left ( h_\theta(x^{(i)}) - y^{(i)} \right )^2$$

gradient of cost function:
$$\frac{\partial J(\theta)}{\partial \theta_j} = \frac{1}{m} \sum_{i = 1}^m \left ( h_\theta(x^{(i)}) - y^{(i)} \right )x_j^{(i)}$$
,$\forall j \in [0 , D] , x^{(i)}_0 = 1$