import aws_cdk as core
import aws_cdk.assertions as assertions

from metrics_service.metrics_service_stack import MetricsServiceStack

# example tests. To run these tests, uncomment this file along with the example
# resource in metrics_service/metrics_service_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MetricsServiceStack(app, "metrics-service")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
