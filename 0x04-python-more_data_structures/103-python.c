#define PY_SSIZE_T_CLEAN
#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_bytes - bytes
 * @p: hola
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	long int len = 0;
	int i = 0, j = 0, checking = 0;
	/*PyObject *obj;*/
	char *str;

	printf("[.] bytes object info\n");
	checking = PyBytes_Check(p);
	if (!checking)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	len = PyBytes_Size(p);
	str = PyBytes_AsString(p);
	printf("  size: %li\n", len);
	printf("  trying string: %s\n", str);
	i = PyBytes_Size(p);
	if (i > 10)
		i = 10;
	else
		i = i + 1;
	printf("  first %i bytes:", i);
	for (j = 0; j < i; j++)
	{
		printf(" %02x", str[j]);
	}
	printf("\n");
}
/**
 * print_python_list - list
 * @p: hola
 * Return: void
 */
void print_python_list(PyObject *p)
{
	long int len = PyList_Size(p);
	int i;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < len; i++)
	{
		printf("Element %i: %s\n", i, obj->ob_item[i]->ob_type->tp_name);
		if (obj->ob_item[i]->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(obj->ob_item[i]);
	}
}
