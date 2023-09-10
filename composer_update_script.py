import json

def update_composer_json():
    # Read composer.json file to get dependencies
    with open('composer.json', 'r') as json_file:
        data = json.load(json_file)
        require = data.get('require', {})
        require_dev = data.get('require-dev', {})

    # Read composer.lock file to get installed package versions
    with open('composer.lock', 'r') as lock_file:
        lock_data = json.load(lock_file)
        installed_require_packages = {package['name']: package['version'].lstrip('v') for package in lock_data['packages']}
        installed_require_dev_packages = {package['name']: package['version'].lstrip('v') for package in lock_data['packages-dev']}

    # Update version constraints in composer.json for require
    for package, version in require.items():
        if version == '*':
            new_version = installed_require_packages.get(package)
            if new_version:
                data['require'][package] = "^" + new_version

    # Update version constraints in composer.json for require-dev
    for package, version in require_dev.items():
        if version == '*':
            new_version = installed_require_dev_packages.get(package)
            if new_version:
                data['require-dev'][package] = "^" + new_version

    # Write updated data back to composer.json
    with open('composer.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print("composer.json updated successfully.")

if __name__ == '__main__':
    update_composer_json()
