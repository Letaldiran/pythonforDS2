from app.io import (read_from_console, read_from_file_builtin, read_from_file_pandas, \
                    write_to_console, write_to_file_builtin)

def main():
    text_from_console = read_from_console()
    text_from_file_builtin = read_from_file_builtin("data/input.txt")
    text_from_file_pandas = read_from_file_pandas("data/input.csv")

    write_to_console(text_from_console)
    write_to_console(text_from_file_builtin)
    write_to_console(text_from_file_pandas)
    write_to_file_builtin("data/output.txt", text_from_console)

if __name__ == "__main__":
    main()
