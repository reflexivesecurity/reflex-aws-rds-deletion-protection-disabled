module "reflex_aws_rds_deletion_protection_disabled" {
  source           = "git::https://github.com/cloudmitigator/reflex-engine.git//modules/cwe_lambda?ref=v0.5.8"
  rule_name        = "RDSDeletionProtectionDisabled"
  rule_description = "Rule to detect if deletion protection is disabled for RDS Instance."

  event_pattern = <<PATTERN
{
  "source": [
    "aws.rds"
  ],
  "detail-type": [
    "AWS API Call via CloudTrail"
  ],
  "detail": {
    "eventSource": [
      "rds.amazonaws.com"
    ],
    "eventName": [
      "ModifyDBInstance"
    ]
  }
}

PATTERN

  function_name   = "RDSDeletionProtectionDisabled"
  source_code_dir = "${path.module}/source"
  handler         = "reflex_aws_rds_deletion_protection_disabled.lambda_handler"
  lambda_runtime  = "python3.7"
  environment_variable_map = {
    SNS_TOPIC = var.sns_topic_arn,
    
  }


  queue_name    = "RDSDeletionProtectionDisabled"
  delay_seconds = 0

  target_id = "RDSDeletionProtectionDisabled"

  sns_topic_arn  = var.sns_topic_arn
  sqs_kms_key_id = var.reflex_kms_key_id
}
