#include <Python.h>
#include <stdio.h>

/**
  *print_python_list - print a python list
  *
  *@p: python object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
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
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return (0);
	}

	size = PyBytes_Size(p);
	bytes_str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes_str);

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
