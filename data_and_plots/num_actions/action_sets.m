clear;clc;
set(0,'defaultfigurecolor','w');
load('fp_performance.mat');
load('a5times4.mat');
load('a5times6.mat');
load('a5times8.mat');
load('a5times10.mat');
load('a8times4.mat');
load('a8times6.mat');
load('a8times8.mat');
load('a8times10.mat');
plot(fp_performance,'LineWidth',1)
hold on
plot(a54,'LineWidth',1)
plot(a56,'LineWidth',1)
plot(a58,'LineWidth',1)
plot(a510,'LineWidth',1)
plot(a84,'LineWidth',1)
plot(a86,'LineWidth',1)
plot(a88,'LineWidth',1)
xlabel('x')
ylabel('y')
grid on
handle = legend('ideal FP', '$Q_1=5, Q_2=4$', '$Q_1=5, Q_2=6$','$Q_1=5, Q_2=8$','$Q_1=5, Q_2=10$','$Q_1=8, Q_2=4$','$Q_1=8, Q_2=6$','$Q_1=8, Q_2=8$','Location', 'best');
set(handle, 'interpreter','latex')