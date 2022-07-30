"""Run pylint and create a badge displaying the score"""

import argparse
from pylint.lint import Run


DEFAULT_MIN_YELLOW = 3.0
DEFAULT_MIN_GREEN = 7.0


def main():
    """Main deal"""
    parser = argparse.ArgumentParser()
    parser.add_argument("file_to_lint")
    parser.add_argument("output_file")
    parser.add_argument("--min_yellow", type=float)
    parser.add_argument("--min_green", type=float)
    args = parser.parse_args()
    file_to_lint = args.file_to_lint
    min_yellow = args.min_yellow
    if min_yellow is None:
        min_yellow = DEFAULT_MIN_YELLOW
    min_green = args.min_green
    if min_green is None:
        min_green = DEFAULT_MIN_GREEN

    linterstats_obj = Run([file_to_lint], do_exit=False).linter.stats
    try:
        score = linterstats_obj["global_note"]
    except TypeError:
        score = linterstats_obj.global_note
    score = round(score, 2)
    template = """
<svg xmlns="http://www.w3.org/2000/svg" width="85" height="20">
    <linearGradient id="a" x2="0" y2="100%">
        <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
        <stop offset="1" stop-opacity=".1"/>
    </linearGradient>
    <rect rx="3" width="85" height="20" fill="#555"/>
    <rect rx="3" x="50" width="35" height="20" fill="{color}"/>
    <path fill="{color}" d="M50 0h4v20h-4z"/><rect rx="3" width="85" height="20" fill="url(#a)"/>
    <g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="11">
        <text x="25" y="15" fill="#010101" fill-opacity=".3">pylint</text><text x="25" y="14">pylint</text>
        <text x="67" y="15" fill="#010101" fill-opacity=".3">{score}</text><text x="67" y="14">{score}</text>
    </g>
</svg>""".replace(
        "\n", ""
    ).replace(
        "    ", ""
    )

    color_ok = "#44cc11"
    color_warning = "#dfb317"
    color_red = "#e05d44"

    if float(score) < min_yellow:
        color = color_red
    elif min_yellow <= float(score) < min_green:
        color = color_warning
    else:
        color = color_ok

    with open(args.output_file, "w") as score_file:
        score_file.write(template.format(score=score, color=color))


if __name__ == "__main__":
    main()
