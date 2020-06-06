clear;clc;
set(0,'defaultfigurecolor','w');
load('fp_performance.mat');
load('CTDE.mat');
load('DTDE.mat');
plot(fp_performance,'LineWidth',1)
hold on
plot(DTDE,'m','LineWidth',1)
plot(CTDE,'c','Linewidth',1)
xlabel('x')
ylabel('y')
grid on