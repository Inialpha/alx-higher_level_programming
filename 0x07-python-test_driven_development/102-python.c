#include "Python.h"

/**
 * print_python_string - Prints info about a Python string.
 * @p: PyObject string.
 */

void print_python_string(PyObject *p)
{
	long int len;

	fflush(stdout);

	printf("[.] string object info\n");
	fflush(stdout);

	if (strcmp(p->ob_type->tp_name, "str") == 0)
	{
		len = ((PyASCIIObject *)(p))->length;
		if (PyUnicode_IS_COMPACT_ASCII(p))
			printf("  type: compact ascii\n");
		else
			printf("  type: compact unicode object\n");
		printf("  length: %ld\n", length);
		printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
	}
	else
		printf("  [ERROR] Invalid String Object\n");
}
