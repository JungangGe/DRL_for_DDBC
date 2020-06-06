close all; clear;
set(0,'defaultfigurecolor','w');
%--------------------------Codebook Design--------------------------------%
M = 3; % number of antennas 
K = 4; % codebook size
N = 16; % number of phases
W = zeros(M, K);
for m = 1:M
    for k = 1:K
        W(m, k) = exp(2j*pi/N*fix(m*mod(k + K/2, K) / (K/N))) / sqrt(M);
    end
end
save('codebook.mat', 'W');
code_book = W;
%-----------------------------Beam Graph----------------------------------%
N = M; % number of attennas
M = K; % codebook size
phi = linspace(0, 2*pi, 1000);
for j = 0:M-1
    bv = code_book(:, j+1);
    rp = zeros(1, length(phi));
    for i = 1:length(phi)
        s = exp(1j*pi*cos(phi(i))*(0:N-1))/sqrt(N);
        rp(i) = abs(s*bv);
    end
%     figure
    polar(phi, rp)
    hold on
end


