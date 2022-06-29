#include <Python.h>
#include <locale.h>

/**
 * print_python_string - Prints info about a Python unicode object
 * @p: Pointer to the unicode object
 * Return: void
 */

void print_python_string(PyObject *p)
{
	Py_ssize_t len;

	setlocale(LC_ALL, "C.UTF-8");
	printf("[.] string object info\n");
	if (strcmp("str", p->ob_type->tp_name))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	len = ((PyASCIIObject *)p)->length;
	printf("  length: %ld\n", len);
	printf("  value: %ls\n",
		   PyUnicode_AsWideCharString(p, &len));
}
