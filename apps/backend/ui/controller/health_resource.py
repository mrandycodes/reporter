class HealthResource:

    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.media = None
