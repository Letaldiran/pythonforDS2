def write_to_console(text):
  """
  Function to print text to the console.

  Args:
    text: Text to be printed (str).

  Returns:
    None.
  """
  print(text)

def write_to_file_builtin(filepath, text):
  """
  Function to write text to a file using Python's built-in capabilities.

  Args:
    filepath: Path to the file (str).
    text: Text to be written (str).

  Returns:
    None.
  """
  with open(filepath, "w") as f:
    f.write(text)
