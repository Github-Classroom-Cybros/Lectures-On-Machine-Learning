x= [1 1 -1 -1;1 -1 1 -1];
t= [1 -1 -1 -1];
w= [0 0];
b=0;

for i= 1:4;
    for j= 1:2
        w(j)=w(j)+t(i)*x(j,i);
    end
    b= b+t(i);
end

disp('Final Weight Matrix: ');
disp(w);
disp('Final bias Values');
disp(b);

% Plotting by Linear Separability Concept
plot(x(1,1),x(2,1), 'or','MarkerSize',20,'MarkerFaceColor',[0 0 1]);hold on;
plot(x(1,2),x(2,2), 'or','MarkerSize',20,'MarkerFaceColor',[1 0 0]);hold on;
plot(x(1,3),x(2,3), 'or','MarkerSize',20,'MarkerFaceColor',[1 0 0]);hold on;
plot(x(1,4),x(2,4), 'or','MarkerSize',20,'MarkerFaceColor',[1 0 0]);hold on;
hold on;

m= -(w(1)/w(2));
c= -b/w(2);

x1=linspace(-2,2,100);
x2=m*x1+c;
plot(x2,x1,'r');
axis([-2 2 -2 2]);
