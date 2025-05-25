import requests
import time

THEHIVE_URL = "http://192.168.1.19:9000"
API_KEY = "AhpOlsf/////////5Ef1MH1JyJUTiEAyytytytyyvdVmgshdghsfddddddsssssss/////////////SK342626bH9O"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

RESPONDER_VT = "Virustotal_Downloader_0_1"
RESPONDER_MISP = "put here any responder name"

def get_alerts():
    url = f"{THEHIVE_URL}/api/v1/alert"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"[-] Failed to fetch alerts: {response.status_code}")
        print(response.text)
        return []

def run_responder(alert_id, responder_name):
    url = f"{THEHIVE_URL}/api/v1/responder/{responder_name}/run"
    payload = {
        "inputId": alert_id,
        "inputType": "alert"
    }
    response = requests.post(url, json=payload, headers=HEADERS)
    if response.status_code == 200:
        print(f"[+] Responder '{responder_name}' ran on alert {alert_id}")
    else:
        print(f"[-] Failed to run responder '{responder_name}': {response.status_code}")
        print(response.text)

def update_alert_status(alert_id, status="Ignored"):
    url = f"{THEHIVE_URL}/api/v1/alert/{alert_id}"
    payload = {"status": status}
    response = requests.patch(url, json=payload, headers=HEADERS)
    print(f"[~] Updated alert {alert_id} status to {status}")

def main():
    alerts = get_alerts()
    for alert in alerts:
        alert_id = alert.get("id")
        if alert.get("status") == "New":
            observables = alert.get("observables", [])
            if any(o.get("dataType") in ["ip", "domain"] for o in observables):
                print(f"[+] Alert {alert_id} contains IP/domain. Running responders...")
                run_responder(alert_id, RESPONDER_VT)
                time.sleep(10)
                run_responder(alert_id, RESPONDER_MISP)
                update_alert_status(alert_id, "Ignored")

if __name__ == "__main__":
    main()
