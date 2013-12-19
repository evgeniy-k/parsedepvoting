#!/bin/bash
rm -f locale/ru/LC_MESSAGES/*.mo
msgfmt locale/ru/depvotingparser.po
mv messages.mo locale/ru/LC_MESSAGES/depvotingparser.mo
