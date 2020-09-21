""" Module for RDSDeletionProtectionDisabled """

import json
import os

import boto3
from reflex_core import AWSRule, subscription_confirmation


class RDSDeletionProtectionDisabled(AWSRule):
    """ Rule to detect when deletion protection is disabled for RDS. """

    def __init__(self, event):
        super().__init__(event)

    def extract_event_data(self, event):
        """ Extract required event data """
        self.db_instance_id = event["detail"]["requestParameters"][
            "dBInstanceIdentifier"
        ]
        self.deletion_protection = event["detail"]["requestParameters"][
            "deletionProtection"
        ]

    def resource_compliant(self):
        """
        Determine if the resource is compliant with your rule.

        Return True if it is compliant, and False if it is not.
        """
        return self.deletion_protection

    def get_remediation_message(self):
        """ Returns a message about the remediation action that occurred """
        return f"The DB instance {self.db_instance_id} has had deletion protection disabled."


def lambda_handler(event, _):
    """ Handles the incoming event """
    print(event)
    event_payload = json.loads(event["Records"][0]["body"])
    if subscription_confirmation.is_subscription_confirmation(event_payload):
        subscription_confirmation.confirm_subscription(event_payload)
        return
    rule = RDSDeletionProtectionDisabled(event_payload)
    rule.run_compliance_rule()
