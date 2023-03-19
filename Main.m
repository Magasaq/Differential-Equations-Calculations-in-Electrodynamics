clear all
Phi  = importdata('Field.txt');
I = importdata('Ic.txt');
N = length(I);
for i = 1:N
    X(i) = (i-)
end
X = X';
W  = Jacob(N,X,Phi);
%%
F =  FNew(N,X,Phi,I);
F = F';
Winv = inv(W);
XNew = X - Winv*F;