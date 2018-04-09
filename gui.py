import easygui as eg
from functions import merge

if __name__ == '__main__':
    input_files = eg.fileopenbox('Open', filetypes='*.xml', multiple=True)
    if not input_files:
        eg.msgbox('Please select XMLs.')
        exit()
    output_file = eg.filesavebox('Save', filetypes='*.xml', default='output.xml')
    if not output_file:
        eg.msgbox('Please select save path.')
        exit()
    merge(input_files, output_file)
    eg.msgbox('Files merged.')