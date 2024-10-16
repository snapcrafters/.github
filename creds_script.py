#!/usr/bin/env python3
import sys
import tempfile
from launchpadlib.launchpad import Launchpad
from launchpadlib.uris import LPNET_SERVICE_ROOT

with tempfile.NamedTemporaryFile("w+") as credentials_file:

    Launchpad.login_with(
        application_name="Snapcrafters CI",
        service_root=LPNET_SERVICE_ROOT,
        credentials_file=credentials_file.name,
        version="devel",
        consumer_name="Snapcrafters CI"
    )

    print(credentials_file.read())
