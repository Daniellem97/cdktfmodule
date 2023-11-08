from constructs import Construct
from cdktf import App, TerraformStack
from imports.aws import AwsProvider

class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)
        
        AwsProvider(self, 'Aws', region='us-east-1')
        
        # Define your resources here

app = App()
MyStack(app, "my-cdktf-project")
app.synth()
