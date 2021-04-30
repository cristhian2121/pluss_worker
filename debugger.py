# debugger.py
from os import getenv

def initialize_flask_server_debugger_if_needed():
    print('*** ***')
    if getenv("FLASK_DEBUG") == "True":
        
        import debugpy

        debugpy.listen(("0.0.0.0", 5713))
        print("⏳ VS Code debugger can now be attached, press F5 in VS Code ⏳", flush=True)
        debugpy.wait_for_client()
        print("🎉 VS Code debugger attached, enjoy debugging 🎉", flush=True)