"""Launch the Urban Research dashboard."""
import subprocess
import sys
from pathlib import Path

app_path = Path(__file__).parent / "app" / "dashboard.py"
subprocess.run(
    [sys.executable, "-m", "streamlit", "run", str(app_path),
     "--server.headless", "true"],
)
