from bs4 import BeautifulSoup

file = BeautifulSoup(open('objects.xml'),'lxml-xml') 

# print(file.prettify())

takeaways = file.findAll('row')

for eachtakeaway in takeaways:
	# print eachtakeaway
	object_identifier = eachtakeaway('id')
	object_name = eachtakeaway('name')
	object_type = eachtakeaway('type')
	object_external_reference = eachtakeaway('external_reference')
	object_metadata = eachtakeaway('metadata')
	print object_identifier.get_text()