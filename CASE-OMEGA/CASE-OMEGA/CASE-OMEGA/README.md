\# CASE OMEGA

\## Healthcare Ransomware Investigation \& Digital Forensics

\*\*Educational Simulation\*\*



\*\*Case ID:\*\* OMEGA-2026-001  

\*\*Organization:\*\* Omega Care Hospital (Fictional)  

\*\*Incident Window:\*\* 2026-11-24 08:42–10:16 UTC  

\*\*Status:\*\* Simulated / Closed for Academic Demonstration



\## 1. Overview



Case Omega is an end-to-end digital forensics exercise that simulates a ransomware incident at a fictional hospital.



The project demonstrates:

\- First responder procedures and scene documentation.

\- Digital evidence collection and preservation.

\- SHA-256 evidence hashing and verification.

\- Chain-of-custody documentation.

\- Safe ransomware behavior simulation.

\- Malware behavior analysis and indicators of compromise (IOCs).

\- Attack timeline reconstruction using synthetic logs.

\- Preparation of a digital forensic investigation report.



\### Safety and Authenticity Notice



No real hospital, patient, account, or attacker is involved. All patient records, timestamps, IP addresses, logs, IOCs, and evidence are fictional.



The ransomware simulator only encrypts copies of dummy files inside the project. Original files are preserved. It does not spread, establish persistence, contact external hosts, disable security tools, or modify operating-system files.



This is an educational simulation, not a real forensic acquisition or a legally certified expert report.



\## 2. Requirements



\- Python 3.10 or later

\- Git (for repository management)

\- Visual Studio Code (recommended)



\## 3. Setup Instructions (Windows PowerShell)



Open the project folder in PowerShell.



\### Step 1: Create a virtual environment



```powershell

py -m venv .venv

```



\### Step 2: Activate the environment



```powershell

.\\.venv\\Scripts\\Activate.ps1

```



If PowerShell blocks activation, run:



```powershell

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

.\\.venv\\Scripts\\Activate.ps1

```



\### Step 3: Install dependencies



```powershell

py -m pip install -r requirements.txt

```



\## 4. Run the Investigation



Run these commands one at a time from the main project folder.



\### Step 1: Generate the simulated hospital scenario



```powershell

py 09\_simulated\_hospital\\generate\_scenario.py

```



This creates fictional patient records and synthetic system, login, network, and USB logs.



\### Step 2: Run the safe ransomware simulator



```powershell

py 03\_malware\_analysis\\safe\_ransomware\_simulator.py

```



This demonstrates ransomware-like encryption on copies of dummy files. Original files remain unchanged.



\### Step 3: Reconstruct the attack timeline



```powershell

py 04\_timeline\_analysis\\analyze\_logs.py

```



This generates:

\- `attack\_timeline.csv`

\- `timeline.png`



\### Step 4: Acquire the simulated evidence package



```powershell

py 02\_evidence\_collection\\acquire\_image.py

```



\### Step 5: Verify the SHA-256 hash



```powershell

py 02\_evidence\_collection\\calculate\_hash.py

```



The generated hash can be compared with the acquisition output to verify integrity.



\## 5. Repository Structure



| Folder | Description |

|---|---|

| `01\_first\_responder/` | SOP, scene sketch, evidence tags |

| `02\_evidence\_collection/` | Evidence acquisition, hashing, chain of custody, manifest |

| `03\_malware\_analysis/` | Safe simulator, ransom note, malware analysis, fictional IOCs |

| `04\_timeline\_analysis/` | Synthetic logs, timeline analysis script, CSV and PNG |

| `05\_investigation\_report/` | Investigation report in Markdown, DOCX and PDF |

| `07\_documentation/` | Tools used, workflow and authorship declaration |

| `08\_screenshots/` | Genuine screenshots captured during project execution |

| `09\_simulated\_hospital/` | Fictional hospital records and scenario generator |

| `.github/workflows/` | Automated project validation |



\## 6. Important Forensic Limitations



The generated `simulated\_server\_image.tar` is a logical evidence package containing fictional server files. It is NOT a bit-for-bit physical disk image.



For actual forensic disk acquisition in a controlled laboratory, use a legally authorized test disk and a validated imaging tool such as FTK Imager.



Never acquire data from a real hospital or another person's device without proper written authorization.



\## 7. Academic Use



Before submission:



1\. Review all generated files and reports.

2\. Replace authorship placeholders with your own details.

3\. Run the scripts and verify their outputs.

4\. Capture genuine screenshots of your execution.

5\. Review the evidence and understand the investigation process.

6\. Be prepared to explain the methods, findings, and limitations.



\*\*Important:\*\* Never present synthetic evidence as evidence collected from a real cybercrime incident.

