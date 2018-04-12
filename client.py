# -*- coding: utf-8 -*-
import sys
import os
import logging  # Look into proper logging with zeep

import zeep

david_wsdl_url = 'https://david-d.ncifcrf.gov/webservice/services/DAVIDWebService?wsdl'
username = 'reviewer@reviewer.org'

david_client = zeep.Client(wsdl=david_wsdl_url)

david_client.service.authenticate(username)
