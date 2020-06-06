clear;clc;
set(0,'defaultfigurecolor','w');
load('fp_performance.mat');
load('greedy_performance.mat');
load('random_performance.mat');
load('drl_performance.mat');
plot(fp_performance,'k','LineWidth',1)
hold on
plot(drl_performance,'b','LineWidth',1)
plot(greedy_performance,'c','LineWidth',1)
plot(random_performance,'m','LineWidth',1)
xlabel('x')
ylabel('y')
grid on