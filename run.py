print("Debug: Starting run.py")
from app import app
print("Debug: Imported app from app.py")

if __name__ == '__main__':
    print("Debug: __main__ block in run.py")
    print("Starting Flask web server from run.py...")
    app.run(debug=True, host='0.0.0.0', port=5000)
else:
    print("Debug: run.py is being imported, not run directly")