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
	const char *type_name;
	PyVarObject *item;
	PyListObject *list = (PyListObject *)p;

	item = (PyVarObject *)p;
	size = item->ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		type_name = list->ob_item[i]->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type_name);
		if (strcmp(type_name, "bytes") == 0):
			print_python_bytes(list->ob_item[i]);
	}
}

/**
  *print_python_bytes - print python bytes objects.
  *
  *@p: python object
 */
void print_python_bytes(PyObject *p)
{
	unsigned char i, size;
	PyBytesObject *bytes_str;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return (0);
	}

	size = ((PyVarObject *)p)->ob_size;
	bytes_str = ((PyListObject *)p)->ob_sval;

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
