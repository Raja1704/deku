import typer 
import sys
from docx2pdf import convert as ToPdfConverter
from pdf2docx import Converter as ToDocConverter

app = typer.Typer()


@app.command()
def ConvertToPdf(input_docx: str):
    ToPdfConverter(input_docx)

@app.command()
def ConvertToWord(input_pdf: str):
    ToDocConverter(input_pdf)

@app.command()
def ConvertToPng(input_png: str):
    typer.echo("This feature is not available yet")

@app.command()
def ConvertToJpg(input_jpg: str):
    typer.echo("This feature is not available yet")

@app.command()
def CompressImageSize(input_image: str):
    typer.echo("This feature is not available yet")

if len(sys.argv) != 2:
    print(f"\n                                        👀 Hello There!!! I'm Deku\n")


if __name__ == "__main__":
    app()


