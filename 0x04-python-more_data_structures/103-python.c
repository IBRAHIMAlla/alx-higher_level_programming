#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints bytes information
 *
 * @p: the PyObject
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t s = 0, m = 0;
	char *str = NULL;

	printf("[.] bytes object info\n");

	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	if (PyBytes_AsStringAndSize(p, &str, &s) != -1)
	{
		printf("  size: %zd\n", s);
		printf("  trying string: %s\n", str);
		printf("  first %zd bytes:", s < 10 ? s + 1 : 10);
		for (; i < size + 1 && m < 10; m++)
		{
			printf(" %02hhx", string[m]);
		}
		printf("\n");
	}
}

/**
 * print_python_list - Prints list information
 *
 * @p: the PyObject
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t s = 0;
	PyObject *it;
	int m = 0;

	if (PyList_CheckExact(p))
	{
		size = PyList_Size(p);

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %zd\n", s);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

		for (; m < s; m++)
		{
			it = PyList_GET_ITEM(p, m);
			printf("Element %d: %s\n", m, it->ob_type->tp_name);
			if (PyBytes_Check(it))
				print_python_bytes(it);
		}
	}
}
