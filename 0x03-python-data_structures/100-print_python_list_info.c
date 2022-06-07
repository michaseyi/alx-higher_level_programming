#include <Python.h>

/**
 * print_python_list_info - Prints some basic info about a Python list
 * @p: Pointer to the Python list
 */

void print_python_list_info(PyObject *p)
{
	int i, allocated = ((PyListObject *)p)->allocated, list_size = Py_SIZE(p);
	PyObject *obj;

	printf("[*] Size of the Python List = %d\n", list_size);
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < list_size; i++)
	{
		obj = PyList_GET_ITEM(p, i);
		printf("Element %d: ", i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
