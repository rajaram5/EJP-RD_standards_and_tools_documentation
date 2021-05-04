import os

INPUT_EXCEL_FILE_NAME = os.environ['INPUT_EXCEL_FILE_NAME']

INPUT_EXCEL_FILE = "input/" + INPUT_EXCEL_FILE_NAME
DATA_SHEET_NAME = "deliverable+inventory+listsALL"
HEADER_START_ROW = 2
STANDARD_NAME_COL = "Name"
FINDABLITY_FLAG_COL = "Findable"
ACCESSIBLITY_FLAG_COL = "Accessible"
INTEROPERABLITY_FLAG_COL = "Interoperable"
REUSABLITY_FLAG_COL = "Reusable"
MACHINES_FLAG_COL = "for Machines"
HUMANS_FLAG_COL = "for Humans"
FOR_CATALOGUES_FLAG_COL = "Catalogue"
FOR_DATABASE_FLAG_COL = "Database"
FOR_RECORD_FLAG_COL = "Record"
FLAG_STRING = "x"