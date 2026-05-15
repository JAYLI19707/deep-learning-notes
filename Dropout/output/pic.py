import subprocess
import os

pdf_path = r"D:\\Year3\\科研\\自媒体\\Dropout\\dropout_xiaohongshu_note.pdf"
output_folder = "output"
output_prefix = os.path.join(output_folder, "img")

os.makedirs(output_folder, exist_ok=True)

subprocess.run([
    "pdftoppm",
    pdf_path,
    output_prefix,
    "-png",
    "-r", "300"
])

print("转换完成")
