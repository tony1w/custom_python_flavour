PyX - Custom Python Flavour
PyX is a custom Python language flavour built using CPython.
It introduces custom syntax and language constructs, which are
transformed into Python code and executed using the CPython
compiler and runtime.

-----------------
ARCHITECTURE
-----------------

PyX follows a compiler frontend and backend architecture.

              PyX Source Code (.pyx)
                       |
                       v
              Custom Syntax Frontend
                       |
                       v
              Syntax Transformation
                       |
                       v
                 Python AST
                       |
                       v
                CPython Compiler
                       |
                       v
               Python Code Object
                       |
                       v
               CPython Runtime
                       |
                       v
                  Execution


Compilation Process:

1. Source Input
   Reads the .pyx source file.

2. Syntax Processing
   Recognizes PyX-specific syntax.

3. Transformation
   Converts custom constructs into Python-compatible syntax.

4. AST Generation
   Parses the transformed source into a Python Abstract
   Syntax Tree.

5. Compilation
   CPython compiles the AST into a code object.

6. Execution
   The runtime executes the compiled code.


---------------
HOW TO RUN
---------------

Requirements:
- Python 3.9 or newer
- No external dependencies


Clone the repository:
-git clone https://github.com/YOUR_USERNAME/PyX-Custom-Python.git
-cd PyX-Custom-Python


Run an example:
-python -m pyx examples/hello.pyx


Run the main demonstration:
-python -m pyx examples/example.pyx
Debug mode:
Display the generated Python code before execution:
-python -m pyx examples/example.pyx --debug


Interactive mode:
Start the PyX interactive shell:
-python -m pyx


Exit the shell:
- :quit