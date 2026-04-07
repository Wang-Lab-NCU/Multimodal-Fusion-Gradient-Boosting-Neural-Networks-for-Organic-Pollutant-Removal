import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 解释问题4
# 通过颜色和大小编码展示了压力与孔径的同步变化。如果高温点（右侧）普遍伴随较小的孔径（小点）或较低压力（冷色），就能解释负相关
# 因为压力和孔径 与 水通量是正相关， 从图种可以看出
# 读取 Excel 文件
file_path = "pfas_nalv - 副本.xlsx"  # 替换为你的 Excel 文件路径
sheet_name = 0  # 如果需要指定工作表名称或索引，可以修改
data = pd.read_excel(file_path, sheet_name=sheet_name)

# 温度-水通量关系图（叠加其他变量影响）
plt.figure(figsize=(10, 6))
scatter = sns.scatterplot(
    data=data,
    x="Temperature (˚C)",
    y="water flux(LMH)",
    hue="Pressure (MPa)",  # 用颜色表示压力值
    size="Pore size(nm)",  # 用点大小表示孔径
    sizes=(20, 200),  # 点大小范围
    palette="viridis"  # 颜色方案
)
plt.title("Temperature vs Water Flux (Color: Pressure, Size: Pore Size)")
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("Figure_温度-水通量关系图.tif", format="tif", dpi=300)
plt.show()

# 温度分布直方图（展示温度范围狭窄）
# 温度分布图直接显示数据集中在狭窄区间，难以观察显著趋势。
# plt.figure(figsize=(8, 4))
# sns.histplot(data["Temperature (˚C)"], bins=5, kde=True)
# plt.title("Temperature Distribution (Narrow Range: 20-25°C)")
# plt.xlabel("Temperature (˚C)")
# plt.ylabel("Count")
# plt.grid(True)
#
# # 调整图像布局，增加底部边距
# plt.subplots_adjust(bottom=0.15)  # 调整底部边距
#
#
# plt.savefig("Figure_温度分布直方图.tif", format="tif", dpi=300)
# plt.show()

# # 多变量分面回归图
# g = sns.lmplot(
#     data=data,
#     x="Temperature (˚C)",
#     y="water flux(LMH)",
#     col="Pressure (MPa)",  # 按压力分列
#     hue="Pore size(nm)",   # 按孔径着色
#     col_wrap=3,            # 每行显示3列
#     height=4,
#     aspect=1.2,
#     scatter_kws={'alpha':0.6}
# )
# g.set_titles("Pressure = {col_name} MPa")
# g.fig.subplots_adjust(top=0.9)
# g.fig.suptitle("Temperature vs Water Flux Under Different Pressures")
# plt.show()
