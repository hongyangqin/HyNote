# How to accelerate exponent (exp) calculation in MATLAB?

如何加速exp的计算?

1. 多个exp并行化
2. 更好的CPU?
3. 不知道GPU能不能加速?

> No. exp() is an expensive operation. The only way to accelerate it is to reduce repeated calls with the same argument.
> 
> I've experimented with the implementation of netlib.org, but did not found a significant acceleration and the results are lesss accurate. I assume this is the reason why it is not used in Matlab (in opposite to e.g. acos, which is taken from netlib).
> 
> A parfor loop might help to distribute the calculation to multiple cores.
> 
> Note: Think twice. If there would be a way to accelerate the computation of a specific function, it would have been included by Mathworks certainly. It is very pitty, but there are no magic tricks to make Matlab faster.

## 参考

[How to accelerate exponent (exp) calculation in MATLAB? - MATLAB Answers - MATLAB Central](https://cn.mathworks.com/matlabcentral/answers/336461-how-to-accelerate-exponent-exp-calculation-in-matlab)