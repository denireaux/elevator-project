from src.parse_cli_args import parse_cli_args

def core_elevator_logic(start_floor, floors_to_visit):
    current_floor = start_floor
    total_time = 0
    visited_log = [start_floor]
    
    TRAVEL_CONSTANT = 10

    for next_floor in floors_to_visit:
        distance = abs(next_floor - current_floor)
        total_time += distance * TRAVEL_CONSTANT
        
        current_floor = next_floor
        visited_log.append(current_floor)
        
    return total_time, visited_log
