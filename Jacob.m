function [W] = Jacob(N,X,Phi)
W(1:N,1:N) = 0;
	for k = 1:N
		for i = 1:N
			for j = 1:N
				W(k,i) = W(k,i) - sin(2*pi*Phi(k)*(i-j)/N + X(i) - X(j));
			end
		end
	end
