#include "/usr/include/python3.8/Python.h"

/**
 * print_python_list - prints info about a python list
 * @p: python object
 */
void print_python_list(PyObject *p)
{
	int i, num_alloc, size;
	PyObject * obj;
	PyListObject *list = (PyListObject *)p;

	num_alloc = list->alloc;
	size = PyList_GET_SIZE(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("Allocated = %d\n", num_alloc);

	for (i = 0; i < size; i++)
	{
		obj = PyList_GET_ITEM(p, i);
		printf("Element %d: %s\n", obj->ob_type->tp_name);
	}
}
	
