import json
from latex_generator.latex_generator import generate_table_latex, generate_image_latex


def main():
    with open("data/table_data.json", "r") as f:
        table_data = json.load(f)["table"]

    table_code = generate_table_latex(table_data)
    image_code = generate_image_latex(
        "../data/image.png", caption="Sample Image")

    document = r"""\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{graphicx}
\begin{document}
"""
    document += table_code + "\n"
    document += image_code + "\n"
    document += r"\end{document}\n"

    with open("artifacts/output.tex", "w", encoding="utf-8") as f:
        f.write(document)


if __name__ == "__main__":
    main()
