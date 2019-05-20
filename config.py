
farmLocation = "guyi"

minerConfig = {
    "debug": True,
    "minerLogin": {
        "minerPort": 80,
        "minerUser": "root",
        "minerPassword": "root"
    },
    "farm": {
        "farmLocation": farmLocation,
        "farmAdmin": "SOMEONE",
        "totalMiners": 30
    }
}

iotConfig = {
    "host": 'a1s6wepkits1h3-ats.iot.ap-southeast-1.amazonaws.com',
    "caPath": './cert2/root-CA.crt',
    "keyPath": './cert2/' + farmLocation + '_dev.private.key',
    "certPath": './cert2/' + farmLocation + '_dev.cert.pem.crt',
    "clientId": farmLocation,
    "generalInfoPublishTo": farmLocation + '/generalinfo',
    "minerDetailsPublishTo": farmLocation + '/minerdetails',
    "controlSubscribeTo": farmLocation + '/controlsignal',
    "controlPublishTo": farmLocation + '/controlfeedback',
    "scheduledPublishTo": 'fh/' + farmLocation + '/minerdetails'
}


dynamodb_config = {
    "region_name": 'ap-southeast-1',
    "aws_access_key_id": 'SOMEKEY',
    "aws_secret_access_key": 'SOMEKEY'
}

ssh_config = {
    "port": 22,
    "username": 'root',
    "password": 'admin',
    "reboot_command": '/sbin/reboot'
}

