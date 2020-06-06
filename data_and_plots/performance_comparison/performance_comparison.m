clear;clc;
set(0,'defaultfigurecolor','w');
load('fp_performance.mat');
load('greedy_performance.mat');
load('random_performance.mat');
load('drl_performance.mat');
plot(fp_performance,'LineWidth',1)
hold on
plot(drl_performance,'LineWidth',1)
plot(greedy_performance,'LineWidth',1)
plot(random_performance,'LineWidth',1)
xlabel('x')
ylabel('y')
grid on