#!/usr/bin/python 
#coding=utf-8 
from django.core.management.base import BaseCommand           
from hammar.main import report,report_index
from optparse import make_option

class Command(BaseCommand):
	option_list = BaseCommand.option_list+(\
		make_option('-m','--market',dest="market",action='store',type='string',help='sh/sz/hk'),\
		make_option('-d','--day',dest="day",default=3,action='store',type='int',help='days'),\
		make_option('-i','--index',dest="index",default=False,action='store_true',help=u'各个市场的指数'),\
		make_option('-c','--code',dest="code",default=0,action='store',type='int',help=u'股票号码'),\
		)
	
	def handle(self, *args, **options):
		#print "test %s"%str(args)
		pass
		#print str(options)
		#print options['market']
		if not options['index']:
			if options['code'] == 0:
				report(day=options['day'],market=options['market'])
			else:
				report(day=options['day'],code=options['code'],market=options['market'])
		else:
			report_index(day=options['day'])	
		
