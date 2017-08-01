from bs4 import BeautifulSoup

infile = open("objects.xml","r")
contents = infile.read()
soup = BeautifulSoup(contents,'xml')

objects_identifiers = soup.find_all('id')
objects_names = soup.find_all('name')
objects_type = soup.find_all('type')
objects_external_reference = soup.find_all('external_reference')
objects_metadata = soup.find_all('metadata')


comp_objects_identifiers=0
comp_objects_names =0
comp_objects_type =0
comp_objects_external_reference =0
comp_objects_metadata =0

for i in range(0, len(objects_identifiers)):
	len_objects_identifiers = len(objects_identifiers[i].get_text())
	if len_objects_identifiers>comp_objects_identifiers:
		comp_objects_identifiers=len_objects_identifiers

	len_objects_names = len(objects_names[i].get_text())
	if len_objects_names>comp_objects_names:
		comp_objects_names=len_objects_names

	len_objects_type = len(objects_type[i].get_text())

	if len_objects_type>comp_objects_type:
		comp_objects_type= len_objects_type

	len_objects_external_reference = len(objects_external_reference[i].get_text())

	if len_objects_external_reference>comp_objects_external_reference:
		comp_objects_external_reference= len_objects_external_reference

	len_objects_metadata = len(objects_metadata[i].get_text())

	if len_objects_metadata>comp_objects_metadata:
		comp_objects_metadata= len_objects_metadata

print "La logitud maxima del campo id es: ", comp_objects_identifiers
print "La logitud maxima del campo name es: ", comp_objects_names 
print "La logitud maxima del campo type es: ", comp_objects_type 
print "La logitud maxima del campo external reference es: ", comp_objects_external_reference 
print "La logitud maxima del campo metadata es: ", comp_objects_metadata 