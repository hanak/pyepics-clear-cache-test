import epics

# Stress-test on shutdown when clear_cache is in use.
#
# This test assumes an IOC which provides following PVs:
# * beacon:X:delay: record AI
# * beacon:X:value: record AI: Increase after beacon:X:delay seconds.
# where X in [1, 10]. 
#
def pv_name(beacon, name):
    return f'beacon:{beacon}:{name}'


def clear_cache():
    # Additional cleanup which prevent SIGSEGV
    #for chid, _ in list(epics.ca._chid_cache.items()):
    #    epics.ca.clear_channel(chid)
    epics.ca.clear_cache()


def loop(num_sources):
    clear_cache()
    for id in range(1, num_sources + 1):
        value = epics.caget(pv_name(id, 'value'))
        if value is None:
            print(f'Source {id} offline')


def test(num_sources, retries):
    while retries > 0:
        loop(num_sources)
        retries = retries - 1
    print()


def setup(num_sources):
    delay = epics.caget(pv_name(1, 'delay'))
    assert delay is not None, \
        'IOC is not running.'
    for id in range(1, num_sources + 1):
        epics.caput(pv_name(id, 'delay'), 0.1, wait=True)


if __name__ == '__main__':
    num_sources = 10
    retries = 10
    setup(num_sources)
    test(num_sources, retries)

