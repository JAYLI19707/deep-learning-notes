import subprocess

pdf_path = r"D:\\Year3\\科研\\Pytorch\\pytorch_xiaohongshu_note.pdf"
output_prefix = "output"
start_page = 11
end_page = 27

subprocess.run([
    "pdftoppm",
    pdf_path,
    output_prefix,
    "-png",
    "-r", "300",
    "-f", str(start_page),
    "-l", str(end_page)
])

print("转换完成")
