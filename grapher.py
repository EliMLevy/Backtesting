# importing the required module
import matplotlib.pyplot as plt
import math
import numpy as np
import datetime

# x = ['2020-01-06', '2020-01-08', '2020-01-10', '2020-01-13', '2020-01-15', '2020-01-17', '2020-01-21', '2020-01-24', '2020-01-27', '2020-01-29', '2020-01-31', '2020-02-03', '2020-02-05', '2020-02-07', '2020-02-10', '2020-02-12', '2020-02-14', '2020-02-18', '2020-02-21', '2020-02-24', '2020-02-26', '2020-02-28', '2020-03-02', '2020-03-04', '2020-03-06', '2020-03-09', '2020-03-11', '2020-03-13', '2020-03-16', '2020-03-18', '2020-03-20', '2020-03-23', '2020-03-25', '2020-03-27', '2020-03-30', '2020-04-01', '2020-04-03', '2020-04-06', '2020-04-08', '2020-04-13', '2020-04-15', '2020-04-17', '2020-04-20', '2020-04-22', '2020-04-24', '2020-04-27', '2020-04-29', '2020-05-01', '2020-05-04', '2020-05-06', '2020-05-08', '2020-05-11', '2020-05-13', '2020-05-15', '2020-05-18', '2020-05-20', '2020-05-22', '2020-05-26', '2020-05-29', '2020-06-01', '2020-06-03', '2020-06-05', '2020-06-08', '2020-06-10', '2020-06-12', '2020-06-15', '2020-06-17', '2020-06-19', '2020-06-22', '2020-06-24', '2020-06-26', '2020-06-29', '2020-07-01', '2020-07-06', '2020-07-08', '2020-07-10', '2020-07-13', '2020-07-15', '2020-07-17', '2020-07-20', '2020-07-22', '2020-07-24', '2020-07-27', '2020-07-29', '2020-07-31', '2020-08-03', '2020-08-05', '2020-08-07', '2020-08-10', '2020-08-12', '2020-08-14', '2020-08-17', '2020-08-19', '2020-08-21', '2020-08-24', '2020-08-26', '2020-08-28', '2020-08-31', '2020-09-02', '2020-09-04', '2020-09-08', '2020-09-11', '2020-09-14', '2020-09-16', '2020-09-18', '2020-09-21', '2020-09-23', '2020-09-25', '2020-09-28', '2020-09-30', '2020-10-02', '2020-10-05', '2020-10-07', '2020-10-09', '2020-10-12', '2020-10-14', '2020-10-16', '2020-10-19', '2020-10-21', '2020-10-23', '2020-10-26', '2020-10-28', '2020-10-30', '2020-11-02', '2020-11-04', '2020-11-06', '2020-11-09', '2020-11-11', '2020-11-13', '2020-11-16', '2020-11-18', '2020-11-20', '2020-11-23', '2020-11-25', '2020-11-27', '2020-11-30', '2020-12-02', '2020-12-04', '2020-12-07', '2020-12-09', '2020-12-11', '2020-12-14', '2020-12-16', '2020-12-18', '2020-12-21', '2020-12-23', '2020-12-28', '2020-12-30']
# y = [0.015000000000000013, 0.9450000000000001, 1.675, 2.295, 3.02, 3.94, 4.295, 2.3499999999999996, -0.3600000000000003, 1.6349999999999996, -2.125, -0.31499999999999995, 1.495, 2.455, 3.345, 4.525, 5.265000000000001, 5.950000000000001, 3.9750000000000014, -3.8149999999999995, -11.5, -32.5, -26.175, -22.005, -34.19499999999999, -46.209999999999994, -43.55, -50.974999999999994, -57.25999999999999, -59.89999999999999, -53.974999999999994, -57.3, -50.169999999999995, -43.864999999999995, -38.60999999999999, -50.364999999999995, -45.404999999999994, -41.669999999999995, -38.199999999999996, -33.574999999999996, -30.159999999999997, -27.054999999999996, -27.099999999999994, -25.424999999999994, -22.339999999999993, -20.199999999999992, -17.859999999999992, -27.039999999999992, -24.68999999999999, -22.30999999999999, -19.65499999999999, -18.234999999999992, -28.819999999999993, -25.914999999999992, -24.02999999999999, -22.04999999999999, -21.97999999999999, -20.24999999999999, -17.91499999999999, -16.29999999999999, -14.37499999999999, -12.65999999999999, -11.00999999999999, -10.564999999999989, -25.71499999999999, -22.31499999999999, -19.20999999999999, -16.51499999999999, -14.27999999999999, -16.33999999999999, -17.36999999999999, -14.92499999999999, -12.63999999999999, -10.164999999999988, -8.979999999999988, -7.0449999999999875, -6.359999999999987, -3.989999999999987, -1.7849999999999873, -0.26999999999998714, 1.300000000000013, -2.574999999999987, -1.1099999999999868, 0.6350000000000133, 2.055000000000013, 3.270000000000013, 4.920000000000013, 6.280000000000014, 7.480000000000014, 8.900000000000015, 9.310000000000015, 10.480000000000015, 11.400000000000015, 12.520000000000014, 13.510000000000014, 14.680000000000014, 16.650000000000013, 17.470000000000013, 18.835000000000015, 5.995000000000015, 0.5800000000000161, 4.095000000000017, 6.120000000000017, 8.235000000000017, 3.1450000000000173, -0.489999999999982, 0.6900000000000182, 3.130000000000018, 4.795000000000018, 6.585000000000018, 8.940000000000019, 10.78500000000002, 12.82500000000002, 15.015000000000022, 16.35500000000002, 14.810000000000022, 16.455000000000023, 12.180000000000023, 14.530000000000022, 16.82000000000002, 11.70000000000002, 4.56000000000002, 4.63500000000002, 7.5400000000000205, 12.680000000000021, 15.910000000000021, 17.71500000000002, 18.545000000000023, 20.580000000000023, 22.110000000000024, 20.620000000000026, 21.570000000000025, 22.960000000000026, 24.510000000000026, 25.405000000000026, 24.940000000000026, 26.740000000000027, 28.230000000000025, 28.480000000000025, 28.980000000000025, 29.830000000000027, 30.155000000000026, 32.17000000000002, 32.83500000000002, 33.715000000000025, 36.00000000000003, 37.605000000000025, 38.61500000000002]

x = ['2015-01-09', '2015-01-16', '2015-01-23', '2015-01-30', '2015-02-06', '2015-02-13', '2015-02-20', '2015-02-27', '2015-03-06', '2015-03-13', '2015-03-20', '2015-03-27', '2015-03-31', '2015-04-02', '2015-04-10', '2015-04-17', '2015-04-24', '2015-05-01', '2015-05-08', '2015-05-15', '2015-05-22', '2015-05-29', '2015-06-05', '2015-06-12', '2015-06-19', '2015-06-26', '2015-06-30', '2015-07-02', '2015-07-10', '2015-07-17', '2015-07-24', '2015-07-31', '2015-08-07', '2015-08-14', '2015-08-21', '2015-08-28', '2015-09-04', '2015-09-11', '2015-09-18', '2015-09-25', '2015-09-30', '2015-10-02', '2015-10-09', '2015-10-16', '2015-10-23', '2015-10-30', '2015-11-06', '2015-11-13', '2015-11-20', '2015-11-27', '2015-12-04', '2015-12-11', '2015-12-18', '2015-12-24', '2015-12-31', '2016-01-08', '2016-01-15', '2016-01-22', '2016-01-29', '2016-02-05', '2016-02-12', '2016-02-19', '2016-02-26', '2016-03-04', '2016-03-11', '2016-03-18', '2016-03-24', '2016-03-31', '2016-04-08', '2016-04-15', '2016-04-22', '2016-04-29', '2016-05-06', '2016-05-13', '2016-05-20', '2016-05-27', '2016-06-03', '2016-06-10', '2016-06-17', '2016-06-24', '2016-06-30', '2016-07-08', '2016-07-15', '2016-07-22', '2016-07-29', '2016-08-05', '2016-08-12', '2016-08-19', '2016-08-26', '2016-09-02', '2016-09-07', '2016-09-09', '2016-09-14', '2016-09-16', '2016-09-21', '2016-09-23', '2016-09-28', '2016-09-30', '2016-10-05', '2016-10-07', '2016-10-12', '2016-10-14', '2016-10-19', '2016-10-21', '2016-10-26', '2016-10-28', '2016-11-02', '2016-11-04', '2016-11-09', '2016-11-11', '2016-11-16', '2016-11-18', '2016-11-23', '2016-11-25', '2016-11-30', '2016-12-02', '2016-12-07', '2016-12-09', '2016-12-14', '2016-12-16', '2016-12-21', '2016-12-23', '2016-12-28', '2016-12-30', '2017-01-04', '2017-01-06', '2017-01-11', '2017-01-13', '2017-01-18', '2017-01-20', '2017-01-25', '2017-01-27', '2017-02-01', '2017-02-03', '2017-02-08', '2017-02-10', '2017-02-15', '2017-02-17', '2017-02-22', '2017-02-24', '2017-03-01', '2017-03-03', '2017-03-08', '2017-03-10', '2017-03-15', '2017-03-17', '2017-03-22', '2017-03-24', '2017-03-29', '2017-03-31', '2017-04-05', '2017-04-07', '2017-04-12', '2017-04-19', '2017-04-21', '2017-04-26', '2017-04-28', '2017-05-03', '2017-05-05', '2017-05-10', '2017-05-12', '2017-05-17', '2017-05-19', '2017-05-24', '2017-05-26', '2017-05-31', '2017-06-02', '2017-06-07', '2017-06-09', '2017-06-14', '2017-06-16', '2017-06-21', '2017-06-23', '2017-06-28', '2017-06-30', '2017-07-05', '2017-07-07', '2017-07-12', '2017-07-14', '2017-07-19', '2017-07-21', '2017-07-26', '2017-07-28', '2017-08-02', '2017-08-04', '2017-08-09', '2017-08-11', '2017-08-16', '2017-08-18', '2017-08-23', '2017-08-25', '2017-08-30', '2017-09-01', '2017-09-06', '2017-09-08', '2017-09-13', '2017-09-15', '2017-09-20', '2017-09-22', '2017-09-27', '2017-09-29', '2017-10-04', '2017-10-06', '2017-10-11', '2017-10-13', '2017-10-18', '2017-10-20', '2017-10-25', '2017-10-27', '2017-11-01', '2017-11-03', '2017-11-08', '2017-11-10', '2017-11-15', '2017-11-17', '2017-11-22', '2017-11-24', '2017-11-29', '2017-12-01', '2017-12-06', '2017-12-08', '2017-12-13', '2017-12-15', '2017-12-20', '2017-12-22', '2017-12-27', '2017-12-29', '2018-01-03', '2018-01-05', '2018-01-10', '2018-01-12', '2018-01-17', '2018-01-19', '2018-01-24', '2018-01-26', '2018-01-31', '2018-02-02', '2018-02-07', '2018-02-09', '2018-02-14', '2018-02-16', '2018-02-21', '2018-02-23', '2018-02-26', '2018-02-28', '2018-03-02', '2018-03-05', '2018-03-07', '2018-03-09', '2018-03-12', '2018-03-14', '2018-03-16', '2018-03-19', '2018-03-21', '2018-03-23', '2018-03-26', '2018-03-28', '2018-04-02', '2018-04-04', '2018-04-06', '2018-04-09', '2018-04-11', '2018-04-13', '2018-04-16', '2018-04-18', '2018-04-20', '2018-04-23', '2018-04-25', '2018-04-27', '2018-04-30', '2018-05-02', '2018-05-04', '2018-05-07', '2018-05-09', '2018-05-11', '2018-05-14', '2018-05-16', '2018-05-18', '2018-05-21', '2018-05-23', '2018-05-25', '2018-05-29', '2018-06-01', '2018-06-04', '2018-06-06', '2018-06-08', '2018-06-11', '2018-06-13', '2018-06-15', '2018-06-18', '2018-06-20', '2018-06-22', '2018-06-25', '2018-06-27', '2018-06-29', '2018-07-02', '2018-07-06', '2018-07-09', '2018-07-11', '2018-07-13', '2018-07-16', '2018-07-18', '2018-07-20', '2018-07-23', '2018-07-25', '2018-07-27', '2018-07-30', '2018-08-01', '2018-08-03', '2018-08-06', '2018-08-08', '2018-08-10', '2018-08-13', '2018-08-15', '2018-08-17', '2018-08-20', '2018-08-22', '2018-08-24', '2018-08-27', '2018-08-29', '2018-08-31', '2018-09-04', '2018-09-07', '2018-09-10', '2018-09-12', '2018-09-14', '2018-09-17', '2018-09-19', '2018-09-21', '2018-09-24', '2018-09-26', '2018-09-28', '2018-10-01', '2018-10-03', '2018-10-05', '2018-10-08', '2018-10-10', '2018-10-12', '2018-10-15', '2018-10-17', '2018-10-19', '2018-10-22', '2018-10-24', '2018-10-26', '2018-10-29', '2018-10-31', '2018-11-02', '2018-11-05', '2018-11-07', '2018-11-09', '2018-11-12', '2018-11-14', '2018-11-16', '2018-11-19', '2018-11-21', '2018-11-23', '2018-11-26', '2018-11-28', '2018-11-30', '2018-12-03', '2018-12-04', '2018-12-07', '2018-12-10', '2018-12-12', '2018-12-14', '2018-12-17', '2018-12-19', '2018-12-21', '2018-12-24', '2018-12-26', '2018-12-28', '2018-12-31', '2019-01-02', '2019-01-04', '2019-01-07', '2019-01-09', '2019-01-11', '2019-01-14', '2019-01-16', '2019-01-18', '2019-01-22', '2019-01-25', '2019-01-28', '2019-01-30', '2019-02-01', '2019-02-04', '2019-02-06', '2019-02-08', '2019-02-11', '2019-02-13', '2019-02-15', '2019-02-19', '2019-02-22', '2019-02-25', '2019-02-27', '2019-03-01', '2019-03-04', '2019-03-06', '2019-03-08', '2019-03-11', '2019-03-13', '2019-03-15', '2019-03-18', '2019-03-20', '2019-03-22', '2019-03-25', '2019-03-27', '2019-03-29', '2019-04-01', '2019-04-03', '2019-04-05', '2019-04-08', '2019-04-10', '2019-04-12', '2019-04-15', '2019-04-17', '2019-04-22', '2019-04-24', '2019-04-26', '2019-04-29', '2019-05-01', '2019-05-03', '2019-05-06', '2019-05-08', '2019-05-10', '2019-05-13', '2019-05-15', '2019-05-17', '2019-05-20', '2019-05-22', '2019-05-24', '2019-05-28', '2019-05-31', '2019-06-03', '2019-06-05', '2019-06-07', '2019-06-10', '2019-06-12', '2019-06-14', '2019-06-17', '2019-06-19', '2019-06-21', '2019-06-24', '2019-06-26', '2019-06-28', '2019-07-01', '2019-07-03', '2019-07-05', '2019-07-08', '2019-07-10', '2019-07-12', '2019-07-15', '2019-07-17', '2019-07-19', '2019-07-22', '2019-07-24', '2019-07-26', '2019-07-29', '2019-07-31', '2019-08-02', '2019-08-05', '2019-08-07', '2019-08-09', '2019-08-12', '2019-08-14', '2019-08-16', '2019-08-19', '2019-08-21', '2019-08-23', '2019-08-26', '2019-08-28', '2019-08-30', '2019-09-03', '2019-09-06', '2019-09-09', '2019-09-11', '2019-09-13', '2019-09-16', '2019-09-18', '2019-09-20', '2019-09-23', '2019-09-25', '2019-09-27', '2019-09-30', '2019-10-02', '2019-10-04', '2019-10-07', '2019-10-09', '2019-10-11', '2019-10-14', '2019-10-16', '2019-10-18', '2019-10-21', '2019-10-23', '2019-10-25', '2019-10-28', '2019-10-30', '2019-11-01', '2019-11-04', '2019-11-06', '2019-11-08', '2019-11-11', '2019-11-13', '2019-11-15', '2019-11-18', '2019-11-20', '2019-11-22', '2019-11-25', '2019-11-27', '2019-11-29', '2019-12-02', '2019-12-04', '2019-12-06', '2019-12-09', '2019-12-11', '2019-12-13', '2019-12-16', '2019-12-18', '2019-12-20', '2019-12-23', '2019-12-27', '2019-12-30', '2020-01-03', '2020-01-06', '2020-01-08', '2020-01-10', '2020-01-13', '2020-01-15', '2020-01-17', '2020-01-21', '2020-01-24', '2020-01-27', '2020-01-29', '2020-01-31', '2020-02-03', '2020-02-05', '2020-02-07', '2020-02-10', '2020-02-12', '2020-02-14', '2020-02-18', '2020-02-21', '2020-02-24', '2020-02-26', '2020-02-28', '2020-03-02', '2020-03-04', '2020-03-06', '2020-03-09', '2020-03-11', '2020-03-13', '2020-03-16', '2020-03-18', '2020-03-20', '2020-03-23', '2020-03-25', '2020-03-27', '2020-03-30', '2020-04-01', '2020-04-03', '2020-04-06', '2020-04-08', '2020-04-13', '2020-04-15', '2020-04-17', '2020-04-20', '2020-04-22', '2020-04-24', '2020-04-27', '2020-04-29', '2020-05-01', '2020-05-04', '2020-05-06', '2020-05-08', '2020-05-11', '2020-05-13', '2020-05-15', '2020-05-18', '2020-05-20', '2020-05-22', '2020-05-26', '2020-05-29', '2020-06-01', '2020-06-03', '2020-06-05', '2020-06-08', '2020-06-10', '2020-06-12', '2020-06-15', '2020-06-17', '2020-06-19', '2020-06-22', '2020-06-24', '2020-06-26', '2020-06-29', '2020-07-01', '2020-07-06', '2020-07-08', '2020-07-10', '2020-07-13', '2020-07-15', '2020-07-17', '2020-07-20', '2020-07-22', '2020-07-24', '2020-07-27', '2020-07-29', '2020-07-31', '2020-08-03', '2020-08-05', '2020-08-07', '2020-08-10', '2020-08-12', '2020-08-14', '2020-08-17', '2020-08-19', '2020-08-21', '2020-08-24', '2020-08-26', '2020-08-28', '2020-08-31', '2020-09-02', '2020-09-04', '2020-09-08', '2020-09-11', '2020-09-14', '2020-09-16', '2020-09-18', '2020-09-21', '2020-09-23', '2020-09-25', '2020-09-28', '2020-09-30', '2020-10-02', '2020-10-05', '2020-10-07', '2020-10-09', '2020-10-12', '2020-10-14', '2020-10-16', '2020-10-19', '2020-10-21', '2020-10-23', '2020-10-26', '2020-10-28', '2020-10-30', '2020-11-02', '2020-11-04', '2020-11-06', '2020-11-09', '2020-11-11', '2020-11-13', '2020-11-16', '2020-11-18', '2020-11-20', '2020-11-23', '2020-11-25', '2020-11-27', '2020-11-30', '2020-12-02', '2020-12-04', '2020-12-07', '2020-12-09', '2020-12-11', '2020-12-14', '2020-12-16', '2020-12-18', '2020-12-21', '2020-12-23', '2020-12-28', '2020-12-30']
x = [datetime.datetime.strptime(n, '%Y-%m-%d') for n in x]
y = [0.7650000000000001, -0.8199999999999998, 1.5100000000000002, -2.21, 0.05500000000000016, 1.8300000000000003, 3.0, 3.7800000000000002, 1.5350000000000006, 1.6500000000000008, 3.545000000000001, -0.10999999999999988, 0.5300000000000001, 1.2850000000000001, 2.825, 1.9050000000000002, 3.3000000000000003, 3.3600000000000003, 4.4750000000000005, 5.555000000000001, 6.525, 5.91, 5.48, 6.905, 8.67, 9.33, 7.43, 8.635, 10.765, 12.63, 9.18, 10.525, 9.23, 10.58, 1.2799999999999994, 4.039999999999999, 1.7849999999999993, 4.3149999999999995, 6.574999999999999, 6.93, 7.21, 8.795, 10.74, 11.940000000000001, 13.180000000000001, 14.345000000000002, 15.640000000000002, 10.080000000000002, 12.195000000000002, 13.225000000000001, 14.610000000000001, 8.160000000000002, 11.305000000000001, 13.055000000000001, 12.840000000000002, 2.580000000000002, 0.6700000000000017, 3.5450000000000017, 5.855000000000002, 2.3700000000000028, 3.6350000000000025, 5.730000000000002, 7.485000000000002, 9.235000000000003, 10.860000000000003, 12.640000000000004, 12.340000000000003, 13.505000000000003, 13.330000000000002, 14.720000000000002, 15.835000000000003, 14.880000000000003, 15.605000000000002, 16.720000000000002, 18.065, 19.32, 20.245, 20.51, 19.650000000000002, 19.035000000000004, 21.620000000000005, 23.025000000000006, 23.985000000000007, 24.800000000000008, 25.63000000000001, 26.59000000000001, 27.280000000000012, 28.005000000000013, 27.590000000000014, 28.825000000000014, 29.295000000000012, 25.05000000000001, 25.92500000000001, 27.12000000000001, 28.50000000000001, 29.19500000000001, 30.09500000000001, 30.675000000000008, 30.370000000000008, 30.370000000000008, 30.07500000000001, 30.68500000000001, 31.77000000000001, 32.16000000000001, 32.85000000000001, 32.49000000000001, 31.47500000000001, 31.17000000000001, 33.93500000000001, 34.73000000000001, 35.79000000000001, 36.27500000000001, 36.84500000000001, 37.16500000000001, 37.46500000000001, 37.14500000000001, 38.16500000000001, 38.66500000000001, 39.39500000000001, 39.68000000000001, 40.49000000000001, 40.82000000000001, 40.165000000000006, 39.77, 40.665000000000006, 41.18500000000001, 41.25500000000001, 41.69500000000001, 41.85000000000001, 42.29500000000001, 42.83500000000001, 42.94500000000001, 42.84000000000001, 43.34000000000001, 43.78000000000001, 44.13000000000001, 44.81000000000001, 45.24000000000001, 45.72500000000001, 46.18500000000001, 46.81000000000001, 45.90000000000001, 44.920000000000016, 45.51000000000002, 46.43500000000002, 46.16000000000002, 43.88500000000002, 44.62500000000002, 45.86000000000002, 46.24000000000002, 45.89000000000002, 46.67000000000002, 46.480000000000025, 46.840000000000025, 47.520000000000024, 49.00000000000002, 49.07000000000002, 49.71000000000002, 50.22000000000002, 51.04000000000002, 50.92500000000002, 48.795000000000016, 49.85500000000002, 50.765000000000015, 51.155000000000015, 51.475000000000016, 51.875000000000014, 52.225000000000016, 52.21500000000002, 52.94000000000002, 53.06500000000002, 53.545000000000016, 53.985000000000014, 54.63500000000001, 54.48000000000001, 54.98000000000001, 55.12000000000001, 55.76000000000001, 56.23000000000001, 56.570000000000014, 56.87000000000001, 57.39500000000001, 57.59500000000001, 58.055000000000014, 58.42500000000001, 58.84500000000001, 56.64500000000001, 58.00500000000001, 55.15000000000001, 56.295000000000016, 56.70500000000001, 57.35500000000001, 57.87000000000001, 57.47000000000001, 57.570000000000014, 58.545000000000016, 59.125000000000014, 59.66500000000001, 60.085000000000015, 60.53500000000002, 60.93500000000002, 61.515000000000015, 61.93500000000002, 62.41500000000001, 62.67500000000001, 62.96500000000001, 63.16500000000001, 62.68500000000002, 63.320000000000014, 63.975000000000016, 64.56500000000001, 65.04500000000002, 64.52000000000001, 63.96500000000001, 64.76500000000001, 65.28000000000002, 65.47000000000001, 65.96000000000001, 66.60000000000001, 66.49000000000001, 67.01500000000001, 67.73500000000001, 68.45500000000001, 69.15, 69.56, 69.845, 70.215, 70.785, 71.30499999999999, 71.955, 72.52499999999999, 73.21499999999999, 73.91499999999999, 74.87499999999999, 75.68499999999999, 72.97999999999999, 68.07499999999999, 64.17999999999999, 56.87499999999999, 60.24999999999999, 61.669999999999995, 61.48499999999999, 62.879999999999995, 63.644999999999996, 60.485, 57.94, 59.15, 60.29, 61.63, 62.34, 59.190000000000005, 60.605000000000004, 56.31, 57.760000000000005, 46.96000000000001, 49.17000000000001, 46.220000000000006, 44.85000000000001, 46.94000000000001, 45.46500000000001, 46.985000000000014, 48.87000000000001, 50.47000000000001, 51.49500000000001, 52.31000000000001, 49.00000000000001, 49.925000000000004, 48.040000000000006, 49.71000000000001, 49.42000000000001, 48.845000000000006, 50.02, 50.730000000000004, 51.690000000000005, 52.64000000000001, 53.26500000000001, 53.705000000000005, 54.080000000000005, 54.54500000000001, 55.165000000000006, 55.205000000000005, 53.23500000000001, 54.84, 55.34, 56.115, 56.815000000000005, 57.435, 57.805, 58.34, 58.32, 58.915, 58.86, 55.75, 56.415, 57.735, 58.089999999999996, 59.349999999999994, 60.05, 60.205, 61.05, 61.379999999999995, 62.01499999999999, 61.574999999999996, 62.019999999999996, 62.635, 61.184999999999995, 60.55499999999999, 61.43999999999999, 62.21499999999999, 62.72499999999999, 63.29999999999999, 61.64999999999999, 61.85999999999999, 62.42499999999999, 63.38499999999999, 63.88999999999999, 64.42999999999999, 65.02, 65.565, 66.195, 65.54499999999999, 65.725, 64.695, 65.30499999999999, 66.035, 66.75999999999999, 65.82499999999999, 66.77499999999999, 67.63499999999999, 67.285, 67.425, 68.11999999999999, 68.65499999999999, 69.34999999999998, 66.39999999999998, 67.25499999999998, 59.81499999999998, 59.139999999999986, 60.19999999999999, 61.71999999999999, 60.61999999999999, 60.75499999999999, 54.139999999999986, 53.914999999999985, 53.06499999999998, 56.03499999999998, 57.70999999999998, 59.01499999999998, 61.16499999999998, 61.09999999999998, 56.83499999999998, 56.32499999999998, 58.234999999999985, 53.97499999999999, 52.02999999999999, 52.14499999999999, 53.41999999999999, 54.789999999999985, 56.164999999999985, 58.139999999999986, 50.539999999999985, 47.444999999999986, 49.359999999999985, 51.40999999999998, 46.83999999999998, 42.79499999999998, 42.29499999999998, 35.86499999999998, 33.62999999999998, 36.15499999999998, 38.48999999999998, 40.80999999999998, 42.079999999999984, 43.734999999999985, 45.09999999999999, 46.60499999999999, 48.02499999999999, 48.09499999999999, 49.224999999999994, 50.27499999999999, 47.07499999999999, 48.83499999999999, 47.46499999999999, 48.79999999999999, 50.24999999999999, 50.709999999999994, 51.489999999999995, 49.56999999999999, 50.434999999999995, 51.419999999999995, 52.269999999999996, 53.04, 54.015, 54.575, 54.940000000000005, 55.83500000000001, 55.05500000000001, 54.690000000000005, 52.165000000000006, 52.94500000000001, 53.75500000000001, 54.76000000000001, 55.235000000000014, 55.695000000000014, 54.60500000000001, 55.41000000000001, 56.72500000000001, 57.99500000000001, 58.67500000000001, 59.305000000000014, 60.30000000000001, 60.90500000000001, 61.24500000000001, 61.92500000000001, 62.26000000000001, 62.84500000000001, 63.60500000000001, 64.30000000000001, 65.025, 65.61500000000001, 65.34, 66.265, 65.825, 63.195, 64.1, 59.019999999999996, 61.26499999999999, 62.48499999999999, 61.73499999999999, 63.279999999999994, 61.36999999999999, 60.38499999999999, 57.474999999999994, 57.26499999999999, 58.864999999999995, 60.035, 60.76, 60.949999999999996, 62.025, 62.589999999999996, 63.785, 65.00999999999999, 64.99, 63.14999999999999, 63.96999999999999, 65.75999999999999, 66.49, 66.955, 66.545, 67.295, 68.12, 68.5, 67.2, 67.86, 68.265, 69.015, 69.765, 69.955, 68.41499999999999, 64.975, 57.83, 60.51, 62.41, 59.38999999999999, 57.68999999999999, 60.13999999999999, 61.285, 62.224999999999994, 56.45499999999999, 58.474999999999994, 60.309999999999995, 62.084999999999994, 62.199999999999996, 64.1, 64.6, 65.50999999999999, 66.44999999999999, 66.15999999999998, 67.42999999999998, 67.47999999999998, 68.22999999999998, 68.61999999999998, 67.09999999999998, 68.02999999999999, 60.524999999999984, 62.24499999999998, 62.649999999999984, 62.094999999999985, 63.90499999999999, 63.859999999999985, 64.99499999999999, 65.895, 66.735, 67.135, 68.095, 68.615, 69.57, 70.58, 70.89999999999999, 71.46999999999998, 72.06999999999998, 72.23999999999998, 72.98999999999998, 73.75499999999998, 74.28499999999998, 74.09499999999998, 74.80499999999998, 75.28499999999998, 75.93499999999999, 75.52499999999999, 74.285, 74.97, 76.05, 75.84, 76.83500000000001, 77.87500000000001, 78.56500000000001, 79.165, 80.275, 80.775, 81.44500000000001, 80.63000000000001, 82.03000000000002, 82.75000000000001, 83.68000000000002, 84.41000000000003, 85.03000000000003, 85.75500000000002, 86.67500000000003, 87.03000000000003, 85.08500000000004, 82.37500000000004, 84.37000000000005, 80.61000000000004, 82.42000000000004, 84.23000000000005, 85.19000000000004, 86.08000000000004, 87.26000000000005, 88.00000000000004, 88.68500000000004, 86.71000000000005, 78.92000000000004, 71.23500000000004, 50.23500000000004, 56.560000000000045, 60.73000000000005, 48.54000000000005, 36.52500000000005, 39.185000000000045, 31.760000000000048, 25.475000000000048, 22.835000000000047, 28.760000000000048, 25.435000000000045, 32.56500000000005, 38.87000000000005, 44.12500000000005, 32.37000000000005, 37.33000000000005, 41.06500000000005, 44.535000000000046, 49.160000000000046, 52.575000000000045, 55.68000000000004, 55.63500000000004, 57.31000000000004, 60.39500000000004, 62.53500000000004, 64.87500000000004, 55.69500000000004, 58.045000000000044, 60.42500000000005, 63.08000000000005, 64.50000000000004, 53.91500000000004, 56.82000000000004, 58.70500000000004, 60.68500000000004, 60.75500000000004, 62.485000000000035, 64.82000000000004, 66.43500000000003, 68.36000000000003, 70.07500000000003, 71.72500000000004, 72.17000000000003, 57.02000000000003, 60.42000000000003, 63.52500000000003, 66.22000000000003, 68.45500000000003, 66.39500000000002, 65.36500000000002, 67.81000000000002, 70.09500000000001, 72.57000000000001, 73.75500000000001, 75.69000000000001, 76.37500000000001, 78.74500000000002, 80.95000000000002, 82.46500000000002, 84.03500000000001, 80.16000000000001, 81.62500000000001, 83.37000000000002, 84.79000000000002, 86.00500000000002, 87.65500000000003, 89.01500000000003, 90.21500000000003, 91.63500000000003, 92.04500000000003, 93.21500000000003, 94.13500000000003, 95.25500000000004, 96.24500000000003, 97.41500000000003, 99.38500000000003, 100.20500000000003, 101.57000000000002, 88.73000000000002, 83.31500000000003, 86.83000000000003, 88.85500000000003, 90.97000000000003, 85.88000000000002, 82.24500000000002, 83.42500000000003, 85.86500000000002, 87.53000000000003, 89.32000000000004, 91.67500000000004, 93.52000000000004, 95.56000000000004, 97.75000000000004, 99.09000000000005, 97.54500000000004, 99.19000000000004, 94.91500000000003, 97.26500000000003, 99.55500000000004, 94.43500000000003, 87.29500000000003, 87.37000000000003, 90.27500000000003, 95.41500000000003, 98.64500000000004, 100.45000000000005, 101.28000000000004, 103.31500000000004, 104.84500000000004, 103.35500000000005, 104.30500000000005, 105.69500000000005, 107.24500000000005, 108.14000000000004, 107.67500000000004, 109.47500000000004, 110.96500000000003, 111.21500000000003, 111.71500000000003, 112.56500000000003, 112.89000000000003, 114.90500000000003, 115.57000000000004, 116.45000000000003, 118.73500000000003, 120.34000000000003, 121.35000000000004]


plt.plot(x, y)
  
plt.xlabel('Time')
plt.ylabel('P/L')
# plt.xticks([0, 1, 2,3,4,5],['2015','2016','2017','2018','2019','2020'], rotation=20)
# plt.xticks(np.arange(0, 1000, step=50), rotation=45) 
# plt.margins(0.1)
# plt.autoscale()
# plt.xlim([0, len(x) - 1])
# plt.xticks([20], rotation=40)
plt.subplots_adjust(bottom=0.25)
plt.title('Selling short term puts ')

plt.savefig('sellingshorttermputs.png')
plt.clf()