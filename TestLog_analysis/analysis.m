

%% 输出功率数据LOG对比

% 输出功率低频测试数据

fig = figure(1)
plot(dBm)
hold on
grid on
plot(dBm1)
ylabel('输出功率/dBm','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('输出功率-低频-最大值','FontSize',14)

set(fig,'Position',[10 10 1000 400]); 
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','输出功率-低频-最大值.bmp'); % export the figure as a BMP image

leop_max_l = [dBm, dBm1]
leop_max_l_s = sortrows(leop_max_l, 1)
figure(34)
plot(leop_max_l_s(:,1))
hold on
grid on
plot(leop_max_l_s(:,2))


fig = figure(2)
plot(dBm2)
hold on
grid on
plot(dBm3)
ylabel('输出功率/dBm','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('输出功率-低频-最小值','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','输出功率-低频-最小值.bmp'); % export the figure as a BMP image

leop_min_l = [dBm2, dBm3]
leop_min_l_s = sortrows(leop_min_l, 1)
figure(35)
plot(leop_min_l_s(:,1))
hold on
grid on
plot(leop_min_l_s(:,2))

% 
fig = figure(3)
plot(dBm4)
hold on
grid on
plot(dBm5)
ylabel('输出功率/dBm','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('输出功率-低频-峰值','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','输出功率-低频-峰值.bmp'); % export the figure as a BMP image

leop_peak_l = [dBm4, dBm5]
leop_peak_l_s = sortrows(leop_peak_l, 1)
figure(36)
plot(leop_peak_l_s(:,1))
hold on
grid on
plot(leop_peak_l_s(:,2))

fig = figure(10)
plot(dBm6)
hold on
grid on
plot(dBm7)
grid on
ylabel('输出功率/dBm','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('输出功率-低频-平均值','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','输出功率-低频-平均值.bmp'); % export the figure as a BMP image

leop_avg_l = [dBm6, dBm7]
leop_avg_l_s = sortrows(leop_avg_l, 1)
figure(37)
plot(leop_avg_l_s(:,1))
hold on
grid on
plot(leop_avg_l_s(:,2))



% 输出功率中频测试数据

fig = figure(4)
plot(dBm8)
hold on
grid on
plot(dBm9)
ylabel('输出功率/dBm','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('输出功率-中频-最大值','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','输出功率-中频-最大值.bmp'); % export the figure as a BMP image


fig = figure(5)
plot(dBm10)
hold on
grid on
plot(dBm11)
ylabel('输出功率/dBm','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('输出功率-中频-最小值','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','输出功率-中频-最小值.bmp'); % export the figure as a BMP image

fig = figure(6)
plot(dBm12)
hold on
grid on
plot(dBm13)
ylabel('输出功率/dBm','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('输出功率-中频-峰值','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','输出功率-中频-峰值.bmp'); % export the figure as a BMP image

fig = figure(11)
plot(dBm14)
hold on
grid on
plot(dBm15)
ylabel('输出功率/dBm','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('输出功率-中频-平均值','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','输出功率-中频-平均值.bmp'); % export the figure as a BMP image


% 输出功率高频测试数据

fig = figure(7)
plot(dBm16)
hold on
grid on
plot(dBm17)
ylabel('输出功率/dBm','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('输出功率-高频-最大值','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','输出功率-高频-最大值.bmp'); % export the figure as a BMP image

fig = figure(8)
plot(dBm18)
hold on
grid on
plot(dBm19)
ylabel('输出功率/dBm','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')   
title('输出功率-高频-最小值','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','输出功率-高频-最小值.bmp'); % export the figure as a BMP image

fig = figure(9)
plot(dBm20)
hold on
grid on
plot(dBm21)
ylabel('输出功率/dBm','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('输出功率-高频-峰值','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','输出功率-高频-峰值.bmp'); % export the figure as a BMP image


fig = figure(12)
plot(dBm22)
hold on
grid on
plot(dBm23)
ylabel('输出功率/dBm','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('输出功率-高频-平均值','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','输出功率-高频-平均值.bmp'); % export the figure as a BMP image

%% 频偏测试数据LOG对比

% 频偏低频测试数据

fig = figure(13)
plot(kHz)
hold on
grid on
plot(kHz1)
ylabel('频偏/kHz','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('频偏-低频- 平均频偏','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','频偏-低频-平均频偏.bmp'); % export the figure as a BMP image

lecid_ave_fn_l = [kHz, kHz1]
lecid_ave_fn_l_s = sortrows(lecid_ave_fn_l,1)
figure(38)
plot(lecid_ave_fn_l_s(:,1))
hold on
grid on
plot(lecid_ave_fn_l_s(:,2))




fig = figure(14)
plot(vekHz)
hold on
grid on
plot(vekHz1)
ylabel('频偏/kHz','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('频偏-低频- +ve最大值','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','频偏-低频-+ve最大值.bmp'); % export the figure as a BMP image

fig = figure(15)
plot(vekHz2)
hold on
grid on
plot(vekHz3)
ylabel('频偏/kHz','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('频偏-低频- -ve最大值','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','漂移速率-低频.bmp'); % export the figure as a BMP image

fig = figure(16)
plot(kHz2)
hold on
grid on
plot(kHz3)
ylabel('漂移速率/ kHz/50us','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('漂移速率-低频','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','漂移速率-低频.bmp'); % export the figure as a BMP image

fig = figure(17)
plot(kHz4)
hold on
grid on
plot(kHz5)
ylabel('最大漂移/ kHz','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('最大漂移-低频','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','最大漂移-低频.bmp'); % export the figure as a BMP image

fig = figure(18)
plot(kHz6)
hold on
grid on
plot(kHz7)
ylabel('平均漂移/ kHz','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('平均漂移-低频','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','平均漂移-低频.bmp'); % export the figure as a BMP image

% 频偏中频测试数据

fig = figure(19)
plot(kHz8)
hold on
grid on
plot(kHz9)
ylabel('频偏/kHz','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('频偏-中频- 平均频偏','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','频偏-中频-平均频偏.bmp'); % export the figure as a BMP image

fig = figure(20)
plot(vekHz4)
hold on
grid on
plot(vekHz5)
ylabel('频偏/kHz','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('频偏-中频- +ve最大值','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','频偏-中频-+ve最大值.bmp'); % export the figure as a BMP image

fig = figure(21)
plot(vekHz6)
hold on
grid on
plot(vekHz7)
ylabel('频偏/kHz','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('频偏-中频- -ve最大值','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','频偏-中频- -ve最大值.bmp'); % export the figure as a BMP image

fig = figure(22)
plot(kHz10)
hold on
grid on
plot(kHz11)
ylabel('漂移速率/ kHz/50us','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('漂移速率-中频','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','漂移速率-中频.bmp'); % export the figure as a BMP image

fig = figure(23)
plot(kHz12)
hold on
grid on
plot(kHz13)
ylabel('最大漂移/ kHz','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('最大漂移-中频','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','最大漂移-中频.bmp'); % export the figure as a BMP image

fig = figure(24)
plot(kHz14)
hold on
grid on
plot(kHz15)
ylabel('平均漂移/ kHz','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('平均漂移-中频','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','平均漂移-中频.bmp'); % export the figure as a BMP image

% 频偏高频测试数据

fig = figure(25)
plot(kHz16)
hold on
grid on
plot(kHz17)
ylabel('频偏/kHz','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('频偏-高频- 平均频偏','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','频偏-高频-平均频偏.bmp'); % export the figure as a BMP image

fig = figure(26)
plot(vekHz8)
hold on
grid on
plot(vekHz9)
ylabel('频偏/kHz','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('频偏-高频- +ve最大值','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','频偏-高频-+ve最大值.bmp'); % export the figure as a BMP image

fig = figure(27)
plot(vekHz10)
hold on
grid on
plot(vekHz11)
ylabel('频偏/kHz','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('频偏-高频- -ve最大值','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','频偏-高频- -ve最大值.bmp'); % export the figure as a BMP image

fig = figure(28)
plot(kHz18)
hold on
grid on
plot(kHz19)
ylabel('漂移速率/ kHz/50us','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('漂移速率-高频','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','漂移速率-高频.bmp'); % export the figure as a BMP image

fig = figure(29)
plot(kHz20)
hold on
grid on
plot(kHz21)
ylabel('最大漂移/ kHz','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('最大漂移-高频','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','最大漂移-高频.bmp'); % export the figure as a BMP image

fig = figure(30)
plot(kHz22)
hold on
grid on
plot(kHz23)
ylabel('平均漂移/ kHz','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('平均漂移-高频','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','平均漂移-高频.bmp'); % export the figure as a BMP image

%% 误码率测试数据

fig = figure(31)
plot(VarName65)
hold on
grid on
plot(VarName66)
ylabel('误码率 / %','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('误码率-低频','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','误码率-低频.bmp'); % export the figure as a BMP image

fig = figure(32)
plot(VarName67)
hold on
grid on
plot(VarName68)
ylabel('误码率 / %','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('误码率-中频','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','误码率-中频.bmp'); % export the figure as a BMP image

fig = figure(39)
less_m = [VarName67, VarName68]
less_m_s = sortrows(less_m,1)
plot(less_m_s(:,1))
hold on
grid on
plot(less_m_s(:,2))


fig = figure(33)
plot(VarName69)
hold on
grid on
plot(VarName70)
ylabel('误码率 / %','FontSize',12)
xlabel('测试序列','FontSize',12)
legend('原测试平台','新测试平台')
title('误码率-高频','FontSize',14)

set(fig,'Position',[10 10 1000 400]);
set(fig,'PaperPositionMode','auto')

print(fig,'-dbmp','-r300','误码率-高频.bmp'); % export the figure as a BMP image











