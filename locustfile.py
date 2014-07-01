from locust import HttpLocust, TaskSet, task, events
from locust.stats import global_stats

class MyPerformanceTask(TaskSet):
    @task
    def index(self):
      self.client.get("/")

class MyLocust(HttpLocust):
    task_set = MyPerformanceTask
    min_wait = 5000
    max_wait = 15000
    host = "http://www.noppanit.com"

def on_request_success(request_type, name, response_time, response_length):
    print 'on success'


def on_quitting():
    aggregated_stats = global_stats.aggregated_stats("Total").get_stripped_report()

    f = open('stats.json','w')
    f.write(str(aggregated_stats))
    f.close()


events.quitting += on_quitting
