import tempfile
import unittest
from pathlib import Path

from lib.argus_result_contract import load_contract, validate_result, write_contract


class ArgusResultContractTests(unittest.TestCase):
    def test_valid_contract_round_trip(self):
        payload = {
            "mission_id": "mis_test",
            "dispatch_id": "disp_test",
            "project_id": "proj_test",
            "attempt_id": "argus-1",
            "run_dir": "/tmp/run",
            "summary_file": "/tmp/run/summary.txt",
            "overall": "PASS",
            "recommendation": "candidate_for_promotion",
            "atlas_overall": "PASS",
            "atlas_recommendation": "new_test",
        }
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "argus_result.json"
            write_contract(path, payload)
            loaded = load_contract(path)
        self.assertEqual(loaded["attempt_id"], "argus-1")
        self.assertEqual(loaded["overall"], "PASS")

    def test_fail_requires_reason_fields(self):
        with self.assertRaises(ValueError):
            validate_result(
                {
                    "attempt_id": "argus-1",
                    "run_dir": "/tmp/run",
                    "summary_file": "/tmp/run/summary.txt",
                    "overall": "FAIL",
                    "recommendation": "stop",
                }
            )

    def test_dispatch_requires_mission(self):
        with self.assertRaises(ValueError):
            validate_result(
                {
                    "dispatch_id": "disp_test",
                    "attempt_id": "argus-1",
                    "run_dir": "/tmp/run",
                    "summary_file": "/tmp/run/summary.txt",
                    "overall": "INCONCLUSIVE",
                    "recommendation": "new_test",
                }
            )


if __name__ == "__main__":
    unittest.main()
