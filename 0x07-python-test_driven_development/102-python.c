#include "Python.h"

/**
 * print_python_string - prints information about python strings.
 * @p: a PyObject string object
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t len;

	fflush(stdout);

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("[Error] invalid string object\n");
i		return;
	}
i	len = PyUnicode_GET_LENGTH(p);
	printf(" type: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ?
			"compact ascii" : "compact unicode");
	printf(" length: %ld\n", len);
	printf(" value: %ls\n", PyUnicode_AsWideCharString(p, &len));
}
