#include <Python.h>
#include <stdio.h>


/**
  *print_python_bytes - print python bytes objects.
  *
  *@p: python object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size = 0;
	char *bytes_str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return (-1);
	}

	if (PyBytes_AsStringAndSize(p, &string, &size) != -1)
	{
		printf("  size: %zd\n", size);
		printf("  trying string: %s\n", bytes_str);

		if (size >= 10)
			size = 10;
		else
			size += 1;

		printf("  first %zd bytes: ", size);
		for (i = 0; i < size && i < 10; i++)
		{
			printf("%02hhx", bytes_str[i]);

		}
		printf("\n");
	}
}

/**
  *print_python_list - print a python list info
  *
  *@p: python object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	int i;
	PyObject *item;
	/*PyListObject *list = (PyListObject *)p;*/

	if (!PyList_CheckExact(p))
		return (-1);
	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	/*printf("[*] Allocated = %ld\n", list->allocated);*/
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}

