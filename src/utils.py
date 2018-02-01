import xlsxwriter
import os

symbol_tags = {'$', '\'\'', '(', ')', ',', '--', '.', ':', '``', 'POS'}


def get_word_normal_form(word, tag):
	lower_cased = word.lower()
	# if tag in ['NNPS', 'NNS']:  # NNPS: noun, proper, plural, NNS: noun, common, plural
	# 	if len(word) < 2:
	# 		return lower_cased
	# 	if word[-2] == 'e' and word[-1] == 's':
	# 		if len(word) > 4 and word[-3] == word[-4]:  # processes -> proces_, gasses -> gas
	# 			return lower_cased[:-3]
	# 		return lower_cased[:-2]
	# 	return lower_cased
	return lower_cased


def is_word(word, tag):
	if tag in symbol_tags:
		return False
	return True


def write_xlsx_file(filename, data=None):
	directory = os.path.dirname(filename)
	if directory != '' and not os.path.exists(directory):
		os.makedirs(directory)
	workbook = xlsxwriter.Workbook(filename)
	worksheet = workbook.add_worksheet("Sheet1")
	row_count = 0
	for row in data:
		cell_count = 0
		for cell in row:
			worksheet.write(row_count, cell_count, cell)
			cell_count += 1
		row_count += 1
	workbook.close()


def clean_the(txt):
	text = []
	for t in txt:
		if t == 'the' or t == 'a':
			continue
		text.append(t)
	return text
