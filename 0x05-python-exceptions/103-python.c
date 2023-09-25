#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>
/**
 * print_python_bytes - print python things
 * @p: pointer 
 */
void print_python_bytes(PyObject *p)
{
	size_t y, m;
	char *ptr;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (PyBytes_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	ptr = ((PyBytesObject *)(p))->ob_sval, y = PyBytes_Size(p);
	printf("  size: %ld\n  trying string: %s\n", y, ptr);
	y >= 10 ? y = 10 : y++;
	printf("  first %ld bytes: ", y);
	for (m = 0; m < y - 1; m++)
		printf("%02hhx ", ptr[m]);
	printf("%02hhx\n", ptr[m]);
}
/**
 * print_python_float - print python things
 * @p: pointer
 */
void print_python_float(PyObject *p)
{
	char *ptr;
	double k;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (PyFloat_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	k = ((PyFloatObject *)(p))->ob_fval;
	ptr = PyOS_double_to_string(k, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", ptr);
}
/**
 * print_python_list - print python things
 * @p: pointer
 */
void print_python_list(PyObject *p)
{
	size_t o, size, m;
	const char *s;
	PyListObject *l;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (PyList_Check(p) == 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	l = (PyListObject *)p;
	size = PyList_GET_SIZE(p);
	o = list->allocated;
	printf("[*] Size of the Python List = %ld\n[*] Allocated = %li\n", size, o);
	for (m = 0; m < size; m++)
	{
		t = (list->ob_item[m])->ob_type->tp_name;
		printf("Element %li: %s\n", m, s);
		!strcmp(s, "bytes") ? print_python_bytes(list->ob_item[m]) : (void)s;
		!strcmp(s, "float") ? print_python_float(list->ob_item[m]) : (void)s;
	}
}
