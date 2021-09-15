#define PY_SSIZE_T_CLEAN
#include <Python.h>

void print_python_list_info(PyObject *p)
{
    long int len = PyList_Size(p);

    PyListObject 
}