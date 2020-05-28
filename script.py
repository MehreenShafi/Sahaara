from mdutils.mdutils import MdUtils
from mdutils import Html
""" import gspread
from oauth2client.service_account import ServiceAccountCredentials
from mdutils.mdutils import MdUtils
from mdutils import Html

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('test-project_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("test-data").sheet1

# Extract and print all of the values
records = sheet.get_all_records()
print(records[0])
 """

mdFile = MdUtils(file_name='Employees.md', title='Sahaara')

mdFile.new_header(level=1, title='Sahaara - A Database for Disabled Community Employees')  # style is set 'atx' format by default.

mdFile.new_paragraph("This is a directory for potential employees looking for employments.")
text_list = ['Name', 'Skills', 'Past Experience', 'Person 1', 'skills', 'XYZ', 'Person 2', 'skills 2', 'ABC']
table = mdFile.new_table(columns=3, rows=3, text=text_list, text_align='center')

mdFile.create_md_file()