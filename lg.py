import bottle
import domain


# Looking Glass - V. 0.1

@bottle.route('/dig', method='GET')
def lg():
    if bottle.request.GET.get('save', '').strip():
        query_domain = bottle.request.GET.get('domain')
        query_dns = bottle.request.GET.get('dns')
        query_type = bottle.request.GET.get('query_type')
        q = domain.Dig(query_domain, query_type, query_dns)
        result = q.query()
        output = bottle.template('www/domain_result', d_result=result)
        return output
    else:
        return bottle.template('www/index_dig')


@bottle.route('/ping', method='GET')
def ping():
    """ Index PING Page """
    if bottle.request.GET.get('save', '').strip():
        query_address = bottle.request.GET.get('address')
        query_ping = domain.Ping(query_address)
        result = query_ping.do()
        output = bottle.template('www/ping_result', d_result=result)
        return output
    else:
        return bottle.template('www/index_ping')


@bottle.route('/traceroute', method='GET')
def traceroute():
    if bottle.request.GET.get('save', '').strip():
        query_address = bottle.request.GET.get('address')
        query_trace = domain.Traceroute(query_address)
        result = query_trace.trace()
        output = bottle.template('www/traceroute_result', d_result=result)
        return output
    else:
        return bottle.template('www/index_traceroute')


@bottle.route('/nmap', method='GET')
def nmap():
    if bottle.request.GET.get('save', '').strip():
        nmap_address = bottle.request.GET.get('address')
        nmap_run = domain.NMap(nmap_address)
        result = nmap_run.run()
        output = bottle.template('www/nmap_result', d_result=result)
        return output
    else:
        return bottle.template('www/index_nmap')


@bottle.route('/')
def default():
    return bottle.static_file('default.html', root='www/static')


bottle.run(host='localhost', port=8080)
