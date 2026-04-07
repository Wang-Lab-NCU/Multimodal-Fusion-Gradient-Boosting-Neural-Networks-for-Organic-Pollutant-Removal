# 审稿5
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import torch
from model import get_model, get_1dcnn_model
from data3 import get_data
file_path = "pfas_nalv - 副本.xlsx"  # 替换为你的 Excel 文件路径
sheet_name = 0  # 如果需要指定工作表名称或索引，可以修改
data = pd.read_excel(file_path, sheet_name=sheet_name)
features = ['MWCO(Da)', 'Pore size(nm)', 'water flux(LMH)', 'Temperature (˚C)', 'PFOS con (ppb)', 'pH',
                    'Pressure (MPa)', 'Divalent cations (mmol/L)',
                    'Monovalent cations (mmol/L)', 'Trivalent cations (mmol/L)',
            'type__ESNA1-K1', 'type__HYDRACORE', 'type__NE70',
            'type__NF270', 'type__PMIA', 'type__Poly NF']
target = "PFOS rejection (%)"
# # 筛选高去除率样本
# high_removal = data[data[target] > 95]
#
# # 绘制关键参数分布
# plt.figure(figsize=(12, 5))
#
# # 子图1：孔径分布
# plt.subplot(1, 2, 1)
# plt.scatter(data['Pore size(nm)'], data[target], alpha=0.5, label="All Data")
# plt.scatter(high_removal['Pore size(nm)'], high_removal[target], c='red', label=">95% Removal")
# plt.axvline(x=0.5, color='k', linestyle='--', label="0.5 nm Threshold")
# plt.xlabel("Pore Size (nm)")
# plt.ylabel("Removal Rate (%)")
# plt.legend()
#
# # 子图2：MWCO分布
# plt.subplot(1, 2, 2)
# plt.scatter(data['MWCO(Da)'], data[target], alpha=0.5, label="All Data")
# plt.scatter(high_removal['MWCO(Da)'], high_removal[target], c='red', label=">95% Removal")
# plt.axvline(x=200, color='k', linestyle='--', label="200 Da Threshold")
# plt.xlabel("MWCO (Da)")
# plt.ylabel("Removal Rate (%)")
# plt.legend()
#
# plt.tight_layout()
# plt.suptitle("Key Parameter Thresholds for High Removal Efficiency", y=1.02)
# plt.show()


# # 组合参数分析（孔径 vs 压力）
# plt.figure(figsize=(10, 6))
# plt.scatter(data['Pore size(nm)'], data['Pressure (MPa)'],
#            c=data[target], cmap='RdYlGn', s=100,
#            edgecolors='k', alpha=0.7)
# plt.colorbar(label='rejection (%)')
#
# # 标注高效区域
# plt.axvline(0.5, color='blue', linestyle='--')
# plt.axhline(0.8, color='blue', linestyle='--')
# plt.text(0.52, 0.85, 'high operation', color='blue', fontsize=12)
#
# plt.xlabel("Pore size (nm)", fontsize=12)
# plt.ylabel("pressure (MPa)", fontsize=12)
# plt.title("Pore size and pressure", fontsize=14)
# plt.grid(True, alpha=0.3)
# plt.show()


# # 分析高温条件下的压力优化 (Analyze pressure optimization under high temperature conditions)
# high_temp = data
# high_temp_high_removal = high_temp[high_temp[target] > 95]
#
# # 创建双轴分析图 (Create dual-axis analysis plot)
# fig, ax = plt.subplots(figsize=(10, 6))
#
# # 散点图：压力与去除率关系 (Scatter plot: Pressure vs Removal Rate)
# sc = ax.scatter(high_temp['Pressure (MPa)'], high_temp[target],
#                c=high_temp['water flux(LMH)'], cmap='viridis',
#                s=80, alpha=0.7, label='Normal Samples')
# sc_high = ax.scatter(high_temp_high_removal['Pressure (MPa)'],
#                     high_temp_high_removal[target],
#                     c='red', edgecolors='k', s=100,
#                     label='High-efficiency Samples (>95%)')
#
# # 添加辅助线 (Add reference lines)
# ax.axvline(0.8, color='grey', linestyle='--', linewidth=1)  # 0.8 MPa ≈ 8 bar
# ax.axhline(95, color='grey', linestyle='--', linewidth=1)
#
# # 颜色条设置 (Colorbar settings)
# cbar = plt.colorbar(sc)
# cbar.set_label('Water Flux (LMH)', rotation=270, labelpad=15)
#
# # 标注优化区域 (Annotate optimization zone)
# ax.annotate('Recommended Zone', xy=(0.82, 96), xytext=(0.85, 85),
#            arrowprops=dict(arrowstyle="->", color='red'),
#            fontsize=12, color='red')
#
# ax.set_xlabel("Operating Pressure (MPa)", fontsize=12)
# ax.set_ylabel("PFOS Rejection Rate (%)", fontsize=12)
# plt.title("Pressure Optimization Strategy in Temperature (25°C) Environment", pad=20, fontsize=14)
# plt.legend()
# plt.show()

# # 分面散点图矩阵
from mpl_toolkits.mplot3d import Axes3D

# 筛选特定温度（示例：30°C）
temp_fixed = data[data['Temperature (˚C)'] > 19]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# 三维散点图
sc = ax.scatter(temp_fixed['Pressure (MPa)'],
               temp_fixed['Pore size(nm)'],
               temp_fixed['MWCO(Da)'],
               c=temp_fixed[target], cmap='RdYlGn', s=50)

ax.set_xlabel('Pressure (MPa)')
ax.set_ylabel('Pore Size (nm)')
ax.set_zlabel('MWCO (Da)')
cbar = plt.colorbar(sc)
cbar.set_label('Rejection Rate (%)')
plt.title('3D Parameter Interaction at 30°C')
plt.show()