function [Q,c] = genquadknap(n,dens,seed)

rand('twister',seed);

Q = zeros(n);
for i = 1:n
  for j = 1:i
    if rand*100 <= dens
      Q(i,j) = ceil( 101 * rand ) - 51;
    end
    if i ~= j
      Q(j,i) = Q(i,j);
    end
  end
end

c = zeros(n,1);
for i = 1:n
  c(i) = ceil( 101 * rand ) - 51;
end

