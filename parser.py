#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import gettext
import re

# Начальные установки для gettext
gettext.bindtextdomain('depvotingparser', localedir='./locale')
gettext.textdomain('depvotingparser')
_ = gettext.gettext

# Проверка параметров командной строки
if len(sys.argv) < 2:
  print _('No input file with report form! Usage: ./parser.py [filename]')
  raise SystemExit

# Читаем данные из файла
print >> sys.stderr, _('Opening file: %s') % sys.argv[1]
try:
  f = open(sys.argv[1], 'r')
except IOError:
  print >> sys.stderr, _('Error open file: %s') % sys.argv[1]
  raise SystemExit
else:
  indata = f.read()
  f.close()
  

# Парсим файл
resulttable = {}
fractionNameRE = re.compile('(Фракция[^\n]+)')
depResultRE = re.compile('\d+\t([\+|\*|\-])\t(.+?)\t', re.DOTALL)

startpos = 0
endpos = 0
while True:
  endpos = indata.find('*\tФракция', startpos)  
  if endpos == -1:
    seg = indata[startpos:]
  else:
    seg = indata[startpos:endpos]  

  try:
    fractionName = fractionNameRE.search(seg).group(1).strip()
  except:
    fractionName = None
    
  if fractionName:
    depres = depResultRE.findall(seg)
    if fractionName not in resulttable:
      resulttable[fractionName] = []
    for i in depres:
      resulttable[fractionName].append({'name': i[1].strip(),'vote': i[0],})
  
  startpos = endpos + 1  
  if endpos == -1: break
  
# Сортируем
for fraction in resulttable:
  resulttable[fraction].sort(key = lambda tup: tup['name'])

# Выводим итоговую таблицу в HTML
for fraction in resulttable:
  print '<table><tr><td colspan="2">%s</td></tr>' % fraction
  for dep in resulttable[fraction]:
    vote = dep['vote'].replace('*', _('Not Voting')).replace('-', _('Nay')).replace('+', _('Yea'))    
    print '<tr><td>%s</td><td>%s</td></tr>' % (dep['name'], vote)
  print '</table><br />'
