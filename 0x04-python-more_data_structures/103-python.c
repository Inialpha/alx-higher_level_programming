#include <Python.h>

/**
 *print_python_bytes - print info about a byte obj
 *@p: a PyBytesObject pointer
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0, num_bytes, i;
	PyBytesObject *obj = (PyBytesObject *)p;
	char *trying_str;
	if (PyBytes_Check(p))
	{
		size = PyBytes_Size(p);
		num_bytes = size + 1;

		if (num_bytes > 10)
			num_bytes = 10;
		trying_str = obj->ob_sval;
		printf("[.] bytes object info\n");
		printf("  size: %ld\n", size);
		printf("  trying string: %s\n", trying_str);
		printf("  first %ld bytes: ", num_bytes);
		for (i = 0; i < num_bytes - 1; i++)
			printf("%02x ", (unsigned char) obj->ob_sval[i]);

		printf("%02x\n", obj->ob_sval[i]);
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}



/**                                                * print_python_list - prints info about a python list                                               * @p: python object
 */
void print_python_list(PyObject *p)
{
	int i, num_alloc, size;
        PyObject * obj;
	PyListObject *list = (PyListObject *)p;
	
	num_alloc = list->allocated;
	size = PyList_GET_SIZE(p);
	printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", num_alloc);

	for (i = 0; i < size; i++)
	{
                obj = PyList_GET_ITEM(p, i);
                printf("Element %d: %s\n", i, obj->ob_type->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
        }
}
