#include <Python.h>
#include <stdio.h>

/**
  *print_python_list - print a python list
  *
  *@p: python object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = PyObject_Length(p);
	Py_ssize_t i;
	PyObject *item;
	const char *type_name;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		type_name = item->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type_name);
	}
}

/**
  *print_python_bytes - print python bytes objects.
  *
  *@p: python object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	char *bytes_str;
	Py_ssize_t i;

	printf("[.] bytes object info\n");
	if (PyObject_HasAttrString(p, "encode"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return (0);
	}

	size = PyObject_Length(p);
	bytes_str = PyUnicode_AsUTF8(p);

	printf("  size: %ld\n", size);

	if (size > 10)
		size = 10;

	printf("  first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02x", (unsigned char)bytes_str[i]);
		if (i < size - 1)
			printf(" ");
	}
	printf("\n");
}
