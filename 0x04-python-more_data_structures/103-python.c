#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
  *print_python_list - print a python list info
  *
  *@p: python object
 */
void print_python_list(PyObject *p)
{
	int size, i, ;
	PyObject *item;
	PyListObject *list = (PyListObject *)p;

	size = PyList_Size(p);;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item)):
			print_python_bytes(item);
	}
}

/**
  *print_python_bytes - print python bytes objects.
  *
  *@p: python object
 */
void print_python_bytes(PyObject *p)
{
	int i, size;
	char *bytes_str;

	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return (0);
	}

	if (PyBytes_AsStringAndSize(p, &string, &size) != -1)
	{
		printf("  size: %ld\n", size);
		printf("  trying string: %s\n", bytes_str);

		if (size > 10)
			size = 10;
		else
			size += 1;

		printf("  first %ld bytes: ", size);
		for (i = 0; i < size; i++)
		{
			printf("%02x", bytes_str[i]);
			if (i < size - 1)
				printf(" ");
		}
		printf("\n");
	}
}
