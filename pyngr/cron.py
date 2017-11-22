#   * * * * *
#   ^ ^ ^ ^ ^
#   | | | | |
#   | | | | +-- Day of the month    ( Range: 1-31 )
#   | | | +---- Day of the week     ( Range: 1-7  )
#   | | +------ Hour                ( Range: 0-23 )
#   | +-------- Minute              ( Range: 0-59 )
#   +---------- Second              ( Range: 0-59 )
#
#   Valid inputs : Number, '*', '-', '/', ','
#       Example : '10 * 5-50 */15 1,2,3 * *'
#
#   Invalid inputs : '*/0', 'number/number', 'anything/*'
#
#   Priorities : ',' => '-' => '/'
#       Example : '1,2,3,5-10/2,15' => '1,2,3,5,7,9,15'

_values_ranges = [(0, 59), (0, 59), (0, 23), (1, 31), (1, 12), (1, 7), None]


def _is_valid_value(item):
    return item is "*" or item.isdigit() or "-" in item or "," in item


def _has_interval(item):
    parts = _get_interval(item)
    return len(parts) is 2 and _is_valid_value(parts[0]) and _is_valid_value(parts[1])


def _get_interval(item):
    return item.split("/")


def _has_range(item):
    parts = _get_range(item)
    return len(parts) is 2 and _is_valid_value(parts[0]) and _is_valid_value(parts[1])


def _get_range(item):
    return item.split("-")


def _has_list(item):
    parts = _get_list(item)
    if len(parts) < 2:
        return False
    for part in parts:
        if not _is_valid_value(part):
            return False
    return True


def _get_list(item):
    return item.split(",")


def _is_in_range(item, value_range, wildcard_allowed=True):
    if value_range is None or (item is "*" and wildcard_allowed):
        return
    if not _is_valid_value(item):
        raise SyntaxError("{item} is not valid"
                          .format(item=item))
    if not (int(item) in range(value_range[0], (value_range[1] + 1))):
        raise SyntaxError("{item} is not in range ({range_min} - {range_max})"
                          .format(item=item, range_min=value_range[0], range_max=value_range[1]))


def _is_valid_format(item, value_range):
    interval_inside = False
    base_value = item
    if _has_interval(item):
        items = _get_interval(item)
        _is_in_range(items[1], value_range, False)
        item = items[0]
        interval_inside = True
    if _has_range(item):
        items = _get_range(item)
        for value in items:
            _is_in_range(value, value_range, False)
        if int(items[0]) > int(items[1]):
            raise SyntaxError("Beginning of range cannot be greater than the end. {start} >= {end}"
                              .format(start=items[0], end=items[1]))
    elif _has_list(item):
        if interval_inside:
            raise SyntaxError("Interval cannot be used with list. {value}"
                              .format(value=base_value))
        items = _get_list(item)
        for value in items:
            _is_in_range(value, value_range, False)
    else:
        _is_in_range(item, value_range)
    return True


def validate_rule(rule):
    rules = rule.split(" ")
    if len(rules) is not 7:
        raise SyntaxError("Invalid cron rule")
    for sub_rule, value_range in zip(rules, _values_ranges):
        if not _is_valid_format(sub_rule, value_range):
            raise SyntaxError("{item} is not a valid format".format(item=sub_rule))


def add_to_scheduler(website, scheduler, job):
    validate_rule(website.rule)
    scheduler.every(1).seconds.do(job, website=website).tag(website.uuid)
