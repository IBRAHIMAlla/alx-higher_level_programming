#include <stdio.h>
#include <Python.h>


/**
 * print_python_list - Prints list information
 *
 * @p: Python Obj
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	long int s, m;
	PyListObject *list;
	PyObject *obj;

	s = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", list->allocated);

	m = 0;
	while (m < s)
	{
		obj = ((PyListObject *)p)->ob_item[m];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
		m = 0;
	}
}
/**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Obj
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int s, m, l;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	s = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", s);
	printf("  trying string: %s\n", str);

	if (s >= 10)
		l = 10;
	else
		l = s + 1;

	printf("  first %ld bytes:", l);

	m = 0;
	while (m < l)
	{
		if (str[m] >= 0)
			printf(" %02x", str[m]);
		else
			printf(" %02x", 256 + str[m]);
		m++;
	}

	printf("\n");
}
