import apachelog, sys
    
format = r'%h %l %u %t \"%r\" %>s %O \"%{Referer}i\" \"%{User-Agent}i\" %D'

def collect_data(data):
    #print data
    host = data['%h']
    request = data['%r']
    output_bytes = int(data['%O'])
    output_time = int(data['%D']) # in microseconds
    print host + " " + request + " " + str(1000000*output_bytes/output_time/1024) + " KiloByte/s"
    
p = apachelog.parser(format)
while True:
    try:
        line = sys.stdin.readline()
        if not line: break
        data = p.parse(line)
        collect_data(data)
    except apachelog.ApacheLogParserError:
        pass
    except KeyboardInterrupt:
        sys.exit(0)
