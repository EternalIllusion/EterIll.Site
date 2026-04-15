import os
from PIL import Image

def upscale_pngs(directory, scale_factor=4):
    """
    读取目录下的所有PNG图片，并按指定倍数放大（最近邻插值）。
    
    :param directory: 图片所在的目录路径
    :param scale_factor: 放大倍数 (默认 4，即 400%)
    """
    
    # 获取当前目录下所有 png 文件
    png_files = [f for f in os.listdir(directory) if f.lower().endswith('.png')]
    
    if not png_files:
        print("当前目录下未找到 PNG 图片。")
        return

    print(f"找到 {len(png_files)} 个 PNG 文件，开始处理...")

    # 创建输出文件夹，防止覆盖原图
    output_dir = os.path.join(directory, "upscaled_output")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in png_files:
        file_path = os.path.join(directory, filename)
        
        try:
            with Image.open(file_path) as img:
                # 获取原始尺寸
                original_width, original_height = img.size
                
                # 计算新尺寸
                new_width = original_width * scale_factor
                new_height = original_height * scale_factor
                
                # 核心步骤：使用 Image.NEAREST 进行放大
                # Image.NEAREST 即最近邻插值，它直接复制像素，不会产生模糊或颜色混合
                upscaled_img = img.resize((new_width, new_height), resample=Image.NEAREST)
                
                # 保存新图片
                output_path = os.path.join(output_dir, filename)
                upscaled_img.save(output_path)
                
                print(f"✅ 已处理: {filename} -> 尺寸: {new_width}x{new_height}")
                
        except Exception as e:
            print(f"❌ 处理失败 {filename}: {e}")

    print(f"\n所有处理完成！图片已保存在 '{output_dir}' 文件夹中。")

if __name__ == "__main__":
    # 获取当前脚本所在的目录
    current_directory = os.getcwd()
    
    # 执行放大，倍数为 4 (400%)
    upscale_pngs(current_directory, scale_factor=4)