import os
import subprocess
import time
import unittest
from pathlib import Path

from lib.argus_result_contract import load_contract

ARGUS_ROOT = Path(__file__).resolve().parents[1]
ARGUS_BIN = str(ARGUS_ROOT / "bin" / "argus-research-run")
LOCK_DIR = ARGUS_ROOT / "logs" / "dispatch"


def parse_envelope(text: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for line in text.splitlines():
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        data[key] = value
    return data


class ArgusRunnerGuardTests(unittest.TestCase):
    def test_invalid_project_binding_writes_valid_contract(self):
        env = os.environ.copy()
        env["ARGUS_OPERATOR_PROJECT_ID"] = "bad"
        env["ARGUS_WORKSPACE_ROOT"] = str(ARGUS_ROOT)
        proc = subprocess.run([ARGUS_BIN, "status"], text=True, capture_output=True, env=env)
        self.assertNotEqual(proc.returncode, 0)
        envelope = parse_envelope(proc.stdout)
        self.assertEqual(envelope["REASON_CODE"], "contract_invalid")
        contract = load_contract(envelope["RESULT_JSON"])
        self.assertEqual(contract["failure_class"], "contract_failure")

    def test_duplicate_dispatch_blocked_before_execution(self):
        dispatch_id = f"disp-test-{os.getpid()}"
        lock_path = LOCK_DIR / f"{dispatch_id}.lock"
        lock_path.parent.mkdir(parents=True, exist_ok=True)
        lock_path.write_text(f"pid={os.getpid()}\nts={int(time.time())}\nattempt_id=test-attempt\n", encoding="utf-8")
        env = os.environ.copy()
        env["ARGUS_DISPATCH_ID"] = dispatch_id
        env["ARGUS_MISSION_ID"] = "mis_test"
        env["ARGUS_WORKSPACE_ROOT"] = str(ARGUS_ROOT)
        try:
            proc = subprocess.run([ARGUS_BIN, "status"], text=True, capture_output=True, env=env)
        finally:
            lock_path.unlink(missing_ok=True)
        self.assertNotEqual(proc.returncode, 0)
        envelope = parse_envelope(proc.stdout)
        self.assertEqual(envelope["REASON_CODE"], "duplicate_dispatch_blocked")
        contract = load_contract(envelope["RESULT_JSON"])
        self.assertEqual(contract["failure_class"], "resource_contention")


if __name__ == "__main__":
    unittest.main()
