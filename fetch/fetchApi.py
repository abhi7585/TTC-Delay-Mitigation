import requests
import os

# Toronto Open Data is stored in a CKAN instance. It's APIs are documented here:
# https://docs.ckan.org/en/latest/api/

# To hit our API, we'll be making requests to:
base_url = "https://ckan0.cf.opendata.inter.prod-toronto.ca"

# Datasets are called "packages". Each package can contain many "resources"
# To retrieve the metadata for this package and its resources, use the package name in this page's URL:
url = base_url + "/api/3/action/package_show"
params = {"id": "ttc-bus-delay-data"}
package = requests.get(url, params=params).json()

# Create a folder named "DATA" if it doesn't exist
data_folder = "DATA2"
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

# To download resource files:
for idx, resource in enumerate(package["result"]["resources"]):
    if not resource["datastore_active"]:
        resource_url = resource["url"]  # the URL directly points to the file
        filename = os.path.basename(resource_url)
        filepath = os.path.join(data_folder, filename)
        print(f"Downloading {filename}...")
        response = requests.get(resource_url)
        with open(filepath, "wb") as file:
            file.write(response.content)
        print(f"{filename} downloaded successfully into {data_folder}.")
