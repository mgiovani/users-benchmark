from locust import HttpUser, task

class CreateUser(HttpUser):
    @task
    def create_user(self):
        self.client.post("/", json={"name": "test name", "email": "test email"})
