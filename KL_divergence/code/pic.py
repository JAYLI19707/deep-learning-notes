import subprocess

pdf_path = r"D:\\Year3\\科研\\手写教材\\rednote\\KL_divergence\\KL.pdf"
output_prefix = "output"
start_page = 1
end_page = 5

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
