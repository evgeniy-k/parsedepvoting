#!/bin/bash
xgettext --language=Python --keyword=_ \
--from-code=UTF-8 \
--output=locale/depvotingparser.pot --package-name=DepVotingParser --package-version=1.0 \
parser.py
rm -f locale/ru/*.po
msginit --input=locale/depvotingparser.pot --locale=ru_RU.UTF-8 \
--output-file=locale/ru/depvotingparser.po
