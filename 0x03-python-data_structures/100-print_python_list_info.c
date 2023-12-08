#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - prints the information about a Python list
 * @p: pointer to the python list
 */

void print_python_list_info(PyObject *p)
{
	ssize_t i, size = PyList_Size(p);
	PyListObject *obj = (PyListObject *)p;

	/* print the size of the python list */
	printf("[*] Size of the Python List = %ld\n", size);

	/* print the allocated memory of the python list */
	printf("[*] Allocated = %ld\n", obj->allocated);

	i = 0;
	while (i < size)
	{
		/* print the info about each element in the list */
		printf("Element %ld: %s\n", i,
		       Py_TYPE(obj->ob_item[i])->tp_name);
		i++;
	}
}
