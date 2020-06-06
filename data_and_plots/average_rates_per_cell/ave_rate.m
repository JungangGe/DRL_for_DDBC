close all; clear;
set(0,'defaultfigurecolor','w');
load('drl_rates.mat');
load('fp_rates.mat');
load('greedy_rates.mat');
load('random_rates.mat');
idx = (0:18)';
ave_drl = topo_map(mean(drl_rates(90000:100000, :)));
ave_fp = topo_map(mean(fp_rates(90000:100000, :)));
ave_random = topo_map(mean(random_rates(90000:100000, :)));
ave_greedy = topo_map(mean(greedy_rates(90000:100000, :)));
ave_rates = [ave_fp',ave_drl',ave_greedy',ave_random'];
% mean(ave_fp)
% mean(ave_drl)
% mean(ave_greedy)
% mean(ave_random)
b = bar((0:18)', ave_rates);
set(b,'edgecolor','none');
b(1).FaceColor = 'k';
b(2).FaceColor = 'b';
b(3).FaceColor = 'c';
b(4).FaceColor = 'm';
h = legend('Ideal FP', 'DRL', 'Greedy','Random', 'Location', 'best');
set(h,'FontName','Times New Roman','Fontsize',8);
xlabel('x');
ylabel('y');
axis([-0.5,18.5,0,18])
grid on
set(gcf,'paperpositionmode','auto');
print('-depsc','ave_rates.eps');