import json
import time
import schedule
from .website import Website


def ping(website):
    print(website)


class Pyngr(object):

    def __init__(self, hook, job=ping):
        self.websites = []
        self.scheduler = schedule.Scheduler()
        self.hook = hook
        self.job = job

    def __str__(self):
        output = ""
        for website in self.websites:
            output += str(website) + "\n"
        return output

    def add_website(self, website):
        website.set_hook(self.hook)
        website.add_to_scheduler(self.scheduler, self.job)
        self.websites.append(website)

    def new_website(self, url,
                    credentials=Website.defaultValues["credentials"],
                    rule=Website.defaultValues["rule"]):
        self.add_website(Website(url, credentials, rule))

    def new_website_from_json(self, website):
        self.add_website(Website.generate_from_json(website))

    def import_config(self, filename):
        with open(filename, encoding="ascii") as configFile:
            data = json.load(configFile)
            for website in data["websites"]:
                self.new_website_from_json(website)

    def run(self, sleep=1, debug=False):
        while True:
            if debug:
                print(self.scheduler.jobs)
            self.scheduler.run_pending()
            time.sleep(sleep)
