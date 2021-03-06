import uuid
from . import cron


class Website(object):

    defaultValues = {
        "credentials": None,
        "rule": "* * * * * * *"
    }

    def __init__(self, url,
                 credentials=defaultValues["credentials"],
                 rule=defaultValues["rule"]):
        self.url = url
        self.credentials = credentials
        self.rule = rule
        self.uuid = uuid.uuid1()
        self.hook = None

    def __str__(self):
        return """Site {uuid}
        URL : {url}
        Credentials : {credentials}
        Rule : {rule}""".format(
            uuid=self.uuid,
            url=self.url,
            credentials=self.credentials,
            rule=self.rule
        )

    def __eq__(self, other):
        return (self.url == other.url and
                self.credentials == other.credentials and
                self.rule == other.rule and
                self.hook == other.hook)

    def add_to_scheduler(self, scheduler, job):
        cron.add_to_scheduler(self, scheduler, job)

    def clear_from_scheduler(self, scheduler):
        scheduler.clear(self.uuid)

    def set_hook(self, hook):
        self.hook = hook

    @staticmethod
    def generate_from_json(data):
        values = Website.defaultValues
        if "url" not in data:
            raise KeyError("URL not found")
        values["url"] = data
        for key in values.keys():
            if key in data:
                values[key] = data[key]
        return Website(values["url"], values["credentials"], values["rule"])
