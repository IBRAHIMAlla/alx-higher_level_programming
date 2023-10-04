#include "Python.h"

/**
 * print_python_string - Prints information.
 * @p: A PyObject string.
 */
void print_python_string(PyObject *p)
{
	long int lgth;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	lgth = ((PyASCIIObject *)(p))->lgth;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", lgth);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &lgth));
