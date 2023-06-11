#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints information about python list
 * @p: the python list object
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	PyObject *obj;

	int i, size, num_alloc;

	num_alloc = list->allocated;
	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", num_alloc);

	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
