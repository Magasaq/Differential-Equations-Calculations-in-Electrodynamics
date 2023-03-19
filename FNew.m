function [F] = FNew(N,X,Phi,I)
F(1:N) = 0;
for k = 1:N
	for i = 1:N
		for j = 1:N
			F(k) = F(k) + cos(2*pi*Phi(k)*(i-j)/N + X(i) - X(j)) ;
        end
    F(k) = F(k) - (I(k)*N)^2;
	end
end
