from decimal import Decimal


def pluralize(s: str, u: int) -> str: return f'{s}s' if u >= 2 else s


def to_readable_size(bytes: Decimal) -> str:
    KB = Decimal(1024)
    MB = Decimal(KB ** 2)  # 1,048,576
    GB = Decimal(KB ** 3)  # 1,073,741,824
    TB = Decimal(KB ** 4)  # 1,099,511,627,776
    PB = Decimal(KB ** 5)  # 1,125,899,906,842,624
    EB = Decimal(KB ** 6)  # 1.152921504606847e+18
    ZB = Decimal(KB ** 7)  # 1.1805916207174113e+21
    YB = Decimal(KB ** 8)  # 1.2089258196146292e+24

    if bytes < KB:
        return '{0:.2f} {1}'.format(bytes, pluralize('byte', bytes))
    elif KB <= bytes < MB:
        return '{0:.2f} KB'.format(bytes/KB)
    elif MB <= bytes < GB:
        return '{0:.2f} MB'.format(bytes/MB)
    elif GB <= bytes < TB:
        return '{0:.2f} GB'.format(bytes/GB)
    elif TB <= bytes < PB:
        return '{0:.2f} TB'.format(bytes/TB)
    elif PB <= bytes < EB:
        return '{0:.2f} PB'.format(bytes/PB)
    elif EB <= bytes < ZB:
        return '{0:.2f} EB'.format(bytes/EB)
    elif ZB <= bytes < YB:
        return '{0:.2f} ZB'.format(bytes/ZB)
    else:
        return '{0:.2f} YB'.format(bytes/YB)


def to_readable_time(seconds: Decimal) -> str:
    seconds = Decimal(seconds)

    MIN = Decimal(60)
    HOU = Decimal(MIN * 60)    # 3600
    DAY = Decimal(HOU * 24)    # 86400
    MON = Decimal(DAY * 30)    # 2592000
    YEA = Decimal(MON * 12)    # 31104000
    DEC = Decimal(YEA * 10)    # 311040000
    CEN = Decimal(DEC * 10)    # 3110400000
    MIL = Decimal(CEN * 10)    # 31104000000
    AGE = Decimal(MIL * 1000)  # 31104000000000
    EPO = Decimal(AGE * 10)    # 311040000000000
    ERA = Decimal(EPO * 10)    # 3110400000000000
    EON = Decimal(ERA * 5)     # 15552000000000000

    if seconds <= MIN:
        return '{0:.2f} {1}'.format(seconds, pluralize('second', seconds))
    elif seconds <= HOU:
        fmt = seconds/MIN
        return '{0:.2f} {1}'.format(fmt, pluralize('minute', seconds/60))
    elif seconds <= DAY:
        fmt = seconds/HOU
        return '{0:.2f} {1}'.format(fmt, pluralize('hour', fmt))
    elif seconds <= MON:
        fmt = seconds/DAY
        return '{0:.2f} {1}'.format(fmt, pluralize('day', fmt))
    elif seconds <= YEA:
        fmt = seconds/MON
        return '{0:.2f} {1}'.format(fmt, pluralize('month', fmt))
    elif seconds <= DEC:
        fmt = seconds/YEA
        return '{0:.2f} {1}'.format(fmt, pluralize('year', fmt))
    elif seconds <= CEN:
        fmt = seconds/DEC
        return '{0:.2f} {1}'.format(fmt, pluralize('decade', fmt))
    elif seconds <= MIL:
        fmt = seconds/CEN
        return '{0:.2f} {1}'.format(fmt, 'century' if fmt < 2 else 'centuries')
    elif seconds <= AGE:
        fmt = seconds/MIL
        return '{0:.2f} {1}'.format(fmt, 'millenium' if fmt < 2 else 'millenia')
    elif seconds <= EPO:
        fmt = seconds/AGE
        return '{0:.2f} {1}'.format(fmt, pluralize('epoch', fmt))
    elif seconds <= ERA:
        fmt = seconds/EPO
        return '{0:.2f} {1}'.format(fmt, pluralize('era', fmt))
    else:
        fmt = seconds/EON
        return '{0:.2f} {1}'.format(fmt, pluralize('eon', fmt))
