# reflex-aws-rds-deletion-protection-disabled
Rule to detect when deletion protection is disabled for an RDS instance.

## Usage
To use this rule either add it to your `reflex.yaml` configuration file:  
```
rules:
  - reflex-aws-rds-deletion-protection-disabled:
```

or add it directly to your Terraform:  
```
...

module "reflex-aws-rds-deletion-protection-disabled" {
  source           = "github.com/cloudmitigator/reflex-aws-rds-deletion-protection-disabled"
}

...
```

## License
This Reflex rule is made available under the MPL 2.0 license. For more information view the [LICENSE](https://github.com/cloudmitigator/reflex-aws-rds-deletion-protection-disabled/blob/master/LICENSE) 
