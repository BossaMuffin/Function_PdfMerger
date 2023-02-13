# A merger for PDF file
# This is a little training project
# From "Internet Made Coder" on Youtube
import PyPDF2
import os


g_merger = PyPDF2.PdfFileMerger()

def start():
    for l_file in os.listdir(os.curdir):
        if l_file.endswith(".pdf") or l_file.endswith(".PDF"):
            g_merger.append(l_file)
    g_merger.write("combined.pdf")


if __name__ == '__main__':
    start()
