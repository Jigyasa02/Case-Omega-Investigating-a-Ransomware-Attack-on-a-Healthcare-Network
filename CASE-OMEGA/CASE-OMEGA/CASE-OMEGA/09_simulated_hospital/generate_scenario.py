"""Generate fictional hospital records and event logs for Case Omega."""
from pathlib import Path
import csv, json
ROOT = Path(__file__).resolve().parent
records = ROOT / "patient_records"
server = ROOT / "server"
workstation = ROOT / "workstation"
logs = ROOT.parent / "04_timeline_analysis" / "sample_logs"
for p in (records, server, workstation, logs):
    p.mkdir(parents=True, exist_ok=True)

dummy = {
 "DEMO_PATIENT_001.txt":"FICTIONAL PATIENT: Demo Person 001\nRecord ID: DEMO-001\nNo real health information.\n",
 "DEMO_PATIENT_002.txt":"FICTIONAL PATIENT: Demo Person 002\nRecord ID: DEMO-002\nNo real health information.\n",
 "DEMO_PATIENT_003.txt":"FICTIONAL PATIENT: Demo Person 003\nRecord ID: DEMO-003\nNo real health information.\n"
}
for name, content in dummy.items():
    (records/name).write_text(content, encoding="utf-8")
(server/"server_readme.txt").write_text("Fictional Omega Care Hospital file server. Training data only.\n", encoding="utf-8")
(workstation/"employee_readme.txt").write_text("Fictional workstation image folder. Training data only.\n", encoding="utf-8")

events = [
 ["2026-11-24T08:42:00Z","EMAIL_GATEWAY","mail-001","Phishing email delivered","sender=records-update@example.invalid; attachment=Invoice_Update.zip"],
 ["2026-11-24T08:47:13Z","WORKSTATION","ws-014","Attachment opened","user=training.user; file=Invoice_Update.zip"],
 ["2026-11-24T08:49:02Z","IDENTITY","id-021","Unusual login success","account=svc_backup; source_ip=192.0.2.44"],
 ["2026-11-24T08:53:40Z","NETWORK","net-033","Outbound connection observed","destination=198.51.100.23; port=443; label=synthetic"],
 ["2026-11-24T09:02:11Z","USB","usb-004","USB storage inserted","device=TRAINING-USB-01; host=ws-014"],
 ["2026-11-24T09:11:55Z","FILE_SERVER","fs-051","Bulk file modification activity","host=fs-01; count=3; extension=.OMEGA_SIMULATED"],
 ["2026-11-24T09:14:20Z","FILE_SERVER","fs-052","Ransom note created","host=fs-01; file=README_RESTORE_OMEGA.txt"],
 ["2026-11-24T09:18:00Z","SOC","soc-010","Incident declared","severity=high; case=OMEGA-2026-001"],
 ["2026-11-24T09:26:30Z","NETWORK","net-041","Affected workstation isolated","host=ws-014; action=network_isolation"],
 ["2026-11-24T10:16:00Z","FORENSICS","for-001","Evidence preservation started","operator=training.investigator"]
]
with (logs/"system_events.csv").open("w", newline="", encoding="utf-8") as f:
    w=csv.writer(f); w.writerow(["timestamp_utc","source","event_id","event","details"]); w.writerows(events)
with (logs/"login_records.csv").open("w", newline="", encoding="utf-8") as f:
    w=csv.writer(f); w.writerow(["timestamp_utc","account","source_ip","result"]); w.writerows([
      ["2026-11-24T08:49:02Z","svc_backup","192.0.2.44","SUCCESS"],
      ["2026-11-24T08:50:31Z","training.user","10.10.20.14","SUCCESS"],
      ["2026-11-24T08:51:12Z","admin-temp","192.0.2.44","FAILURE"]
    ])
with (logs/"network_events.csv").open("w", newline="", encoding="utf-8") as f:
    w=csv.writer(f); w.writerow(["timestamp_utc","source_ip","destination_ip","destination_port","event"]); w.writerows([
      ["2026-11-24T08:53:40Z","10.10.20.14","198.51.100.23","443","SYNTHETIC_OUTBOUND"],
      ["2026-11-24T09:05:02Z","10.10.20.14","10.10.20.5","445","SYNTHETIC_SMB"]
    ])
with (logs/"usb_events.csv").open("w", newline="", encoding="utf-8") as f:
    w=csv.writer(f); w.writerow(["timestamp_utc","host","device_id","event"]); w.writerow(["2026-11-24T09:02:11Z","ws-014","TRAINING-USB-01","INSERTED"])
print("Scenario generated: fictional patient files, server/workstation folders, and synthetic logs.")
