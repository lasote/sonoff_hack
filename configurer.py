import requests
from requests import ConnectTimeout


def get_credentials():
    try:
        ret = requests.get("http://10.10.7.1/device", timeout=5 )
        if ret.status_code == 200:
            return ret.json()
        return None
    except (ConnectTimeout, ConnectionError):
        return None


def send_config():
    payload = {
      "version": 4,
      "ssid": "NUITO",
      "password": "xxxxxx",
      "serverName": "192.168.1.41",
      "port": "9001"
    }
    requests.post("http://10.10.7.1/ap", json=payload)


if __name__ == "__main__":

    print("\n***********************************************************\n\n"
          "- Connect the sonoff and press the button for few seconds\n"
          "- Scan your wifi networks and connect to ITEAD-10000XXX\n"
          "- Use password: 12345678\n"
          "\n***********************************************************")

    input("Press Enter to continue.")

    print("Waiting for the device...")
    while True:
        credentials = get_credentials()
        if credentials:
            send_config()
        else:
            print("Not connected...")

    print("Connected to the device!! %s" % credentials)


