import pandas as pd

def read_from_console():
  """
  Function to read text from the console.

  Args:
    None

  Returns:
    User-entered text (str).
  """
  text = input("Enter text: ")
  return text

def read_from_file_builtin(filepath):
  """
  Function to read text from a file using Python's built-in capabilities.

  Args:
    filepath: Path to the file (str).

  Returns:
    Text read from the file (str).
  """
  with open(filepath, "r") as f:
    text = f.read()
  return text

def read_from_file_pandas(filepath):
  """
  Function to read text from a file using the Pandas library.

  Args:
    filepath: Path to the file (str).

  Returns:
    Text read from the file (str).
  """
  df = pd.read_csv(filepath)
  text = df.to_string()
  return text
