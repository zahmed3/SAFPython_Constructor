import csv
import os
import xml.etree.ElementTree as ET
import os.path
import shutil
from interface_functions import *
import gui as gui

#Sets the starting value for saf_folder_list.
saf_folder_list = []

#This function was adapted from PySAF and altered.
#Link to PySAF's repository: https://github.com/cstarcher/pysaf
#This function creates a new directory for each of the DSpace records.
def new_dir(saf_dir, row_num):
    os.makedirs(os.path.join(saf_dir, ('item_{}'.format(row_num))))

#This function was adapted from PySAF and altered.
#Link to PySAF's repository: https://github.com/cstarcher/pysaf
#This function shifts the current directory being worked to the newly created directory.
def change_dir(saf_dir, row_num):
    os.chdir(os.path.join(saf_dir, ('item_{}'.format(row_num))))

#This function was adapted from PySAF and altered.
#Link to PySAF's repository: https://github.com/cstarcher/pysaf
#This function writes the file names to the 'contents' file and also copies the files to the current directory.
def write_contents_file(data):
    with open('contents', 'a', encoding='utf-8') as contents_file:
        for csv_file_name in data.split('||'):
            contents_file.write('{}' '\t' 'BUNDLE:ORIGINAL' '\n'.format(csv_file_name))
            for dirpath, dirnames, filenames in os.walk(os.path.dirname(gui.selected_file)):
                for fname in filenames:
                    if csv_file_name == fname:
                        shutil.copy2(os.path.join(dirpath, fname), '.')

#This function was adapted from PySAF and altered.
#Link to PySAF's repository: https://github.com/cstarcher/pysaf
#This function writes metadata to the 'dublin_core' file.
def write_dc_metadata(header_split, data_split):
    for value in data_split:
        dc_value = ET.Element('dcvalue')
        dc_value.attrib['element'] = header_split[1]
        if len(header_split) == 3:
            dc_value.attrib['qualifier'] = header_split[2]
        dc_value.text = value
        if os.path.isfile('dublin_core.xml'):
            with open('dublin_core.xml', 'a', encoding='utf-8') as dc_file:
                dc_file.write('  {}' '\n'.format(
                    str(ET.tostring(dc_value, encoding='utf-8'), 'utf-8')))
        else:
            with open('dublin_core.xml', 'w', encoding='utf-8') as dc_file:
                dc_file.write('<?xml version="1.0" encoding="UTF-8"?>' '\n')
                dc_file.write('<dublin_core>' '\n')
                dc_file.write('  {}' '\n'.format(
                    str(ET.tostring(dc_value, encoding='utf-8'), 'utf-8')))

#This function was adapted from PySAF and altered.
#Link to PySAF's repository: https://github.com/cstarcher/pysaf
#This function writes metadata to schema files that are not written into 'dublin_core' files.
def write_schema_metadata(schema_file, header_split, data_split, schema):
    for value in data_split:
        dc_value = ET.Element('dcvalue')
        dc_value.attrib['element'] = header_split[1]
        if len(header_split) == 3:
            dc_value.attrib['qualifier'] = header_split[2]
        dc_value.text = value
        if os.path.isfile(schema_file):
            with open(schema_file, 'a', encoding='utf-8') as dc_file:
                dc_file.write('  {}' '\n'.format(
                    str(ET.tostring(dc_value, encoding='utf-8'), 'utf-8')))
        else:
            with open(schema_file, 'a', encoding='utf-8') as dc_file:
                dc_file.write('<?xml version="1.0" encoding="UTF-8"?>' '\n')
                dc_file.write('<dublin_core schema="{}">' '\n'.format(schema))
                dc_file.write('  {}' '\n'.format(
                    str(ET.tostring(dc_value, encoding='utf-8'), 'utf-8')))

#This function was adapted from PySAF and altered.
#Link to PySAF's repository: https://github.com/cstarcher/pysaf
#This function adds closing tags to the end of the xml files.
def write_closing_tag():
    for file_name in os.listdir('.'):
        if file_name.endswith('xml'):
            with open(file_name, 'a', encoding='utf-8') as dc_file:
                dc_file.write('</dublin_core>' '\n')

#This function was adapted from PySAF and altered.
#Link to PySAF's repository: https://github.com/cstarcher/pysaf
#This function writes CSV metadata to the appropriate schema files.
def create_files(saf_dir, row_num, headers, row):
    new_dir(saf_dir, row_num)
    change_dir(saf_dir, row_num)
    for header, data in zip(headers, row):
        header_split = header.split('.')
        schema = header_split[0]
        data_split = data.split('||')
        schema_file = 'metadata_{}.xml'.format(header_split[0])
        if data:
            if header_split[0] == 'filename':
                write_contents_file(data)
            elif header_split[0] == 'dc':
                write_dc_metadata(header_split, data_split)
            else:
                write_schema_metadata(schema_file,
                                           header_split,
                                           data_split,
                                           schema)
    write_closing_tag()

#This function was adapted from PySAF and altered.
#Link to PySAF's repository: https://github.com/cstarcher/pysaf
#This function runs the SAF operation when called.
def open_csv():
    saf_folder_name = 'SimpleArchiveFormat'
    saf_folder_list.append(saf_folder_name)
    saf_dir = os.path.join(gui.selected_folder, saf_folder_name)
    with open(gui.selected_file, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader)
        row_num = 1
        for row in reader:
            create_files(saf_dir, row_num, headers, row)
            row_num += 1