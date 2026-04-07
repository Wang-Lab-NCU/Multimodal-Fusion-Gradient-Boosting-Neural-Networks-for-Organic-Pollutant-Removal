import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 解释问题1
# 读取 Excel 文件
# file_path = "pfas_nalv - 副本.xlsx"  # 替换为你的 Excel 文件路径
# sheet_name = 0  # 如果需要指定工作表名称或索引，可以修改
# df = pd.read_excel(file_path, sheet_name=sheet_name)
#
#
#
# # 离子浓度与pH值分布
# sns.pairplot(df, hue='Membrane type',
#              vars=[ 'pH', 'Monovalent cations (mmol/L)', 'Pressure (MPa)', 'Temperature (˚C)'])
# plt.suptitle("Ionic Conditions vs. PFOS Rejection by Membrane Type", y=1.02)
# plt.show()
# 读取数据

# # 不同特征与膜类型的分布图
file_path = "pfas_nalv - 副本.xlsx"
df = pd.read_excel(file_path, sheet_name=0)
#
# # 获取所有膜类型并排序
# membrane_types = sorted(df['Membrane type'].unique())
#
# # --- 自定义调色板：膜6用深蓝色，其他用默认颜色 ---
# # 生成基础色板（例如husl调色板）
# base_palette = sns.color_palette("husl", n_colors=len(membrane_types))
#
# # 找到膜6在排序后的列表中的索引位置
# membrane6_idx = membrane_types.index(6)  # 假设膜6的标签是数字6
#
# # 将膜6的颜色替换为深蓝色（RGB值或十六进制）
# base_palette[membrane6_idx] = (0, 0, 0.5)  # RGB: 深蓝色
# # 或使用十六进制：base_palette[membrane6_idx] = "#00008B"
#
# # --- 绘制Pairplot ---
# sns.pairplot(
#     df,
#     hue='Membrane type',
#     vars=['pH', 'Monovalent cations (mmol/L)', 'Pressure (MPa)', 'Temperature (˚C)'],
#     palette=base_palette,  # 应用自定义调色板
#     hue_order=membrane_types,  # 确保颜色顺序与调色板一致
#     plot_kws={'alpha': 0.7, 's': 30}  # 可选：调整点透明度与大小
# )
#
# plt.suptitle("Ionic Conditions vs. PFOS Rejection by Membrane Type", y=1.02)
# plt.savefig("Figure_问题1.tif", format="tif", dpi=400)
# plt.show()


# variables = ['pH', 'Monovalent cations (mmol/L)', 'Pressure (MPa)', 'Temperature (˚C)']
# # 转换数据为长格式
# df_melt = df.melt(id_vars='Membrane type', value_vars=variables)
#
# # 绘制分面箱线图
# g = sns.catplot(
#     data=df_melt,
#     x='Membrane type',
#     y='value',
#     col='variable',
#     kind='box',
#     col_wrap=2,
#     palette='husl',
#     height=4,
#     aspect=1.2,
#     sharey=False  # 各子图独立y轴范围
# )
#
# # 调整标签和标题
# g.set_axis_labels("Membrane Type", "Value")
# g.set_titles(col_template="{col_name}")
# g.fig.suptitle("Box Plots of Variables by Membrane Type", y=1.02)
# plt.show()


# # 多变量联合分布（散点矩阵图）
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取数据
file_path = "pfas_nalv - 副本.xlsx"
df = pd.read_excel(file_path, sheet_name=0)

# 定义目标变量
variables = ['pH', 'Monovalent cations (mmol/L)', 'Pressure (MPa)', 'Temperature (˚C)']

# 转换数据为长格式
df_melt = df.melt(id_vars='Membrane type', value_vars=variables)

# 绘制分面箱线图
g = sns.catplot(
    data=df_melt,
    x='Membrane type',
    y='value',
    col='variable',
    kind='box',
    col_wrap=2,
    palette='husl',
    height=4,
    aspect=1.2,
    sharey=False,
    legend_out=False
)

# 设置全局标题（下移标题位置）
g.fig.suptitle(
    "Distribution of Variables by Membrane Type",
    y=0.95,  # 降低标题的垂直位置
    fontsize=14
)

# 调整图形布局增加顶部空间
g.fig.subplots_adjust(top=0.90)  # 增加顶部边距

# 设置轴标签
g.set_axis_labels(x_var="Membrane Type", y_var="")

# 为每个子图单独设置y轴标签
for ax, var in zip(g.axes.flat, variables):
    ax.set_ylabel(var)

# 隐藏子图标题
g.set_titles(col_template="")
plt.savefig("Figure_问题11.tif", format="tif", dpi=300)
plt.show()









# # 膜类型样本数量分析
# 假设df为数据集，'Membrane type'为膜类型列
# sns.countplot(data=df, x='Membrane type', order=df['Membrane type'].value_counts().index)
# plt.title("Membrane Type Sample Distribution")
# plt.xlabel("Membrane Type")
# plt.ylabel("Sample Count")
# plt.xticks(rotation=45)
# plt.show()


# plt.figure(figsize=(12,5))
# plt.subplot(1,2,1)
# sns.boxplot(data=df, x='Membrane type', y='Pressure (MPa)', order=df['Membrane type'].value_counts().index)
# plt.xticks(rotation=45)
# plt.title("Pressure Distribution by Membrane Type")
#
# plt.subplot(1,2,2)
# sns.boxplot(data=df, x='Membrane type', y='Temperature (˚C)', order=df['Membrane type'].value_counts().index)
# plt.xticks(rotation=45)
# plt.title("Temperature Distribution by Membrane Type")
# plt.tight_layout()
# plt.show()




# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.manifold import TSNE
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import silhouette_score
#
# # 假设df是你的数据集
# # 选择关键特征
# features = df[['Pressure (MPa)', 'Temperature (˚C)', 'Monovalent cations (mmol/L)',
#               'pH', 'Divalent cations (mmol/L)', 'Trivalent cations (mmol/L)', 'PFOS con (ppb)']]
# labels = df['Membrane type']
#
# # 特征标准化
# scaler = StandardScaler()
# features_scaled = scaler.fit_transform(features)
#
# # t-SNE降维
# tsne = TSNE(n_components=2, perplexity=30, n_iter=1000, random_state=42)
# embedded = tsne.fit_transform(features_scaled)
#
# # 可视化
# plt.figure(figsize=(10, 8))
# plt.scatter(embedded[:, 0], embedded[:, 1], c=labels.astype('category').cat.codes, cmap='tab10')
# plt.title("t-SNE Clustering of Membrane Types by Experimental Conditions")
# plt.xlabel("t-SNE Component 1")
# plt.ylabel("t-SNE Component 2")
# plt.colorbar(ticks=range(len(labels.unique())), label='Membrane Type')
# plt.show()
#
# # 聚类效果评估
# silhouette_avg = silhouette_score(features_scaled, labels.astype('category').cat.codes)
# print(f"Silhouette Score: {silhouette_avg}")