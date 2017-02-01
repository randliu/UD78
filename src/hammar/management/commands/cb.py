#!/usr/bin/python
#coding=utf-8
from django.core.management.base import BaseCommand
from optparse import make_option

from hammar.combine_logic import list_combine,add_stock_to_combine,add_combine,report_combine,track_combine

#from hammar.models import Combine

import  string
"""
ud combine add one
ud combine
"""


class Command(BaseCommand):
	option_list = BaseCommand.option_list+(\
		make_option('-n','--name',dest="name",action='store',type='string',help='sh/sz/hk'),\
		make_option('-s','--add_stock_to_combine',default=False,action='store_true',help='days'),\
		make_option('-l','--list',dest="list",default=False,action='store_true',help=u'列表'),\
		make_option('-c','--code',dest="code",default=0,action='store',type='int',help=u'股票号码'),\
		make_option('-m','--market',dest="market",action='store',type='string',help='sh/sz/hk'),\

		make_option('-r','--report',dest="report",default=False,action='store_true',help='sh/sz/hk'),\
		make_option('-d','--day',dest="day",default=1,action='store',type='int',help=u'股票号码'),\

		make_option('-t','--track',dest="track",default=False,action='store_true',help='sh/sz/hk'),\
		make_option('--value',dest="value",default=1,action='store',type='int',help=u'股2票号码'),\

		)

	def handle(self, *args, **options):
		if options['list']:
			list_combine()
			return

		if options['name'] is not None:
			name = string.strip(options['name'])
			#first check if report
			if options['report']:
				day = options['day']
				report_combine(name,day)
				return

			if options['track']:
				value = options['value']
				track_combine(name,value)
				return


			if options['add_stock_to_combine'] is False:
				print options['name']
				c = add_combine(name)
				return
			else:
				market = options['market']
				code = options['code']
				add_stock_to_combine(stock_market=market,stock_code=code,combine_name=name)



