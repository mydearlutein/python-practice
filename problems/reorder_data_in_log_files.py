import argparse
import re

def reorder_data_in_log_files(self, logs: List[str]) -> List[str]:
    logs_with_identifiers = [log.split(" ", 1) for log in logs]

    letter_logs = []
    digit_logs = []

    for i, log in enumerate(logs_with_identifiers):
        if re.match(r"^[ 0-9]+$", log[1]):
            digit_logs.append({'seq': i, 'id': log[0], 'log_val': log[1]})
        else:
            letter_logs.append({'seq': i, 'id': log[0], 'log_val': log[1]})

    letter_logs = sorted(letter_logs, key=lambda x: (x['log_val'],x['id']))

    sorted_letter_log_list = ["{} {}".format(log['id'], log['log_val']) for log in letter_logs]
    sorted_digit_log_list = ["{} {}".format(log['id'], log['log_val']) for log in digit_logs]

    return sorted_letter_log_list + sorted_digit_log_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reorder data in log files")
    parser.add_argument("logs", required=True, tyep=List[str], help="list of log data")

    args = parser.parse_args()
    print("reordered results:", reorder_data_in_log_files(args.logs))
