# Beta Version
# Version Hash: A8C0FED824143AE0192CBFE663AAD73B586DC9D6

# --- Import Modules
from flask import Flask, render_template, request

# --- Config
server_passcode = "cake"

# --- Flask
app = Flask(__name__)

# --- Post Routing
@app.route('/api/vm/startvm')
def HyperV_StartVM():
  if request.form['passcode'] != server_passcode:
    return "{'result':'Mismatched passcode'}"
  else:
    return StartVM(request.form['vm_name'])
  
@app.route('/api/vm/stopvm')
def HyperV_StopVM():
  if request.form['passcode'] != server_passcode:
    return "{'result':'Mismatched passcode'}"
  else:
    return StopVM(request.form['vm_name'])
  
@app.route('/api/vm/startvm')
def HyperV_SaveVM():
  if request.form['passcode'] != server_passcode:
    return "{'result':'Mismatched passcode'}"
  else:
    return SaveVM(request.form['vm_name'])

# --- Command Executers
def StartVM(__vm):
  os.system(f"powershell -NoProfile -NoExit -Command Start-VM -Name '{__vm}'")

def StopVM(__vm):
  os.system(f"powershell -NoProfile -NoExit -Command Stop-VM -Name '{__vm}'")
  
def SaveVM(__vm):
  os.system(f"powershell -NoProfile -NoExit -Command Save-VM -Name '{__vm}'")
