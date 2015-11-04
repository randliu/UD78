#!/usr/bin/python 
#coding=utf-8 
from django.core.management.base import BaseCommand           
from hammar.main import track,track_index
from optparse import make_option

class Command(BaseCommand):
	option_list = BaseCommand.option_list+(\
		make_option('-m','--market',dest="market",action='store',type='string',help='sh/sz/hk'),\
		make_option('--value',dest="value",action='store',default=2,type='int',help='counted value'),\
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
				track(v=options['value'],market=options['market'])
			else:
				track(v=options['value'],code=options['code'],market=options['market'])
		else:
			track_index(v=options['value'])	
		
