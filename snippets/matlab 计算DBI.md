# matlab 计算DBI

计算 Davies Bouldin Index(DBI)

$$
\begin{align}
    DBI = \frac{1}{k} \sum_{i = 1}^k \max_{j\neq i}\left ( \frac{avg(C_i) + avg(C_j)}{d_{cen}(C_i,C_j)} \right )\\
    avg(C) = \frac{2}{|C|(|C| - 1)}\sum_{1\leq i\leq j\leq |C| dist(x_i,x_j)}\\
    d_{cen}(C_i,C_j) = dist(\mu_i,\mu_j)
\end{align}
$$

```matlab
function DB = getDB(p)
    % p(:,1:2) 数据
    % p(:,3) 类别标签
    index = p(:,3);
    clusts = unique(index);
    num = length(clusts);
    if num == 1
        DB = nan;
        return;
    end
    centroids = NaN(num,size(p,2));

    aveWithinD= zeros(num,1);
    for i = 1:num
        members = (index == clusts(i));
        if any(members)
            centroids(i,:) = mean(p(members,:),1) ;
            aveWithinD(i)= mean(pdist2(p(members,:),centroids(i,:)));
        end
    end

    interD = pdist(centroids,'euclidean'); %Euclidean distance
    R = zeros(num);
    for i = 1:num
        for j=i+1:num %j>i
            R(i,j)= (aveWithinD(i)+aveWithinD(j))/ interD((i-1)*(num-i/2)+j-i);%d((I-1)*(M-I/2)+J-I)
        end
    end
    R=R+R';

    RI = max(R,[],1);
    DB = mean(RI);
end
```