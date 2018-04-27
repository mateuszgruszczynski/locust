from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):
   
    @task
    def index(self):
        self.client.get("/")
        self.client.get("/")
        self.client.get("/")
        self.client.get("/")
        self.client.get("/")

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = "http://34.246.0.51:8081"
    min_wait = 5
    max_wait = 5
