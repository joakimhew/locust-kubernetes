from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    @task(4)
    def testTask(self):
        self.client.get("/")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 2000