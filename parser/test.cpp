
#include <C:\Users\USER\AppData\Local\Programs\Python\Python311\include\Python.h>

int main() {
    // Initialize the Python interpreter
    Py_Initialize();

    // Import the qubit module
    PyObject* pModule = PyImport_ImportModule("qubit");

    // Check if the module was imported successfully
    if (pModule != NULL) {
        // Get a reference to the Qubit class
        PyObject* pClass = PyObject_GetAttrString(pModule, "Qubit");

        // Check if the class exists
        if (pClass != NULL && PyCallable_Check(pClass)) {
            // Create an instance of the Qubit class
            PyObject* pInstance = PyObject_CallObject(pClass, NULL);

            // Check if the instance was created successfully
            if (pInstance != NULL) {
                // Call methods or access attributes of the instance as needed
                // Example: Call a method named "measure"
                PyObject_CallMethod(pInstance, "measure", NULL);

                // Decrement reference count for the instance
                Py_DECREF(pInstance);
            } else {
                // Handle error
                PyErr_Print();
            }
            // Decrement reference count for the class
            Py_DECREF(pClass);
        } else {
            // Handle error
            PyErr_Print();
        }
        // Decrement reference count for the module
        Py_DECREF(pModule);
    } else {
        // Handle error
        PyErr_Print();
    }

    // Finalize the Python interpreter
    Py_Finalize();

    return 0;
}
