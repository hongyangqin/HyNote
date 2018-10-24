function S = fuhuaSimpson(a,b,n,f)

a = 0;
b = pi;
n = 8;
f = @(x) sin(x);

h = (b - a)/n;
m = n / 2;

s1 = 0;
s2 = 0;

for k = 1:m
    s1 = s1 + f(a + (2 * k - 1)*h);
end

for k = 1:m - 1
    s2 = s2 + f(a + 2 * k * h);
end

S = h / 3*(f(a) + f(b) + 4 * s1 + 2 * s2);
