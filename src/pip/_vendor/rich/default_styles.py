from typing import Dict

from .style import Style

DEFAULT_STYLES: Dict[str, Style] = {
    "none": Style.null(),
    "reset": Style(
        color="default",
        bgcolor="default",
        dim=False,
        bold=False,
        italic=False,
        underline=False,
        blink=False,
        blink2=False,
        reverse=False,
        conceal=False,
        strike=False,
    ),
    "dim": Style(dim=True),
    "bright": Style(dim=False),
    "bold": Style(bold=True),
    "strong": Style(bold=True),
    "code": Style(reverse=True, bold=True),
    "italic": Style(italic=True),
    "emphasize": Style(italic=True),
    "underline": Style(underline=True),
    "blink": Style(blink=True),
    "blink2": Style(blink2=True),
    "reverse": Style(reverse=True),
    "strike": Style(strike=True),
    "black": Style(color="black"),
    "red": Style(color="red"),
    "green": Style(color="green"),
    "yellow": Style(color="yellow"),
    "magenta": Style(color="magenta"),
    "cyan": Style(color="cyan"),
    "white": Style(color="white"),
    "inspect.attr": Style(color="yellow", italic=True),
    "inspect.attr.dunder": Style(color="yellow", italic=True, dim=True),
    "inspect.callable": Style(bold=True, color="red"),
    "inspect.async_def": Style(italic=True, color="bright_cyan"),
    "inspect.def": Style(italic=True, color="bright_cyan"),
    "inspect.class": Style(italic=True, color="bright_cyan"),
    "inspect.error": Style(bold=True, color="red"),
    "inspect.equals": Style(),
    "inspect.help": Style(color="cyan"),
    "inspect.doc": Style(dim=True),
    "inspect.value.border": Style(color="green"),
    "live.ellipsis": Style(bold=True, color="red"),
    "layout.tree.row": Style(dim=False, color="red"),
    "layout.tree.column": Style(dim=False, color="blue"),
    "logging.keyword": Style(bold=True, color="yellow"),
    "logging.level.notset": Style(dim=True),
    "logging.level.debug": Style(color="green"),
    "logging.level.info": Style(color="blue"),
    "logging.level.warning": Style(color="yellow"),
    "logging.level.error": Style(color="red", bold=True),
    "logging.level.critical": Style(color="red", bold=True, reverse=True),
    "log.level": Style.null(),
    "log.time": Style(color="cyan", dim=True),
    "log.message": Style.null(),
    "log.path": Style(dim=True),
    "repr.ellipsis": Style(color="yellow"),
    "repr.indent": Style(color="green", dim=True),
    "repr.error": Style(color="red", bold=True),
    "repr.str": Style(color="green", italic=False, bold=False),
    "repr.brace": Style(bold=True),
    "repr.comma": Style(bold=True),
    "repr.ipv4": Style(bold=True, color="bright_green"),
    "repr.ipv6": Style(bold=True, color="bright_green"),
    "repr.eui48": Style(bold=True, color="bright_green"),
    "repr.eui64": Style(bold=True, color="bright_green"),
    "repr.tag_start": Style(bold=True),
    "repr.tag_name": Style(color="bright_magenta", bold=True),
    "repr.tag_contents": Style(color="default"),
    "repr.tag_end": Style(bold=True),
    "repr.attrib_name": Style(color="yellow", italic=False),
    "repr.attrib_equal": Style(bold=True),
    "repr.attrib_value": Style(color="magenta", italic=False),
    "repr.number": Style(color="cyan", bold=True, italic=False),
    "repr.number_complex": Style(color="cyan", bold=True, italic=False),  # same
    "repr.bool_true": Style(color="bright_green", italic=True),
    "repr.bool_false": Style(color="bright_red", italic=True),
    "repr.none": Style(color="magenta", italic=True),
    "repr.url": Style(underline=True, color="bright_blue", italic=False, bold=False),
    "repr.uuid": Style(color="bright_yellow", bold=False),
    "repr.call": Style(color="magenta", bold=True),
    "repr.path": Style(color="magenta"),
    "repr.filename": Style(color="bright_magenta"),
    "rule.line": Style(color="bright_green"),
    "rule.text": Style.null(),
    "json.brace": Style(bold=True),
    "json.bool_true": Style(color="bright_green", italic=True),
    "json.bool_false": Style(color="bright_red", italic=True),
    "json.null": Style(color="magenta", italic=True),
    "json.number": Style(color="cyan", bold=True, italic=False),
    "json.str": Style(color="green", italic=False, bold=False),
    "json.key": Style(color="blue", bold=True),
    "prompt": Style.null(),
    "prompt.choices": Style(color="magenta", bold=True),
    "prompt.default": Style(color="cyan", bold=True),
    "prompt.invalid": Style(color="red"),
    "prompt.invalid.choice": Style(color="red"),
    "pretty": Style.null(),
    "scope.border": Style(color="blue"),
    "scope.key": Style(color="yellow", italic=True),
    "scope.key.special": Style(color="yellow", italic=True, dim=True),
    "scope.equals": Style(color="red"),
    "table.header": Style(bold=True),
    "table.footer": Style(bold=True),
    "table.cell": Style.null(),
    "table.title": Style(italic=True),
    "table.caption": Style(italic=True, dim=True),
    "traceback.error": Style(color="red", italic=True),
    "traceback.border.syntax_error": Style(color="bright_red"),
    "traceback.border": Style(color="red"),
    "traceback.text": Style.null(),
    "traceback.title": Style(color="red", bold=True),
    "traceback.exc_type": Style(color="bright_red", bold=True),
    "traceback.exc_value": Style.null(),
    "traceback.offset": Style(color="bright_red", bold=True),
    "traceback.error_range": Style(underline=True, bold=True),
    "traceback.note": Style(color="green", bold=True),
    "traceback.group.border": Style(color="magenta"),
    "bar.back": Style(color="grey23"),
    "bar.complete": Style(color="rgb(249,38,114)"),
    "bar.finished": Style(color="rgb(114,156,31)"),
    "bar.pulse": Style(color="rgb(249,38,114)"),
    "progress.description": Style.null(),
    "progress.filesize": Style(color="green"),
    "progress.filesize.total": Style(color="green"),
    "progress.download": Style(color="green"),
    "progress.elapsed": Style(color="yellow"),
    "progress.percentage": Style(color="magenta"),
    "progress.remaining": Style(color="cyan"),
    "progress.data.speed": Style(color="red"),
    "progress.spinner": Style(color="green"),
    "status.spinner": Style(color="green"),
    "tree": Style(),
    "tree.line": Style(),
    "markdown.paragraph": Style(),
    "markdown.text": Style(),
    "markdown.em": Style(italic=True),
    "markdown.emph": Style(italic=True),  # For commonmark backwards compatibility
    "markdown.strong": Style(bold=True),
    "markdown.code": Style(bold=True, color="cyan", bgcolor="black"),
    "markdown.code_block": Style(color="cyan", bgcolor="black"),
    "markdown.block_quote": Style(color="magenta"),
    "markdown.list": Style(color="cyan"),
    "markdown.item": Style(),
    "markdown.item.bullet": Style(color="yellow", bold=True),
    "markdown.item.number": Style(color="yellow", bold=True),
    "markdown.hr": Style(color="yellow"),
    "markdown.h1.border": Style(),
    "markdown.h1": Style(bold=True),
    "markdown.h2": Style(bold=True, underline=True),
    "markdown.h3": Style(bold=True),
    "markdown.h4": Style(bold=True, dim=True),
    "markdown.h5": Style(underline=True),
    "markdown.h6": Style(italic=True),
    "markdown.h7": Style(italic=True, dim=True),
    "markdown.link": Style(color="bright_blue"),
    "markdown.link_url": Style(color="blue", underline=True),
    "markdown.s": Style(strike=True),
    "iso8601.date": Style(color="blue"),
    "iso8601.time": Style(color="magenta"),
    "iso8601.timezone": Style(color="yellow"),
}


if __name__ == "__main__":  # pragma: no cover
    import argparse
    import io

    from pip._vendor.rich.console import Console
    from pip._vendor.rich.table import Table
    from pip._vendor.rich.text import Text

    parser = argparse.ArgumentParser()
    parser.add_argument("--html", action="store_true", help="Export as HTML table")
    args = parser.parse_args()
    html: bool = args.html
    console = Console(record=True, width=70, file=io.StringIO()) if html else Console()

    table = Table("Name", "Styling")

    for style_name, style in DEFAULT_STYLES.items():
        table.add_row(Text(style_name, style=style), str(style))

    console.print(table)
    if html:
        print(console.export_html(inline_styles=True))
