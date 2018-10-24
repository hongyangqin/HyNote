function T = fuhuatixingqiuji(a , b, n, f)

a = 0;
b = pi;
n = 8;
f = @(x) sin(x);

h = (b - a)/n;
sum = 0;
for k =1 : n - 1
    sum = sum + f(a + k * h);
end

T = h / 2 * (f(a) + f(b) + 2 * sum);