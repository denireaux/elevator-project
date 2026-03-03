# Elevator Simulation Logic

A robust Python CLI tool that simulates elevator travel. It calculates the total travel time based on a constant speed and tracks the sequence of floors visited, starting from a specific floor.

## Quick Start

### Prerequisites

- Python 3.12+
- pytest (for running the test suite)

### Installation

Clone the repository.

(Optional) Create and activate a virtual environment:

```bash
# Windows MNGW64
python -m venv venv
source venv/Scripts/activate

# WSL
python -m venv venv
source venv/bin/activate
```

Install project dependencies:
```
pip install -r requirements.txt
```

## Running the Script
The script uses positional arguments via CLI. The first number is the starting floor, followed by any number of target floors.
```bash
# Expected Output -> 
    # Total travel time (seconds): 560s
    # Elevator path: 12, 2, 9, 1, 32
python elevator.py 12 2 9 1 32
```

## Testing
The project uses pytest for unit testing the core logic.
To run tests from the project root:

```
python -m pytest
```

## Documented Assumptions
### Chronological Execution

The elevator visits floors in the exact order provided by the user. It does not reorder or optimize the path (e.g., it does not use a SCAN/Elevator algorithm).

### Travel Constant

The time taken to travel between floors is calculated as: |(Current Floor - Next Floor)| x 10.

### Instantaneous Stops
Total travel time accounts only for the movement between floors; it assumes 0 seconds for door operations or passenger boarding.

### Input Handling
The script assumes all inputs are integers. Non-integer inputs will trigger a CLI validation error.

# Project Structure
elevator.py: The main entry point that connects the CLI parser to the core logic.

src/elevator_core.py: Contains the mathematical logic for travel time and path tracking.

src/parse_cli_args.py: Handles command-line argument validation using argparse.

tests/: Contains pytest test cases to ensure logic accuracy.
