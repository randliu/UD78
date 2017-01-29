from models import Stock,Combine,StockTrait
from hammar.main import report,track


def list_combine():
    lst_combine = Combine.objects.all()

    for c in lst_combine:
        print "Name:    %s"%c.name
        lst_trait = c.stocktrait_set.all()
        for trait in lst_trait:
            s= trait.stock
            print " %d  %s  %s"%(s.code,s.name,s.market)


def add_stock_to_combine(stock_code,stock_market,combine_name):
    combine = Combine.objects.get(name = combine_name)

    if combine is None:
        print " no such combine"
        return

    s = Stock.objects.get(code = stock_code,market= stock_market)

    if s is None:
        print "no such stock"
        return

    lst_t = combine.stocktrait_set.all()

    for t in lst_t:
        if t.stock == s:
            print "stock already exist in combine"
            return

    #new stock in combine
    trait = StockTrait()
    trait.stock = s
    trait.combine = combine
    trait.save()


def add_combine(name):
    lst_combine = Combine.objects.all()

    for c in lst_combine:
        if c.name == name:
            print "combine already existed"
            return
    c = Combine(name = name)
    c.save()

def report_combine(name,day):
    combine = Combine.objects.get(name = name)

    if combine is None:
        print " no such combine"
        return

    lst_trait = combine.stocktrait_set.all()
    for trait in lst_trait:
        s= trait.stock

        report(day=day,code=s.code,market=s.market)

def track_combine(name,value):
    combine = Combine.objects.get(name = name)

    if combine is None:
        print " no such combine"
        return

    lst_trait = combine.stocktrait_set.all()
    for trait in lst_trait:
        s= trait.stock
        track(v=value,code=s.code,market=s.market)
