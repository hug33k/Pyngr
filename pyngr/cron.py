_values_ranges = [(0, 59), (0, 23), (1, 31), (1, 12), (1, 7), None]


def _is_interval(item):
    parts = item.split("/")
    return len(parts) is 2 and parts[0] is "*" and parts[1].isdigit()


def _get_value(item):
    if _is_interval(item):
        parts = item.split("/")
        return int(parts[1])
    if item.isdigit():
        return int(item)
    return item


def _is_valid_format(item):
    if _is_interval(item):
        return True
    return item is "*" or item.isdigit()


def _is_in_range(item, value_range):
    if value_range is None or item is "*":
        return True
    value = _get_value(item)
    return value in range(value_range[0], (value_range[1] + 1))


def _validate_rule(rule):
    rules = rule.split(" ")
    if len(rules) is not 6:
        raise SyntaxError("Invalid cron rule")
    for sub_rule, value_range in zip(rules, _values_ranges):
        if not _is_valid_format(sub_rule):
            raise SyntaxError("{item} is not a valid format".format(item=sub_rule))
        if not _is_in_range(sub_rule, value_range):
            raise SyntaxError("{item} is not in range ({range_min} - {range_max})"
                              .format(item=sub_rule, range_min=value_range[0], range_max=value_range[1]))


def add_to_scheduler(rule, uuid, scheduler, job):
    _validate_rule(rule)
    scheduler.every(1).seconds.do(job).tag(uuid)
