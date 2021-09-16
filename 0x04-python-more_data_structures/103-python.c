#define PY_SSIZE_T_CLEAN                                                                                                                                                                      
#include <Python.h>                                                                                                                                                                           
                                                                                                                                                                                              
void print_python_list(PyObject *p)
{
	long int len = PyList_Size(p);
        int i;
        PyBytes_Type *obj = (PyBytes_Type *)p;
        printf("[*] Size of the Python List = %li\n", len); 
        printf("[*] Allocated = %li\n", obj->allocated); 
        for(i = 0; i < len; i++)
        { 
                printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name); 
        } 
}

void print_python_bytes(PyObject *p)
{
        long int len = PyBytes_Size(p);
        int i;
        PyBytes_Type *obj = (PyBytes_Type *p);
        printf("[.] bytes object info\n"); 
        printf("size: %li\n", len);
        printf("trying string: %s\n", PyBytes_AsString(p));
        for(i = 0; i < len; i++)
        {
                printf("first %c bytes: %p\n", PyBytes_FromObject(obj->ob_item[0])->tp_);
        }
}

