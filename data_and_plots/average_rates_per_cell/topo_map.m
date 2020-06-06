function ave_rates = topo_map(temp)
ave_rates = zeros(1,19);
ave_rates(1+0) = temp(1+0);
ave_rates(1+1) = temp(1+3);
ave_rates(1+2) = temp(1+2);
ave_rates(1+3) = temp(1+1);
ave_rates(1+4) = temp(1+6);
ave_rates(1+5) = temp(1+5);
ave_rates(1+6) = temp(1+4);
ave_rates(1+7) = temp(1+9);
ave_rates(1+8) = temp(1+15);
ave_rates(1+9) = temp(1+8);
ave_rates(1+10) = temp(1+14);
ave_rates(1+11) = temp(1+7);
ave_rates(1+12) = temp(1+13);
ave_rates(1+13) = temp(1+12);
ave_rates(1+14) = temp(1+18);
ave_rates(1+15) = temp(1+11);
ave_rates(1+16) = temp(1+17);
ave_rates(1+17) = temp(1+10);
ave_rates(1+18) = temp(1+16);
end

