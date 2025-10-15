
import os

LOG_FILE = 'sample.log'

def analyze_log(file_path):
    
    if not os.path.exists(file_path):
        print(f"Hata: {file_path} dosyası bulunamadı.")
        return

    error_count = 0
    warning_count = 0
    info_count = 0
    total_lines = 0

    with open(file_path, 'r') as f:
        for line in f:
            total_lines += 1
            line = line.strip().upper()
            if 'ERROR' in line:
                error_count += 1
            elif 'WARNING' in line:
                warning_count += 1
            elif 'INFO' in line:
                info_count += 1

    print("\n--- Log Analysis Summary ---")
    print(f"Total Lines Processed: {total_lines}")
    print(f"INFO Count: {info_count}")
    print(f"WARNING Count: {warning_count}")
    print(f"ERROR Count: {error_count}")
    print("----------------------------\n")

if __name__ == "__main__":
    analyze_log(LOG_FILE)
