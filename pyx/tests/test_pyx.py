import unittest
from pyx.compiler import compile_source, PyXError
from pyx.runtime import run_source

class PyXTests(unittest.TestCase):
    def test_let_and_fn(self):
        env = run_source("let x = 4\nfn square(n):\n    give n*n\ny = square(x)\n")
        self.assertEqual(env["y"], 16)

    def test_pipeline(self):
        env = run_source("fn double(x):\n    give x*2\nresult = 5 |> double\n")
        self.assertEqual(env["result"], 10)

    def test_pipeline_call(self):
        env = run_source("fn add(x, y):\n    give x+y\nresult = 5 |> add(7)\n")
        self.assertEqual(env["result"], 12)

    def test_strict_type(self):
        with self.assertRaises(TypeError):
            run_source('let count: int = "wrong"\n')

    def test_invalid_pipeline(self):
        with self.assertRaises(PyXError):
            compile_source("x = 1 |>\n")

if __name__ == "__main__":
    unittest.main()
