# -*- coding: utf-8 -*-

import sys
import os
import timeit

from lxml import etree as ET

class Record(object):
	'''Klasse zur Darstellung von Records des arxiv-Datensatzes '''

	'''Namespaces im arxiv-Datensatz'''
	ns0 = 'http://www.openarchives.org/OAI/2.0/'
	ns1 = 'http://www.openarchives.org/OAI/2.0/oai_dc/'
	dc  = 'http://purl.org/dc/elements/1.1/'

	def __init__(self,record):
		self.record = record
		self.header = record.find('{%s}header' % (Record.ns0))
		self.metadata = record.find('{%s}metadata/{%s}dc' % (Record.ns0,Record.ns1))

	def get_title(self):
		''' Titel einer Publikation'''
		return self.metadata.find('{%s}title' % Record.dc).text

	def get_authors(self):
		'''Authoren einer Publikation'''
		authors = list()
		for s in self.metadata.findall('{%s}creator' % Record.dc):
			authors.append(s.text)

		return authors

	def get_identifier(self):
		''' Identifier on arxiv.org'''
		return self.header.find('{%s}identifier' % Record.ns0).text

	def get_subjects(self):
		''' Returns subjects in metadata'''
		subjects = list()
		for s in self.metadata.findall('{%s}subject' % Record.dc):
			subjects.append(s.text)

		return subjects

	def get_setSpecs(self):
		''' Returns SetSpecs in header'''
		setSpecs = list()
		for s in self.header.findall('{%s}setSpec' % Record.ns0):
			setSpecs.append(s.text)

		return setSpecs

	def get_description(self):
		''' Beschreibung zu einer Publikationen'''
		return self.metadata.find('{%s}description' % Record.dc).text

	def get_date(self):
		'''Erstes Datum(Veröffentlichung) einer Publikation'''
		return self.metadata.find('{%s}date' % Record.dc).text

	def info(self):
		'''Ausgabe aller Informationen einer Publikation'''
		print 'title:', self.get_title()
		print 'setSpecs:', self.get_setSpecs()
		print 'identifier:', self.get_identifier()
		print 'desc:', self.get_description()
		print 'Date:', self.get_date()
		print 'Subjects:', self.get_subjects()
		print 'Authors:', self.get_authors()

class ArxivParser(object):
	def __init__(self, xmlFile):
		# iteratives Parsen über die Records mit default-Event 'end'
		self.context = ET.iterparse(
				os.path.abspath(xmlFile), 
				events=('end',), 
				tag='{%s}record' % Record.ns0)

		self.count = 0;
	
	def iter_records(self, handle):
		result = list()
		for event, elem in self.context:
			# wenn das End-Tag eines Records erreicht wurde
			# und der Record sowohl header, als auch metadata hat
			if event == 'end' and len(list(elem)) == 2:
				self.count += 1
				r = Record(elem)
				result.append(handle(r))
				# Referenz auf aktuelles Element entfernen
				elem.clear()
				# Referenzen auf Elternknoten entfernen
				while elem.getprevious() is not None:
					del elem.getparent()[0]
		return result

def analyze_len_of_setSpecs(parser):
	len_of_setSpec = lambda x: len(x.get_setSpecs())
	
	result =  parser.iter_records(len_of_setSpec)

	for r in set(result):
		print r, result.count(r)

def analyze_dist_of_setSpecs(parser):
	get_setSpecs = lambda x: x.get_setSpecs()
	# flatten list, because the subjects per paper are in lists
	result = sum(parser.iter_records(get_setSpecs),[])

	for r in set(result):
		print r, result.count(r)


def main(args):
	if len(args) != 1:
		print 'Usage: python arxivParser.py <arxiv dataset>'
		exit()


	p = ArxivParser(args[0])	
	
	# Anzahl der Anzahl der setSpecs pro Publikation
	#analyze_len_of_setSpecs(p)

	analyze_dist_of_setSpecs(p)

	
if __name__ == "__main__":
	#main(sys.argv[1:])
	t = timeit.Timer("main(args)", "from __main__ import main; args=%r" % sys.argv[1:])
	print  t.timeit(number=1)
