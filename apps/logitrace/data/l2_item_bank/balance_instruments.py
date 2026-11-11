"""
Script to balance option keys and reasoning keys for TOLT and NEDV instruments.
Ensures zero position bias across options {"A", "B", "C", "D"} and reasoning keys {"1", "2", "3"}.
"""

import json
import os

BASE_DIR = os.path.dirname(__file__)
TOLT_PATH = os.path.join(BASE_DIR, "tolt_test_parallel.json")
NEDV_PATH = os.path.join(BASE_DIR, "nedv_control_items.json")


def balance_tolt():
    with open(TOLT_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Balanced target option keys for 10 items in Form A & Form B
    # 3 A, 3 B, 2 C, 2 D (sum = 10)
    target_options_a = ["A", "B", "C", "D", "B", "C", "D", "A", "B", "A"]
    target_reasons_a = ["1", "2", "3", "1", "2", "3", "1", "2", "3", "1"]

    target_options_b = ["B", "A", "D", "C", "A", "B", "C", "D", "A", "C"]
    target_reasons_b = ["2", "1", "3", "2", "1", "3", "2", "1", "3", "2"]

    for form_name, target_opts, target_reasons in [
        ("form_a", target_options_a, target_reasons_a),
        ("form_b", target_options_b, target_reasons_b),
    ]:
        items = data[form_name]
        for i, item in enumerate(items):
            # 1. Clean up option E if present (e.g., TOLT_B_PB_02)
            if "E" in item["options"]:
                del item["options"]["E"]

            cur_correct_opt = item["correct_option"]
            target_opt = target_opts[i]

            if cur_correct_opt != target_opt:
                # Swap the text of cur_correct_opt and target_opt
                text_correct = item["options"][cur_correct_opt]
                text_target = item["options"][target_opt]
                item["options"][target_opt] = text_correct
                item["options"][cur_correct_opt] = text_target
                item["correct_option"] = target_opt

            # 2. Balance reasoning options
            cur_correct_reason = item["correct_reasoning"]
            target_reason = target_reasons[i]
            if cur_correct_reason != target_reason:
                text_r_correct = item["reasoning_options"][cur_correct_reason]
                text_r_target = item["reasoning_options"][target_reason]
                item["reasoning_options"][target_reason] = text_r_correct
                item["reasoning_options"][cur_correct_reason] = text_r_target
                item["correct_reasoning"] = target_reason

    with open(TOLT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("TOLT parallel test successfully balanced.")


def balance_nedv():
    with open(NEDV_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 6 items: target keys ["A", "B", "C", "D", "B", "C"]
    target_keys = ["A", "B", "C", "D", "B", "C"]

    for i, item in enumerate(data["items"]):
        cur_ans = item["correct_answer"]
        target = target_keys[i]
        if cur_ans != target:
            text_correct = item["options"][cur_ans]
            text_target = item["options"][target]
            item["options"][target] = text_correct
            item["options"][cur_ans] = text_target
            item["correct_answer"] = target

    with open(NEDV_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("NEDV items successfully balanced.")


if __name__ == "__main__":
    balance_tolt()
    balance_nedv()
