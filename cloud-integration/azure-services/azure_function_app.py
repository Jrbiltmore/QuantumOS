from azure.identity import ClientSecretCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.web import WebSiteManagementClient

# Azure Setup - fill these in with your details
TENANT_ID = 'your-tenant-id'
CLIENT_ID = 'your-client-id'
CLIENT_SECRET = 'your-client-secret'
SUBSCRIPTION_ID = 'your-subscription-id'

# Resource and Function App Configurations
RESOURCE_GROUP_NAME = 'your-resource-group-name'
LOCATION = 'eastus'
FUNCTION_APP_NAME = 'your-function-app-name'

# Authenticate and create management clients
credential = ClientSecretCredential(tenant_id=TENANT_ID, client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
resource_client = ResourceManagementClient(credential, SUBSCRIPTION_ID)
web_client = WebSiteManagementClient(credential, SUBSCRIPTION_ID)

def create_resource_group():
    print("Creating resource group...")
    resource_group = resource_client.resource_groups.create_or_update(RESOURCE_GROUP_NAME, {'location': LOCATION})
    print(f"Resource group '{RESOURCE_GROUP_NAME}' created.")

def create_function_app():
    print("Creating function app...")
    # For simplification, using an existing App Service Plan. Replace with your plan's details or create a new one.
    app_service_plan_id = f"/subscriptions/{SUBSCRIPTION_ID}/resourceGroups/{RESOURCE_GROUP_NAME}/providers/Microsoft.Web/serverfarms/your-app-service-plan"
    web_client.web_apps.create_or_update(RESOURCE_GROUP_NAME, FUNCTION_APP_NAME, {
        'location': LOCATION,
        'server_farm_id': app_service_plan_id,
    })
    print(f"Function app '{FUNCTION_APP_NAME}' created.")

def list_function_apps():
    print("Listing function apps in subscription...")
    for function_app in web_client.web_apps.list():
        print(function_app.name)

def delete_function_app():
    print(f"Deleting function app '{FUNCTION_APP_NAME}'...")
    web_client.web_apps.delete(RESOURCE_GROUP_NAME, FUNCTION_APP_NAME)
    print(f"Function app '{FUNCTION_APP_NAME}' deleted.")

if __name__ == '__main__':
    create_resource_group()
    create_function_app()
    list_function_apps()
    delete_function_app()
