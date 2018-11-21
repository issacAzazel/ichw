"""currency.py: the calculation about currency.

__author__ = "Lin Xiaohan"
__pkuid__  = "1800011791"
__email__  = "linxiaohan@pku.edu.cn"
"""


from urllib.request import urlopen


def before_space(s):
    """
    get str before spaces
    """
    s_list=s.split()
    return(s_list[0])


def test_before_space():
    '''
    test!
    '''
    assert('0.8963'==before_space('0.8963 Euros'))


def after_space(s):
    """
    get str after spaces
    """
    s_list=s.split()
    return(s_list[1])


def test_after_space():
    '''
    test!
    '''
    assert('Euros'==after_space('0.8963 Euros'))


def first_inside_quotes(s):
    """
    get str first inside quotes
    """
    s_list=s.split('"')
    return(s_list[1])


def test_first_inside_quotes():
    """
    test!
    """
    assert('B C'==first_inside_quotes('A "B C" D "E F" G'))


def get_from(json):
    """
    get str first after from
    """
    s_list=json.split('"')
    for i in range(len(s_list)):
        if s_list[i] == 'from':
            return s_list[i+2]


def test_get_from():
    """
    test!
    """
    assert('2 United States Dollars'==get_from('{"from":"2 United States Dollars","to":"1.825936 Euros","success":true,"error":""}'))



def get_to(json):
    """
    get str first after to
    """
    s_list=json.split('"')
    for i in range(len(s_list)):
        if s_list[i] == 'to':
            return s_list[i+2]


def test_get_to():
    """
    test!
    """
    assert('1.825936 Euros'==get_to('{"from":"2 United States Dollars","to":"1.825936 Euros","success":true,"error":""}'))


def has_error(json):
    """
    valid or invalid
    """
    if 'success' in json:
        return True
    else:
        return False


def test_has_error():
    """
    test!
    """
    assert(True==has_error('{"from":"2 United States Dollars","to":"1.825936 Euros","success":true,"error":""}'))


def currency_response(currency_from, currency_to, amount_from):
    """
    return a JSON string that is a response to a currency query.
    """
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from+'&to='+currency_to+'&amt='+str(amount_from))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr


def test_currency_response():
    """
    test!
    """
    assert('{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, "error" : "" }'==currency_response('USD','EUR',2.5))


def iscurrency(currency):
    """
    whether this currency word is valid or not
    """
    json=currency_response(currency,currency,1)
    return(has_error(json))


def test_iscurrency():
    """
    test!
    """
    assert(True==iscurrency('USD'))


def exchange(currency_from, currency_to, amount_from):
    """
    return amount of currency received in the given exchange.
    """
    json=currency_response(currency_from, currency_to, amount_from)
    s=get_to(json)
    return(before_space(s))


def test_exchange():
    """
    test!
    """
    assert('2.1589225'==exchange('USD','EUR',2.5))


def testAll():
    """
    test all cases!
    """
    test_before_space()
    test_after_space()
    test_first_inside_quotes()
    test_get_from()
    test_get_to()
    test_has_error()
    test_currency_response()
    test_iscurrency()
    test_exchange()
    print("All tests passed")


testAll()


def main():
    """main module
    """
    print("请输入初始货币")
    currency_from=input()
    print("请输入要换算的货币")
    currency_to=input()
    print("请输入货币金额")
    amount_from=float(input())
    print(exchange(currency_from, currency_to, amount_from))


if __name__ == '__main__':
    main()
