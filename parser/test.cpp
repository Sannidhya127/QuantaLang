
#include <C:\Users\USER\AppData\Local\Programs\Python\Python311\include\Python.h>


class Interpreter {
public:
    Interpreter() {
        Py_Initialize();
    }

    ~Interpreter() {
        Py_Finalize();
    }

    void execute(const char* code) {
        PyRun_SimpleString(code);
    }
};

int main() {
    Interpreter interpreter;

    // Import the necessary modules
    interpreter.execute("import sys");
    interpreter.execute("sys.path.append('/path/to/your/modules')");

    // Import your QuantaLang modules
    interpreter.execute("import qubit");
    interpreter.execute("import gates");
    interpreter.execute("import var");
    interpreter.execute("import probe");

    // Execute some QuantaLang code
    interpreter.execute("q = qubit.Qubit(0)");
    interpreter.execute("g = gates.Gate()");
    interpreter.execute("v = var.Var()");
    interpreter.execute("p = probe.Probe()");

    return 0;
}