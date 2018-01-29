# 使用 libsvm 时 自定义 kernel

参数`-t 4` ， 训练和测试输入数据为`核矩阵`而不是`原始数据` ， 注意`核矩阵` 第一列为索引（从1开始） ， 后面才是核矩阵的内容

libsvm参数说明：

```batch
-t kernel_type : set type of kernel function (default 2)
    0 -- linear: u'*v
    1 -- polynomial: (gamma*u'*v + coef0)^degree
    2 -- radial basis function: exp(-gamma*|u-v|^2)
    3 -- sigmoid: tanh(gamma*u'*v + coef0)
    4 -- precomputed kernel (kernel values in training_instance_matrix)
```

示例：

计算RBF核矩阵

```matlab
function [trainning_kernel , test_kernel] = calcGRBFKernel(trainning_x , test_x , savefilename)

if ~exist(strcat(savefilename , '_trainning_kernel', '.mat') , 'file'),
    n_trainning = size(trainning_x , 1);
    trainning_kernel = [(1:n_trainning)' exp(-0.01 .* pdist2(trainning_x,trainning_x,'euclidean').^2)];
    save(strcat(savefilename , '_trainning_kernel', '.mat') , 'trainning_kernel');
end

if ~exist(strcat(savefilename , '_test_kernel', '.mat') , 'file'),
    n_test = size(test_x , 1);
    test_kernel = [(1:n_test)' exp(-0.01 .* pdist2(test_x,trainning_x,'euclidean').^2)];
    save(strcat(savefilename , '_test_kernel', '.mat') , 'test_kernel');
end

load(strcat(savefilename , '_trainning_kernel', '.mat'));
load(strcat(savefilename , '_test_kernel', '.mat'));
```

进行(SwedishLeaf)分类：

```matlab
configPath;
[ trainning_x ,trainning_y , test_x , test_y ] = readData();

[trainning_kernel , test_kernel] = calcGRBFKernel(trainning_x , test_x , 'GRBF_SwedishLeaf');

model = svmtrain(trainning_y , trainning_kernel , '-t 4' );
[predicted_label, accuracy, ~] = svmpredict(test_y , test_kernel , model);

accuracy
```

结果输出：
```batch
optimization finished, #iter = 24
nu = 0.374867
obj = -13.604654, rho = -0.134895
nSV = 25, nBSV = 20
Total nSV = 478
Accuracy = 79.04% (494/625) (classification)

accuracy =

   79.0400
   10.3760
    0.5198
```

参考：
[using precomputed kernels with libsvm
](https://stackoverflow.com/questions/7715138/using-precomputed-kernels-with-libsvm)