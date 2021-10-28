import os
import xml.dom.minidom
import xml.etree.ElementTree as ET
from lxml import etree
import xml.etree.cElementTree as ET
from pprint import pprint


tree = ET.parse('test.xml')
root = tree.getroot()


def pretty_print_xml_given_root(root, output_xml):
    """
    Useful for when you are editing xml data on the fly
    """
    xml_string = xml.dom.minidom.parseString(ET.tostring(root)).toprettyxml()
    # remove the weird newline issue
    xml_string = os.linesep.join(
        [s for s in xml_string.splitlines() if s.strip()])
    with open(output_xml, "w") as file_out:
        file_out.write(xml_string)


def addNewBook(all_sub_elements):
    if len(all_sub_elements):
        Books = root.find("Books")
        Book = ET.SubElement(Books, 'Book')
        for subelement in all_sub_elements:
            new_element = ET.SubElement(Book, subelement.tag)
            new_element.text = subelement.text


# result = len(root.findall(".//*"))
# pprint(result)
# double_titles = []
for book in tree.findall('Books/Book'):
    counter = 0
    for children in book.findall(".//*"):
        if children.tag == 'quote-block':
            counter += 1
            if counter >= 2:
                all_sub_elements = []
                for subchild in children.findall(".//"):
                    print(
                        f'COUNTER:{counter} children:{book.attrib["id"]} subchild:{subchild.tag}')
                    all_sub_elements.append(subchild)
                addNewBook(all_sub_elements)
                book.remove(children)


pretty_print_xml_given_root(root, 'output.xml')
# tree.write('output.xml')
