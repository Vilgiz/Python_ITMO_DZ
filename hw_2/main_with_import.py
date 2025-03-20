import os
from latex_generator_VILGIZ import generate_table_latex, generate_image_latex, compile_latex_to_pdf


def main():
    table_data = [
        ["Header 1", "Header 2"],
        [1, 2],
        [3, 4]
    ]

    image_path = "example.png"

    if not os.path.exists(image_path):
        print(
            f"Ошибка: файл {image_path} не найден.")
        return

    latex_table = generate_table_latex(
        table_data
    )

    latex_image = generate_image_latex(
        image_path, caption="Example"
    )
    latex_content = f"""
\\documentclass{{article}}
\\usepackage[utf8]{{inputenc}}  
\\usepackage{{graphicx}}

\\begin{{document}}

{latex_table}

{latex_image}

\\end{{document}}
"""

    try:
        compile_latex_to_pdf(latex_content, output_name="output")
        print("PDF успешно сгенерирован и сохранён в output.pdf")
    except Exception as e:
        print(f"Ошибка при компиляции LaTeX в PDF: {e}")


if __name__ == "__main__":
    main()
