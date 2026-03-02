import argparse

def parse_cli_args():
    parser = argparse.ArgumentParser(description="For initial settings in the elevator simulation.")
    
    parser.add_argument("start", type=int, help="The floor the elevator will start on.")
    parser.add_argument("floors", type=int, nargs='+', 
                        help="The floors, chronologically, the elevator will visit.")

    args = parser.parse_args()
    
    return args.start, args.floors
