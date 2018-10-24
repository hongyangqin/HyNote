% 定义变量
syms x y

% 使用变量定义公式
z = x + x + y

% 化简公式
z = simplify(z)
% z = 2*x + y

% 偏导
dzx = diff(z , x)
% dzx = 2

% 代入值计算
vz1 = subs(z , [x] , [1])
vz2 = subs(z , [x y] , [1 2])
% vz1 = y + 2
% vz2 = 4


syms a b x y;
f = (a + b * x - y)^2;
E = subs(f , [x y], [1 1000/931]) + subs(f , [x y], [1.4 1000/473]) + subs(f , [x y], [1.8 1000/297]) + subs(f , [x y], [2.2 1000/224]) + subs(f , [x y], [2.6 1000/168]);
% E = simplify(E);

da = diff(E , a)
db = diff(E , b)

syms a b x y;
f = (a*x + b * x^2 - y)^2;

E = subs(f , [x y], [1 0.8]) + subs(f , [x y], [2 1.5]) + subs(f , [x y], [3 1.8]) + subs(f , [x y], [4 2]);
% E = simplify(E);

da = diff(E , a)
db = diff(E , b)