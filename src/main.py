from textual.app import App, ComposeResult
from textual.widgets import MarkdownViewer
import aspose.words as aw
import os
import argparse

parser = argparse.ArgumentParser(description='Convert a PDF to Markdown.')
parser.add_argument('--pdf', help='Path to the input PDF file', required=True)
parser.add_argument(
    '--md', help='Path to the output Markdown file', required=True)
args = parser.parse_args()

# Load PDF file
doc = aw.Document(args.pdf)

# Save PDF as markdown
doc.save(args.md)

markdowntext = open(args.md).read()


class MarkdownExampleApp(App):
    def compose(self) -> ComposeResult:
        yield MarkdownViewer(markdowntext, show_table_of_contents=True)


if __name__ == "__main__":
    app = MarkdownExampleApp()
    app.run()
