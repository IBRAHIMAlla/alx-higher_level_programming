#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: pointer.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t len, al, m;
	const char *s;
	PyListObject *l = (PyListObject *)p;
	PyVarObject *v = (PyVarObject *)p;

	len = v->ob_size;
	al = l->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", z);
	printf("[*] Allocated = %ld\n", al);

	for (m = 0; m < z; m++)
	{
		s = l->ob_item[m]->ob_type->tp_name;
		printf("Element %ld: %s\n", m, s);
		if (strcmp(s, "bytes") == 0)
			print_python_bytes(l->ob_item[m]);
		else if (strcmp(s, "float") == 0)
			print_python_float(l->ob_item[m]);
	}
}

/**
 * print_python_bytes - Prints basic info about Python.
 * @p: pointer.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t z, m;
	PyBytesObject *b = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "b") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  s: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", b->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		z = 10;
	else
		z = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", z);
	for (m = 0; m < z; m++)
	{
		printf("%02hhx", b->ob_sval[m]);
		if (m == (z - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Prints basic info about Python.
 * @p: pointer.
 */
void print_python_float(PyObject *p)
{
	char *bf = NULL;

	PyFloatObject *fl = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	bf = PyOS_double_to_string(fl->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", bf);
	PyMem_Free(bf);
}
