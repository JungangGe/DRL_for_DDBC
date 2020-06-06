clear;clc;
set(0,'defaultfigurecolor','w');
load('fp_performance.mat');
plot(fp,'LineWidth',1)
hold on
for v = 3:7
    filename = ['u=', num2str(v),'.mat'];
    load(filename)
    cmd = ['plot(u',num2str(v),',''LineWidth'',1)'];
    eval(cmd)
end
grid on
legend('ideal FP','U=3','U=4','U=5','U=6','U=7','Location','best')