from django.db import models

from core.constants import InformationPresentationTypes
from core.direct_sql_worker.server_time import get_server_time_now


class BaseUserInformation(models.Model):
    ip_address = models.CharField(max_length=50, blank=True, null=True)
    is_ipv6 = models.BooleanField(default=False)
    user_agent = models.TextField(blank=True, null=True, default=InformationPresentationTypes.NOT_PRESENTED)
    operation_system = models.CharField(max_length=100, default=InformationPresentationTypes.NOT_PRESENTED)
    browser_name = models.CharField(max_length=100, blank=True, null=True,
                                    default=InformationPresentationTypes.NOT_PRESENTED)
    request_dt = models.DateTimeField(default=get_server_time_now)

    class Meta:
        abstract = True