# A merger for PDF file
# This is a little training project
# From "Internet Made Coder" on Youtube
import PyPDF2
import os

#g_merger = PyPDF2.PdfFileMerger()
g_merger = PyPDF2.PdfMerger()


def get_files():
    # Get the files to merge, alphabetical ordered
    list_dir = os.listdir('.')
    list_dir_lower = [f.lower() for f in list_dir]   # Convert to lower case
    return sorted(list_dir)


def start(list_dir):
    for l_file in list_dir:
        if l_file.endswith(".pdf") or l_file.endswith(".PDF"):
            g_merger.append(l_file)
    g_merger.write("combined.pdf")


if __name__ == '__main__':

    start(get_files())

    
