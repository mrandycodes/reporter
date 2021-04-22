import falcon
from apps.backend.ui.controller.health_resource import HealthResource

app = falcon.App()
app.add_route('/_health', HealthResource())
