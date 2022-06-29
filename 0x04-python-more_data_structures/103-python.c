#include <Python.h>

/**
 * print_python_bytes - Prints out details about a python bytes object
 * @p: Pointer to the byte object
 * Return: void
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = ((PyVarObject *)p)->ob_size, i = 0, disp_byte_size;
	char *string_val;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", size);
	string_val = ((PyBytesObject *)p)->ob_sval;
	printf("  trying string: ");
	for (i = 0; i < size; i++)
	{
		putchar(string_val[i]);
		if (!isascii(string_val[i]))
			break;
	}
	putchar(10);
	disp_byte_size = size + 1 > 10 ? 10 : size + 1;
	printf("  first %ld bytes: ", disp_byte_size);
	for (i = 0; i < disp_byte_size; i++)
	{
		printf("%02x", (unsigned char)((PyBytesObject *)p)->ob_sval[i]);
		if (i != disp_byte_size - 1)
			putchar(' ');
	}
	putchar(10);
}

/**
 * print_python_list - Prints out details about a python list object
 * @p: Pointer to the python list object
 * Return: void
 */

void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = ((PyVarObject *)p)->ob_size, i = 0;
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (; i < size; i++)
	{
		item = list->ob_item[i];
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (!strcmp(item->ob_type->tp_name, "bytes"))
			print_python_bytes(item);
	}
}
