import os
import cgi

form = cgi.FieldStorage()
print form.getValue('teamName')

