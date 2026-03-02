from src.elevator_core import core_elevator_logic
from src.parse_cli_args import parse_cli_args

def main():
    start_floor, floors_to_visit = parse_cli_args()
    
    total_time, visited_log = core_elevator_logic(start_floor, floors_to_visit)
    
    path_string = ",".join(map(str, visited_log))
    print(f"{total_time} {path_string}")

if __name__ == "__main__":
    main()
