#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <floatobject.h>
#include <string.h>

/**
 * print_python_list - print some basic infor about python lists
 * @p: pylistobject
 * Return: void or an error message if p is not a valid PyListObject
 */
void print_python_list(PyObject *p)
{
	int pyobj;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list"))
	{
		printf(" [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %lu\n", ((PyVarObject *)p)->ob_size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (pyobj = 0; pyobj < ((PyVarObject *)p)->ob_size; pyobj++)
	{
		printf("Element %d: %s\n", pyobj,
			((PyListObject *)p)->ob_item[pyobj]->ob_type->tp_name);
		if (!strcmp(((PyListObject *)p)->ob_item[pyobj]->ob_type->tp_name, "bytes"))
			print_python_bytes(((PyListObject *)p)->ob_item[pyobj]);
		else if (!strcmp(((PyListObject *)p)->ob_item[pyobj]->ob_type->tp_name, "float"))
			print_python_float(((PyListObject *)p)->ob_item[pyobj]);
	}
}

/**
 * print_python_bytes - print info about python bytes
 * @p: Python bytes object
 * Return: void or an error message
 */
void print_python_bytes(PyObject *p)
{
	size_t pyb, pylen, pyt;
	char *st8;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}
	pyt = ((PyVarObject *)p)->ob_size;
	st8 = ((PyBytesObject *)p)->ob_sval;
	pylen = pyt + 1 > 10 ? 10 : pyt + 1;
	printf(" pyt: %lu\n", pyt);
	printf(" trying string: %s\n", st8);
	printf(" first %lu bytes: ", pylen);
	for (pyb = 0; pyb < pylen; pyb++)
		printf("%02hhx%s", st8[pyb], pyb + 1 < pylen ? " " : "");
	printf("\n");
}

/**
 * print_python_float - print info about Python float objects
 * @p: python float object
 * Return: void or error message
 */
void print_python_float(PyObject *p)
{
	double pyfloat;

		setbuf(stdout, NULL);
		printf("[.] float object info\n");
		if (strcmp(p->ob_type->tp_name, "float"))
		{
			printf(" [ERROR] Invalid Float Object\n");
			return;
		}

	pyfloat = ((PyFloatObject *)p)->ob_fval;
		printf(" value: %s\n",
			PyOS_double_to_string(pyfloat, 'r', 0, Py_DTSF_ADD_DOT_0, NULL));
}
