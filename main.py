import shopee_data
import graphic_data
import organize_data



df = shopee_data.create_df()
organize_data.describe_data(df)
# graphic_data.window_result(df)
# print(df)
print("移除離群值跟0前:")
graphic_data.draw_box_figure(df)
for i in range(5):
    df = organize_data.remove_zero(df)
    df = organize_data.remove_outliers(df)
print("移除離群值跟0後:")
graphic_data.draw_box_figure(df)
graphic_data.draw_scatter_figure(df)
