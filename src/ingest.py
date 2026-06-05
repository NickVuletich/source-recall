"""
SUPPORTED_EXTENSIONS = {".txt", ".md"}

function load_documents(data_dir):
    turn data_dir into a Path object

    if folder does not exist:
        raise error

    create empty documents list

    loop through every file inside folder:
        if it is a file AND extension is supported:
            read text
            create dictionary with source, text, char_count
            append dictionary to documents

    return documents

    call load_documents()
    print number of documents
    for each document:
        print source
        print char count
        print preview of first 200-300 characters
    """
def load_documents(data_dir):
    